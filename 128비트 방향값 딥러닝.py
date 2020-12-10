import torch
import torch.nn as nn
import torch.nn.functional as F
from random import *
import numpy as np

class net(nn.Module):
  def __init__(self):
    super(net, self).__init__()
    self.fc1 = nn.Linear(128, 64)
    self.fc2 = nn.Linear(64, 64)
    self.fc3 = nn.Linear(64, 2)

  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)#F.relu(self.fc3(x))
    return x #self.fc3(self.fc2(self.fc1(x)))


def angle_feature(heading, elevation):
    import math
    # twopi = math.pi * 2
    # heading = (heading + twopi) % twopi     # From 0 ~ 2pi
    # It will be the same
    return np.array([math.sin(heading), math.cos(heading),
                     math.sin(elevation), math.cos(elevation)] * (128 // 4),
                    dtype=np.float32)
    
criterion = torch.nn.MSELoss()
m = net()
optimizer = torch.optim.Adam(m.parameters(), lr=0.0001)

print("start!")
for i in range(10000):
  loss = 0
  #for j in range(16):
  x = float(randint(1, 6280)) / 1000
  y = float(randint(-1, 1)) * 0.523  # float(randint(-523, 523)) / 1000
  heading = torch.tensor([x])
  elevation = torch.tensor([y])
  angle = torch.from_numpy(angle_feature(heading, elevation))
  #print(angle)
  a = m(angle)
  #print(a)
  t = torch.tensor([x, y])
  '''y = m(x)
  t = x * 4 - 3'''
  #print(t)

  loss += criterion(a, t)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

while 1:
  optimizer.zero_grad()
  x = torch.tensor([float(input('입력을 넣으시오'))])
  y = torch.tensor([float(input('입력을 넣으시오'))])
  heading = torch.tensor([x])
  elevation = torch.tensor([y])
  angle = torch.from_numpy(angle_feature(heading, elevation))
  a = m(angle)
  t = torch.tensor([x, y])
  #t = x * 4 - 3
  print("a:%s, t:%s"%(a, t))

  loss = criterion(a, t)
  loss.backward()
  optimizer.step()

