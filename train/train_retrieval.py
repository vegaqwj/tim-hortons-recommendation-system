
import pandas as pd
import torch
from candidate_generation.two_tower_model import TwoTowerModel

ratings = pd.read_csv("data/ratings.csv")

users = ratings.user_id.unique()
items = ratings.item_id.unique()

user_map = {u:i for i,u in enumerate(users)}
item_map = {i:j for j,i in enumerate(items)}

model = TwoTowerModel(len(user_map), len(item_map))

print("Training demo complete (embedding model initialized).")
