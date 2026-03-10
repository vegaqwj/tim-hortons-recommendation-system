
# Tim Hortons Recommendation System (FAANG-style)

This project implements a production-style recommendation system inspired by architectures used at companies like Netflix, Amazon, and TikTok.

Architecture:

User Logs
 → Feature Engineering
 → Two-Tower Retrieval Model
 → Vector Search
 → Ranking Model
 → Top-K Recommendations
 → REST API

Key Features

- Two-tower retrieval model
- Ranking neural network
- Vector similarity search
- Feature engineering pipeline
- Offline evaluation metrics (Recall@K)
- REST API for real-time recommendation

Run pipeline

1 Install dependencies

pip install -r requirements.txt

2 Train retrieval model

python train/train_retrieval.py

3 Start API

python api/app.py

Example

http://localhost:5000/recommend?user_id=1
