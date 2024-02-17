from torch.utils.tensorboard import SummaryWriter
from dataset import TrainData, TestData
from model import *
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms

# 定义训练的设备
device = torch.device("cuda")
# 创建transform
transform = transforms.Compose([transforms.Resize((256, 256)), transforms.RandomHorizontalFlip(), transforms.RandomVerticalFlip(),transforms.ToTensor()])
# 准备训练数据集
train_dir = "D:/VS Code/workspace/python_project/pytorch-tutorial-master/dataset/train"
image_ants = "ants_image"
label_ants = "ants_label"
ants_dataset = TrainData(train_dir, image_ants, label_ants, transform)
image_bees = "bees_image"
label_bees = "bees_label"
bees_dataset = TrainData(train_dir, image_bees, label_bees, transform)
train_data = ants_dataset + bees_dataset
# 准备测试数据集
val_dir = "D:/VS Code/workspace/python_project/pytorch-tutorial-master/dataset/val"
image_ants = "ants"
image_bees = "bees"
test_ants_dataset = TestData(val_dir, image_ants, transform)
test_bees_dataset = TestData(val_dir, image_bees, transform)
test_data = test_ants_dataset + test_bees_dataset


# length 长度
train_data_size = len(train_data)
test_data_size = len(test_data)
# 如果train_data_size=10, 训练数据集的长度为：10
print("训练数据集的长度为：{}".format(train_data_size))
print("测试数据集的长度为：{}".format(test_data_size))

# 利用 DataLoader 来加载数据集
train_dataloader = DataLoader(train_data, batch_size=16)
test_dataloader = DataLoader(test_data, batch_size=16)

# 创建网络模型
model = My_model().to(device)

# 损失函数
loss_fn = nn.CrossEntropyLoss().to(device)

# 优化器(学习率，权重衰减)
learning_rate = 0.001
weight_decay = 0.0001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)

# 设置训练网络的一些参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 500

# 添加tensorboard
writer = SummaryWriter("logs")

for i in range(epoch):
    print("-------第 {} 轮训练开始-------".format(i+1))

    # 训练步骤开始
    model.train()
    for data in train_dataloader:
        imgs = data["img"].to(device)
        targets = data["label"].to(device)
        outputs = model(imgs)
        loss = loss_fn(outputs, targets)
        # 优化器优化模型
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step = total_train_step + 1
        if total_train_step % 20 == 0:
            print("训练次数：{}, Loss: {}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    # 测试步骤开始
    model.eval()
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs = data["img"].to(device)
            targets = data["label"].to(device)
            outputs = model(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss = total_test_loss + loss.item()
            # 将概率转换为类别标签
            predicted_labels = outputs.argmax(dim=1)
            targets_labels = targets.argmax(dim=1)
            # 计算准确率
            accuracy = (predicted_labels == targets_labels).sum()
            total_accuracy = total_accuracy + accuracy

    print("整体测试集上的Loss: {}".format(total_test_loss))
    print("整体测试集上的正确率: {}".format(total_accuracy/test_data_size))
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy/test_data_size, total_test_step)
    total_test_step = total_test_step + 1
    if i % 50 == 0:
        torch.save(model, "model_{}.pth".format(i))
        print("模型已保存")

writer.close()
