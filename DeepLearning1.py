import torch

x = torch.rand((2,5))
x = x.view([1,10])

print(x)
