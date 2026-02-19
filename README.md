# AI-Powered Teaching Assistant

## Overview
This project implements an AI-powered teaching assistant that:
1. Understands student queries using NLP and ML models
2. Recommends adaptive learning paths based on performance

The system integrates:
- Sentence embeddings (MiniLM)
- ML-based intent classification
- ML-based topic classification
- LLM-based intent refinement
- Policy-based adaptive recommendation engine
- Explainable AI outputs

---

## System Architecture

User Query  
→ Sentence Embedding  
→ Intent Classifier (ML)  
→ LLM Refinement  
→ Topic Classifier (ML)  
→ Difficulty Detection  
→ Performance-Based Recommendation Engine  
→ Explainable Output  

---

## Technologies Used

- Python
- Sentence-Transformers (MiniLM)
- Scikit-learn
- HuggingFace Transformers
- Logistic Regression
- Modular System Design

---

## Features

- Embedding-based semantic understanding
- Multi-class intent classification
- Topic classification
- Hybrid difficulty detection
- Adaptive learning path recommendation
- Explainable recommendations

---

## How to Run

1. Activate virtual environment:

venv\Scripts\activate

2. Run main system:

python src/main-system.py

---

## Assumptions

- Synthetic labeled dataset used
- Fixed topic progression path
- Policy-based adaptation logic

---

## Limitations

- Small synthetic dataset
- Lightweight LLM used
- No real-time student history storage

---

## Future Improvements

- Reinforcement learning-based adaptation
- Larger dataset
- Fine-tuned instruction LLM
- Student performance tracking
