
# Recommendation System Architecture

User Logs
    ↓
Feature Engineering
    ↓
Two-Tower Retrieval Model
    ↓
Vector Similarity Search
    ↓
Candidate Items
    ↓
Ranking Model
    ↓
Top-K Recommendations
    ↓
API Serving


ASCII Architecture Diagram

           User Behavior Logs
                    │
                    ▼
         Feature Engineering Pipeline
                    │
                    ▼
           Two Tower Retrieval
         (User & Item Embeddings)
                    │
                    ▼
             Vector Search
                    │
                    ▼
         Candidate Items (Top 100)
                    │
                    ▼
              Ranking Model
                    │
                    ▼
           Top-K Recommendations
                    │
                    ▼
                 REST API
