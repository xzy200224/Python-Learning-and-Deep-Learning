import torch
import torchvision
from PIL import Image
from torch import nn
from torchvision import transforms

image_path = "D:/VS Code/workspace/python_project/pytorch-tutorial-master/dataset/val/bees/6a00d8341c630a53ef00e553d0beb18834-800wi.jpg"
image = Image.open(image_path)
print(image)
image = image.convert('RGB')
# 创建transform
transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])

image = transform(image)
print(image.shape)

class My_model(nn.Module):
    def __init__(self):
        super(My_model, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=(3, 3), stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Dropout(0.25),
            nn.Flatten(),
            nn.Linear(57600, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 2),
            nn.Softmax(dim=1)
        )


    def forward(self, x):
        x = self.model(x)
        return x

model = torch.load("model_0.pth", map_location=torch.device('cpu'))
print(model)
image = torch.reshape(image, (1, 3, 256, 256))
model.eval()
with torch.no_grad():
    output = model(image)
print(output)

print(output.argmax())
