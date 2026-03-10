
# Tim Hortons Recommendation System

Production-style recommendation system inspired by large-scale architectures used at Netflix, Amazon and TikTok.

This project implements a **two-stage recommendation pipeline**:

1. Candidate Retrieval (Two-Tower Model)
2. Ranking Model for Top-K recommendations

The system simulates how real-world recommendation systems operate in production ML environments.

---

# System Architecture

User Behavior Logs  
↓  
Feature Engineering Pipeline  
↓  
Two-Tower Retrieval Model  
↓  
Vector Similarity Search  
↓  
Candidate Generation (Top 100)  
↓  
Ranking Model  
↓  
Top-K Recommendations  
↓  
REST API Serving  

---

# Tech Stack

Python  
TensorFlow Recommenders  
Scikit-learn  
Flask  
Pandas / NumPy  

---

# Project Structure

tim-hortons-recommendation-system
│
├── data
├── feature_pipeline
│   └── build_features.py
├── models
│   ├── two_tower.py
│   └── ranking_model.py
├── train
│   └── train_retrieval.py
├── evaluation
│   └── metrics.py
├── serving
│   ├── vector_index.py
│   └── recommend.py
├── api
│   └── app.py
├── notebooks
│   └── EDA.ipynb
├── configs
│   └── config.yaml
└── README.md

---

# Model Design

## Two-Tower Retrieval

Two separate neural networks learn embeddings for:

- Users
- Products

User Tower → User Embedding  
Item Tower → Item Embedding  

Similarity(User, Item)

Top-K similar products are selected as candidate items.

---

# Ranking Model

A neural ranking model re-scores the candidates.

Input features:

- user features
- item features
- interaction features

Output:

ranking score

Top scoring items become final recommendations.

---

# Evaluation Metrics

Offline evaluation includes:

- Recall@K
- Precision@K
- NDCG@K

Example:

Recall@10 = 0.34

---

# API Example

Start API:

python api/app.py

Request:

http://localhost:5000/recommend?user_id=1

Response:

{
"user_id":1,
"recommendations":["Coffee","Ice Capp","Bagel"]
}

---

# Future Improvements

Possible production extensions:

- Spark feature engineering
- Databricks training pipeline
- FAISS vector search
- Real-time user events
- A/B testing

---

# Author

Weijia Qi  
Machine Learning & Data Engineer
