#!/usr/bin/env python
# coding: utf-8

# # 3.2 线性回归的从零开始实现

import torch
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import random

print(torch.__version__)


# ## 3.2.1 生成数据集
num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
torch.manual_seed(100)
features = torch.randn(num_examples, num_inputs,
                      dtype=torch.float32)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0, 1, size=labels.size()),
                       dtype=torch.float32)


print(features[0], labels[0])



def use_svg_display():
    # 用矢量图显示
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(8, 6)):
    use_svg_display()
    # 设置图的尺寸
    plt.rcParams['figure.figsize'] = figsize


set_figsize()
# plt.scatter(features[:, 1].numpy(), labels.numpy(), 1)
# plt.scatter(features[:, 0].numpy(), labels.numpy(), 1)
# plt.scatter(features[:, 0].numpy(), features[:, 1].numpy(), 1)


from mpl_toolkits.mplot3d import Axes3D  # 3D图表需要使用“mpl_toolkits”模块
print(Axes3D)

fig = plt.figure('3D scatter plot')
ax = fig.add_subplot(111, projection='3d')  # 3d图需要加projection='3d'
ax.scatter(features[:, 0].numpy(), features[:, 1], labels.numpy(), c='r', marker='.')  #上半部分为红色圆点

