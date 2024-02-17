import tarfile
import pickle
import io

# 打开tar.gz文件
with tarfile.open('train_dataset.tar.gz', 'r:gz') as tar:
   # 加载.pkl文件
   train_dataset = []
   for member in tar.getmembers():
       f = tar.extractfile(member)
       if f is not None:
           data = pickle.load(f)
           train_dataset.append(data)

print(len(train_dataset))

