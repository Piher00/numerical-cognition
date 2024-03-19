import torch
import torchvision

#torch.dataset = torchvision.datasets.MNIST('path/to/root/', train=True, download=False)

x = torch.randn(1,2,3).to('cuda')
print(x)
print(x+1)
