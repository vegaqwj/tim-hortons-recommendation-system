
import torch
import torch.nn as nn

class RankingModel(nn.Module):

    def __init__(self, embed_dim=32):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(embed_dim*2,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,1)
        )

    def forward(self,u,i):

        x = torch.cat([u,i],dim=1)

        return self.network(x).squeeze()
