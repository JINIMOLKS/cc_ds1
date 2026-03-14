import cv2
import numpy as np

# ---------------- LOAD YOLO ----------------
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# ---------------- LOAD IMAGE ----------------
img = cv2.imread("images/dog.jpg")   # Change path if needed
height, width, _ = img.shape

# ---------------- CREATE BLOB ----------------
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# ---------------- GET OUTPUT LAYERS ----------------
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# ---------------- FORWARD PASS ----------------
outs = net.forward(output_layers)

# ---------------- STORE DETECTIONS ----------------
boxes = []
confidences = []
class_ids = []

conf_threshold = 0.5   # Confidence threshold

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > conf_threshold:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# ---------------- APPLY NON-MAX SUPPRESSION ----------------
nms_threshold = 0.4

indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

# ---------------- DRAW FINAL BOXES ----------------
for i in indices.flatten():
    x, y, w, h = boxes[i]
    label = f"{classes[class_ids[i]]} {confidences[i]:.2f}"

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, label, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# ---------------- SHOW OUTPUT ----------------
cv2.imshow("YOLOv3 Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
