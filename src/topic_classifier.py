import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load dataset
data = pd.read_csv("data/student_queries.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert queries to embeddings
X = model.encode(data["query"].tolist())

# Labels
y = data["topic"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
with open("models/topic_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Topic model trained and saved successfully!")
