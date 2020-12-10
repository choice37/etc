import torch
import torch.nn as nn
import torch.nn.functional as F
from random import *

class net(nn.Module):
  def __init__(self):
    super(net, self).__init__()
    self.fc1 = nn.Linear(1, 128)
    self.fc2 = nn.Linear(128, 128)
    self.fc3 = nn.Linear(128, 1)

  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)#F.relu(self.fc3(x))
    return x #self.fc3(self.fc2(self.fc1(x)))


criterion = torch.nn.MSELoss()
m = net()
optimizer = torch.optim.Adam(m.parameters(), lr=0.0001)

print("start!")
for i in range(10000):
  loss = 0
  #for j in range(16):
  x = torch.tensor([float(randint(1, 1000))])
  y = m(x)
  t = x * 4 - 3

  loss += criterion(y, t)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

while 1:
  optimizer.zero_grad()
  x = torch.tensor([float(input('입력을 넣으시오'))])
  y = m(x)
  t = x * 4 - 3
  print("x:%s, y:%s, t:%s"%(x, y, t))

  loss = criterion(y, t)
  loss.backward()
  optimizer.step()

