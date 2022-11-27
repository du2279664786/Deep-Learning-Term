# # 来自https://blog.csdn.net/qq_27825451/article/details/96837905
# # 略有改动

import torch

# # 基本情况
a = torch.tensor([1, 2, 3.], requires_grad=True)
out = a.sigmoid()
print(out.requires_grad)
print(out)
print("----------------------------------------------")
out.sum().backward()  # 注意，这里只是函数，没说是 ”损失函数“
print(a.grad)
"""运行结果为：
True
tensor([0.7311, 0.8808, 0.9526], grad_fn=<SigmoidBackward0>)
----------------------------------------------
tensor([0.1966, 0.1050, 0.0452])
"""

# # data
a = torch.tensor([1, 2, 3.], requires_grad=True)
out = a.sigmoid()
c = out.data  # 需要走注意的是，通过.data “分离”得到的的变量会和原来的变量共用同样的数据，
# 而且新分离得到的张量是不可求导的，c发生了变化，原来的张量也会发生变化
# c.zero_()  # 改变c的值，原来的out也会改变 # 原blog的c 这样操作，似乎不如下面的更有说服力
c[:] = torch.tensor([4, 5, 6])  # 改变c的值，原来的out也会改变
print(c.requires_grad)
print(c)
print(out.requires_grad)
print(out)
print("----------------------------------------------")

out.sum().backward()  # 对原来的out求导，
print(a.grad)  # 不会报错，但是结果却并不正确 (似乎是 a * (1 - a) 不能正常使用)
'''运行结果为：
False
tensor([4., 5., 6.])
True
tensor([4., 5., 6.], grad_fn=<SigmoidBackward0>)
----------------------------------------------
tensor([-12., -20., -30.])
'''

# # detach
a = torch.tensor([1, 2, 3.], requires_grad=True)
out = a.sigmoid()
c = out.detach()  # 需要注意的是，通过.detach() “分离”得到的的变量会和原来的变量共用同样的数据，
# 而且新分离得到的张量是不可求导的，c发生了变化，原来的张量也会发生变化
c[:] = torch.tensor([4, 5, 6])  # 改变c的值，原来的out也会改变
print(c.requires_grad)
print(c)
print(out.requires_grad)
print(out)
print("----------------------------------------------")

out.sum().backward()  # 对原来的out求导，
print(a.grad)  # 此时会报错，错误结果参考下面,显示梯度计算所需要的张量已经被“原位操作inplace”所更改了。
'''
False
tensor([4., 5., 6.])
True
tensor([4., 5., 6.], grad_fn=<SigmoidBackward0>)
----------------------------------------------
RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation
'''

