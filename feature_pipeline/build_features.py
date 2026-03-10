
import pandas as pd

ratings = pd.read_csv("data/ratings.csv")

user_features = ratings.groupby("user_id").size().reset_index(name="interaction_count")
item_features = ratings.groupby("item_id").size().reset_index(name="popularity")

print("User features:")
print(user_features)

print("Item features:")
print(item_features)
