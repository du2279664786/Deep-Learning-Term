import torch
from torch import nn


class LinearNet(nn.Module):  # nn.Module是父类
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature, 1)

    # forward 定义前向传播
    def forward(self, x):
        y = self.linear(x)
        return y


# 类与对象：类的实例化
net = LinearNet(2)  # 类是一个“架子”， net是LinearNet的一个实例
# 本质上是调用了__init__()


x = torch.zeros(2)
net(x)


# () call的理解
# 一个对象后面能加 () 是因为类里面有 __call__() 函数
# 也就是callable
callable(0)
callable("runoob")


def add(a, b):
    return a + b


callable(add)  # 函数返回 True


class A:  # 类
    def method(self):
        return 0


callable(A)  # 类返回 True

a = A()
callable(a)  # 没有实现 __call__, 返回 False


class B:
    def __call__(self):
        return 0


callable(B)

b = B()
callable(b)  # 实现 __call__, 返回 True
b()


# nn.Module 把__call__ 指向了 forward
# ctrl + B 跟踪
# 通过structure深入查找
