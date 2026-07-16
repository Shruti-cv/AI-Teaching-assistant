# 📚 AI-Powered Teaching Assistant

An intelligent educational assistant that understands student queries using Machine Learning and Natural Language Processing, classifies the topic and intent, analyzes difficulty, and recommends personalized learning paths.

---

##  Features

-  Intent Classification using Machine Learning
-  Topic Classification across multiple Computer Science subjects
-  Semantic Query Understanding using Sentence Transformers (MiniLM)
-  Adaptive Learning Recommendations based on quiz performance
-  Difficulty Level Detection (Beginner, Intermediate, Advanced)
-  AI-based Response Generation (Gemini API integration with offline fallback)
-  Interactive Streamlit Web Application
-  Explainable outputs for better learning support

---

## System Architecture

```
Student Query
      │
Sentence Transformer (MiniLM)
      │
Intent Classification
      │
Topic Classification
      │
Difficulty Detection
      │
Adaptive Recommendation Engine
      │
Gemini AI Response
      │
Personalized Learning Recommendation
```

---

##  Project Structure

```
AI-Teaching-assistant/
│
├── app.py
├── README.md
├── .gitignore
│
├── data/
│   └── student_queries.csv
│
├── models/
│   ├── intent_model.pkl
│   └── topic_model.pkl
│
├── src/
│   ├── intent_classifier.py
│   ├── topic_classifier.py
│   ├── query_understanding.py
│   ├── recommendation_engine.py
│   ├── gemini_helper.py
│   ├── llm_refiner.py
│   └── main-system.py
│
└── docs/
```

---

## Technologies Used

- Python
- Streamlit
- Sentence Transformers (all-MiniLM-L6-v2)
- Scikit-learn
- Logistic Regression
- Pandas
- Hugging Face Transformers
- Google Gemini API
- Pickle
- Machine Learning
- NLP

---

## Dataset

The project uses a custom dataset containing **1000+ labeled student queries**.

### Topics

- Python
- Data Structures & Algorithms
- DBMS
- Object-Oriented Programming
- Operating Systems
- Computer Networks
- Artificial Intelligence
- SQL

### Intents

- Explanation
- Example
- Doubt
- Revision

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/Shruti-cv/AI-Teaching-assistant.git

cd AI-Teaching-assistant
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Application

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

##  Application Preview

### Input

(Add your screenshot here)

### Output

(Add your screenshot here)

---

### Sample Query

```
Explain Python
```

### Output

- Intent: Explanation
- Topic: Python
- Difficulty: Intermediate
- Adaptive Recommendation
- AI-generated Explanation

---

##  Model Performance

### Topic Classification Accuracy

**96%**

Machine Learning Model:

- Sentence Transformers
- Logistic Regression

---

## Future Enhancements

- Student login system
- Learning history tracking
- Quiz generation using AI
- Voice-based interaction
- RAG-based document retrieval
- Dashboard for teachers
- Personalized learning analytics

---

##  Author

**Gontu Sruthi**

B.Tech – Information Technology

GitHub:
https://github.com/Shruti-cv

---

## ⭐ If you found this project useful, please consider giving it a star!
