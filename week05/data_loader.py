import torch
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import random

num_inputs = 2
num_examples = 11
true_w = [2, -3.4]
true_b = 4.2
torch.manual_seed(100)
features = torch.randn(num_examples, num_inputs, dtype=torch.float32)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()), dtype=torch.float32)

print(features, '\n', labels)

batch_size = 3

array = features.data.numpy().T
np.savetxt('features.csv', array, fmt='%f', delimiter=',')

array = labels.data.numpy()
np.savetxt('labels.csv', array, fmt='%f', delimiter=',')


# 内外共享的变量名已经加了后缀
def data_iter(batch_size_in, features_in, labels_in):
    num_examples_in = len(features_in)
    indices = list(range(num_examples_in))
    random.shuffle(indices)  # 样本的读取顺序是随机的
    for i in range(0, num_examples_in, batch_size_in):
        j = torch.LongTensor(indices[i: min(i + batch_size_in, num_examples_in)])  # 最后一次可能不足一个batch
        yield features_in.index_select(0, j), labels_in.index_select(0, j)


for X, y in data_iter(batch_size, features, labels):
    print('开始执行一次for循环：')
    print(X, '\n', y)
    print('已经执行完成一次for循环！')

# # 关于透进函数
# # debug 也行，不过对于生手，这个更方便，可以摸索……
# 1、分清变量作用域，一种简单的思路即是直接“内外有别”：把重名变量加后缀。
# 2、对函数内变量进行赋值，下面是一种典型的方法：实现实参到“形参”的赋值
batch_size_in, features_in, labels_in = batch_size, features, labels
# 3、充分利用交互式执行的特点，单步执行函数内的命令：理解、评估代码的行为
num_examples_in = len(features_in)
indices = list(range(num_examples_in))  # 第一个关键点，不是直接操作数据，而是操作索引
random.shuffle(indices)  # 第二个关键点，索引乱序
print(indices)
# 4、遇到循环、判断等，进行人工操作
# 自行判断逻辑变量的值，进入相应的分支
# 计算循环变量，手动设定循环变量的值
list(range(0, num_examples_in, batch_size_in))  # 判断 i 怎么迭代
i = 0  # 进入循环体
# 下面一句不太好理解，我们画图
j = torch.LongTensor(indices[i: min(i + batch_size_in, num_examples_in)])
print(j)
print(features_in.index_select(0, j), labels_in.index_select(0, j))
print('我的循环变量是', i, '上面是 yeild 的值，我歇会儿！')
print(features_in)

i = 3  # 进入循环体
j = torch.LongTensor(indices[i: min(i + batch_size_in, num_examples_in)])
print(j)
print(features_in.index_select(0, j), labels_in.index_select(0, j))
print('我的循环变量是', i, '上面是 yeild 的值，我歇会儿！')
print(features_in)

i = 9  # 进入循环体
# 理解 min 其实他就壮实一点
# indices[i:  num_examples_in] 也行，但是 min 更壮实
j = torch.LongTensor(indices[i: min(i + batch_size_in, num_examples_in)])       # 防止索引越界
print(j)
print(features_in.index_select(0, j), labels_in.index_select(0, j))
print('我的循环变量是', i, '上面是 yeild 的值，我歇会儿！')
print(features_in)

# 5、仔细体会，如果自己写代码，可以先这样凑出来，然后打包
# 如果非常熟练了，可以直接打包，但前提仍然是你清楚的知道代码的每一个行为。
