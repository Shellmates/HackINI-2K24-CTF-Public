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


with open('data', 'br') as file:
    data = pickle.load(file)


for p in model.parameters():
    p.data = torch.fmod(p.data, 100)



sentence = data[69] # Write the flag
tokens = process_sentence(sentence)
x = torch.zeros((50,))
x[:len(tokens)] = torch.tensor(tokens)

out =  model(x)
ascii = torch.round(torch.clamp_min(out, 0)).long().tolist()

print('Print the flag:', ''.join((map(chr, ascii))))
