# Technical Documentation
AI-Powered Teaching Assistant System

---

## 1. Problem Statement

The objective of this project is to build an AI-powered teaching assistant capable of:

1. Understanding student queries using Natural Language Processing techniques.
2. Recommending adaptive learning paths based on student performance metrics.

The system simulates an EdTech platform that dynamically adjusts learning recommendations based on student interaction history, quiz performance, and difficulty levels.

---

## 2. System Objectives

The system is designed to:

- Classify student queries into predefined intent categories.
- Identify the academic topic associated with the query.
- Determine the difficulty level of the query.
- Refine intent predictions using a lightweight Large Language Model (LLM).
- Provide adaptive learning path recommendations.
- Generate explainable outputs for transparency.
---

## 3. System Architecture

The system is designed in a modular architecture separating Machine Learning components from LLM components.

### 3.1 High-Level Flow

User Query  
→ Sentence Embedding Generation  
→ Intent Classification (ML Model)  
→ Topic Classification (ML Model)  
→ LLM-Based Intent Refinement  
→ Difficulty Detection  
→ Performance-Based Recommendation Engine  
→ Explainable Output  

---

## 4. ML vs LLM Separation

The system intentionally separates classical Machine Learning from Large Language Model refinement.

### 4.1 Machine Learning Components

The ML layer handles:

- Sentence embeddings using MiniLM (Sentence-Transformers)
- Intent classification using Logistic Regression
- Topic classification using Logistic Regression
- Model persistence using pickle

These components are deterministic and optimized for structured classification tasks.

---

### 4.2 LLM Component

A lightweight transformer model (DistilGPT2) is used to:

- Refine predicted intent
- Validate classification output
- Simulate intelligent reasoning

The LLM operates after ML prediction and acts as a semantic refinement layer.

This hybrid approach ensures:

- Stability from ML models
- Contextual reasoning from LLM
- Reduced over-reliance on generative output
---

## 5. Dataset Strategy

No labeled dataset was provided as part of the assessment.

Therefore, a synthetic labeled dataset was generated to train the intent and topic classifiers.

The dataset includes:

- Student queries written in natural language
- Manually assigned intent labels
- Manually assigned topic labels
- Difficulty level categorization

The dataset contains balanced samples across:

Intent Categories:
- Explanation
- Example
- Doubt
- Revision

Topic Categories:
- Regression
- Classification
- Optimization
- Neural Networks
- CNN
- Regularization

---

## 6. Synthetic Data Generation Methodology

The synthetic dataset was generated based on:

- Common machine learning student questions
- Variations in phrasing
- Concept-level difficulty differences
- Realistic academic terminology

Queries were designed to simulate:

- Beginner-level conceptual confusion
- Intermediate-level conceptual clarification
- Advanced-level mathematical reasoning

The dataset size was intentionally kept below 50MB as per assessment constraints.

---

## 7. Assumptions

- Student queries follow academic terminology.
- Performance metrics (score, attempts, time) are reliable indicators of learning progress.
- Topic progression follows a predefined structured learning path.
- LLM refinement is used for semantic validation, not full decision making.
`---

## 8. Adaptive Learning Path Recommendation

The system includes a rule-based adaptive recommendation engine that simulates basic policy-driven personalization.

### 8.1 Input Parameters

The recommendation engine considers:

- Quiz score
- Number of attempts
- Time spent on topic
- Current topic

---

### 8.2 Policy Logic

The adaptation policy is based on score thresholds:

If score < 50:
- Action: Revision
- Difficulty: Decrease
- Next Topic: Same topic

If 50 ≤ score < 75:
- Action: Practice
- Difficulty: Same
- Next Topic: Same topic

If score ≥ 75:
- Action: Advance
- Difficulty: Increase
- Next Topic: Move to next topic in predefined learning path

---

### 8.3 Topic Progression

The system follows a structured learning graph:

Regression  
→ Optimization  
→ Neural Networks  
→ CNN  

This ensures logical academic progression.

---

### 8.4 Explainability

Each recommendation includes a reasoning string explaining:

- Why the action was chosen
- Which threshold triggered the decision
- Whether the student should revise, practice, or advance

This improves transparency and trustworthiness.
---

## 8. Adaptive Learning Path Recommendation

The system includes a rule-based adaptive recommendation engine that simulates basic policy-driven personalization.

### 8.1 Input Parameters

The recommendation engine considers:

- Quiz score
- Number of attempts
- Time spent on topic
- Current topic

---

### 8.2 Policy Logic

The adaptation policy is based on score thresholds:

If score < 50:
- Action: Revision
- Difficulty: Decrease
- Next Topic: Same topic

If 50 ≤ score < 75:
- Action: Practice
- Difficulty: Same
- Next Topic: Same topic

If score ≥ 75:
- Action: Advance
- Difficulty: Increase
- Next Topic: Move to next topic in predefined learning path

---

### 8.3 Topic Progression

The system follows a structured learning graph:

Regression  
→ Optimization  
→ Neural Networks  
→ CNN  

This ensures logical academic progression.

---

### 8.4 Explainability

Each recommendation includes a reasoning string explaining:

- Why the action was chosen
- Which threshold triggered the decision
- Whether the student should revise, practice, or advance

This improves transparency and trustworthiness.
---

## 9. Model Architecture and Technical Details

### 9.1 Sentence Embeddings

The system uses the "all-MiniLM-L6-v2" model from Sentence-Transformers.

Reason for selection:
- Lightweight and efficient
- Produces dense semantic embeddings
- Captures contextual similarity better than TF-IDF
- Suitable for small datasets

Each student query is converted into a dense vector representation before classification.

---

### 9.2 Intent Classification Model

A Logistic Regression classifier is trained on the generated embeddings.

Reasons for choosing Logistic Regression:

- Interpretable and stable
- Suitable for multi-class classification
- Performs well on embedding-based features
- Avoids overfitting on small datasets

The classifier predicts one of:
- Explanation
- Example
- Doubt
- Revision

---

### 9.3 Topic Classification Model

A second Logistic Regression model is trained independently to classify topics.

This separation ensures:
- Modular architecture
- Reduced model complexity
- Clear task-specific learning

---

### 9.4 Model Persistence

Trained models are saved using pickle.

This allows:
- Fast inference
- No retraining required during runtime
- Modular deployment design

---

### 9.5 LLM Refinement Layer

After ML-based intent prediction, a lightweight transformer model (DistilGPT2) is used to:

- Validate the predicted intent
- Refine semantic understanding
- Simulate intelligent reasoning

This hybrid architecture balances structured ML prediction with contextual LLM reasoning.
---

## 10. Limitations

While the system demonstrates hybrid ML and LLM integration, the following limitations exist:

1. The dataset is synthetic and limited in size.
2. The LLM used (DistilGPT2) is not instruction-tuned.
3. Recommendation logic is threshold-based and not true reinforcement learning.
4. No persistent student profile storage across sessions.
5. Topic progression graph is predefined and static.

---

## 11. Future Improvements

Future enhancements could include:

1. Expanding dataset with real student interaction data.
2. Fine-tuning an instruction-tuned LLM for better refinement.
3. Implementing reinforcement learning for dynamic policy updates.
4. Adding a student knowledge tracing model.
5. Integrating a database to store historical student performance.
6. Deploying the system as a web-based application.

---

## 12. Conclusion

This project demonstrates a modular AI system integrating:

- Sentence embeddings
- Classical machine learning
- Lightweight LLM refinement
- Adaptive personalization logic
- Explainable decision making

The hybrid architecture ensures stability, interpretability, and contextual reasoning while remaining computationally efficient.
---

## 13. Justification for Synthetic Dataset Usage

While public datasets such as SQuAD, SciQ, and ARC were available, they do not provide structured labels aligned with the required task dimensions:

- Intent classification (Explanation, Example, Doubt, Revision)
- Topic classification (Regression, CNN, Optimization, etc.)
- Difficulty level categorization

Since the assessment explicitly requires structured intent and topic prediction, a task-specific labeled dataset was necessary.

Therefore, a synthetic dataset was generated with carefully designed student-style queries mapped to predefined categories.

This approach ensured:

1. Direct alignment with problem requirements.
2. Balanced representation across intent and topic classes.
3. Controlled dataset size (<50MB as required).
4. Clear explainability of label logic.

Additionally, the use of pretrained sentence embeddings (MiniLM) enables semantic generalization beyond exact training examples. This allows the system to handle unseen but semantically similar queries within the machine learning domain.

This design choice prioritizes architectural clarity and task alignment over dataset scale.

