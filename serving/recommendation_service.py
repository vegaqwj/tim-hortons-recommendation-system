
import pandas as pd

items = pd.read_csv("data/items.csv")

def recommend(user_id, k=5):

    return items.head(k).to_dict(orient="records")
