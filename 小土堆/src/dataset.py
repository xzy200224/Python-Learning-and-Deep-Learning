import pickle
import tarfile

from torch.utils.data import Dataset
from PIL import Image
import os
from torchvision import transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch
from torch.utils.tensorboard import SummaryWriter

# tensorboard记录
# writer = SummaryWriter("logs")

# label即文件夹名
class TestData(Dataset):

    def __init__(self, root_dir, label_dir, transform):
        self.root_dir = root_dir
        self.label_dir = label_dir
        # 拼接路径
        self.path = os.path.join(self.root_dir, self.label_dir)
        # 数据列表
        self.image_list = os.listdir(self.path)
        self.transform = transform

    def __getitem__(self, idx):
        img_name = self.image_list[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        dict = {"ants": 0, "bees": 1}
        if self.label_dir in dict:
            label = dict[self.label_dir]
        else:
            raise ValueError("Invalid label: {}".format(self.label_dir))
            
        # transform
        if self.transform:
            img = self.transform(img)

        # 将标签转为one-hot编码
        label_one_hot = F.one_hot(torch.tensor(label), num_classes=len(dict)).float()
        
        sample = {'img': img, 'label': label_one_hot}
        return sample

    def __len__(self):
        assert len(self.image_list) > 0
        return len(self.image_list)

# label单独一个文件夹用文件存储
class TrainData(Dataset):
    def __init__(self, root_dir, image_dir, label_dir, transform):
        self.root_dir = root_dir
        self.image_dir = image_dir
        self.label_dir = label_dir
        # 拼接路径
        self.label_path = os.path.join(self.root_dir, self.label_dir)
        self.image_path = os.path.join(self.root_dir, self.image_dir)
        # 数据列表
        self.image_list = os.listdir(self.image_path)
        self.label_list = os.listdir(self.label_path)
        self.transform = transform
        # 因为label 和 Image文件名相同，进行一样的排序，可以保证取出的数据和label是一一对应的
        self.image_list.sort()
        self.label_list.sort()

    def __getitem__(self, idx):
        img_name = self.image_list[idx]
        label_name = self.label_list[idx]
        img_item_path = os.path.join(self.root_dir, self.image_dir, img_name)
        label_item_path = os.path.join(self.root_dir, self.label_dir, label_name)
        img = Image.open(img_item_path)
        dict = {"ants": 0, "bees": 1}

        with open(label_item_path, 'r') as f:
            label = f.readline().strip()  # 去除换行符
            # 如果label在字典中存在，则将其转换为对应的值；如果label不在字典中，则会引发ValueError异常
            if label in dict:
                label = dict[label]
            else:
                raise ValueError("Invalid label: {}".format(label))

        # transform
        if self.transform:
            img = self.transform(img)

        # 将标签转为one-hot编码
        label_one_hot = F.one_hot(torch.tensor(label), num_classes=len(dict)).float()
        
        sample = {'img': img, 'label': label_one_hot, 'img_name': img_name}
        # sample = {'img': img, 'label': label_one_hot}
        return sample

    def __len__(self):
        assert len(self.image_list) == len(self.label_list)
        return len(self.image_list)

if __name__ == '__main__':
    # 创建transform
    transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
    # 写入dataset路径
    root_dir = "D:/VS Code/workspace/python_project/pytorch-tutorial-master/dataset/train"
    image_ants = "ants_image"
    label_ants = "ants_label"
    ants_dataset = TrainData(root_dir, image_ants, label_ants, transform)
    image_bees = "bees_image"
    label_bees = "bees_label"
    bees_dataset = TrainData(root_dir, image_bees, label_bees, transform)
    # 合并数据集
    train_dataset = ants_dataset + bees_dataset

    # 将字典保存为文件
    with open('train_dataset.pkl', 'wb') as f:
        pickle.dump(train_dataset, f)

    # 创建一个tarfile对象
    with tarfile.open('train_dataset.tar.gz', 'w:gz') as tar:
        # 将文件添加到tarfile
        tar.add('train_dataset.pkl')

    # # # 打包
    # # 将数据集的每个元素保存为一个.pkl文件
    # for i, sample in enumerate(train_dataset):
    #     with open(f'sample_{i}.pkl', 'wb') as f:
    #         pickle.dump(sample, f)
    #
    # # 将.pkl文件打包成一个tar.gz文件
    # with tarfile.open('train_dataset.tar.gz', 'w:gz') as tar:
    #     for i in range(len(train_dataset)):
    #         tar.add(f'sample_{i}.pkl')

    # 输出查看结果
    # print(len(train_dataset))
    # print(train_dataset[23], train_dataset[23]['img'].shape, train_dataset[23]['img_name'])

    # tensorboard加入图片
    # writer.add_image('图片', train_dataset[0]['img'])
    # writer.close()

    
    # 检查图片是否有误
    # train_dataloader = DataLoader(train_dataset, batch_size=1)
    # for i, data in enumerate(train_dataloader):
    #     imgs = data["img"]
    #     img_name = data["img_name"]  # 获取图像文件名
    #     if imgs.shape == (1, 1, 256, 256):
    #         print(img_name)  # 打印图像文件名
    #         print("找到序号：", i)
    #         break
    
    # 检查图片是否有误
    # train_dataloader = DataLoader(train_dataset, batch_size=1)
    # for data in train_dataloader:
    #     label = data["label"]
    #     print(label,label.dtype) 





