from ultralytics import YOLO

# load YOLOv11 model
model = YOLO("yolo11n.pt")

# run detection on image
results = model("dog.jpg", show=True)

# save output
results[0].save("output_yolo11.jpg")