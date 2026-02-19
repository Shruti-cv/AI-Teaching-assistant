import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer
from llm_refiner import refine_intent_with_llm

# Load trained models
intent_model = pickle.load(open("models/intent_model.pkl", "rb"))
topic_model = pickle.load(open("models/topic_model.pkl", "rb"))

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def detect_difficulty(query):
    query_lower = query.lower()

    if "basics" in query_lower or "what is" in query_lower:
        return "Beginner"
    elif "derive" in query_lower or "mathematically" in query_lower:
        return "Advanced"
    else:
        return "Intermediate"

def analyze_query(query):
    # Generate embedding
    embedding = embedding_model.encode([query])

    # Predict intent
    predicted_intent = intent_model.predict(embedding)[0]
    intent = refine_intent_with_llm(query, predicted_intent)

    # Predict topic
    topic = topic_model.predict(embedding)[0]

    # Detect difficulty
    difficulty = detect_difficulty(query)

    return {
        "intent": intent,
        "topic": topic,
        "difficulty_level": difficulty
    }

if __name__ == "__main__":
    user_query = input("Enter student query: ")
    result = analyze_query(user_query)
    print("\nPrediction:")
    print(result)

