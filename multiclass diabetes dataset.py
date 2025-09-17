import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv("diabetes_multiclass.csv")

# Drop ID-like columns
df = df.drop(["ID", "No_Pation"], axis=1)

# Encode categorical 'Gender'
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])  # F->0, M->1

# Features and Target
X = df.drop("CLASS", axis=1)
y = df["CLASS"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling (now all numeric)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Multinomial Logistic Regression
model = LogisticRegression(multi_class="multinomial", solver="lbfgs", max_iter=1000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
