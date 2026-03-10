
import torch
import torch.nn as nn

class TwoTowerModel(nn.Module):

    def __init__(self, num_users, num_items, embed_dim=32):
        super().__init__()
        self.user_embedding = nn.Embedding(num_users, embed_dim)
        self.item_embedding = nn.Embedding(num_items, embed_dim)

    def forward(self, user_ids, item_ids):
        u = self.user_embedding(user_ids)
        i = self.item_embedding(item_ids)
        return (u * i).sum(dim=1)
