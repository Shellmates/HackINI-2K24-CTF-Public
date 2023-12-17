import torch
import torch.nn as nn
import pickle


def process_sentence(sentence):
    return [ord(char) for char in sentence]


class MyModel(nn.Module):
    def __init__(self,):
        super(MyModel, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(50, 512), nn.ReLU(),
            nn.Linear(512, 50),
        )

    def forward(self, x):
        return self.model(x)
    

model = MyModel()
model.load_state_dict(torch.load('hacked_model.pt'))