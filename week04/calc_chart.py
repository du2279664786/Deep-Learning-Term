import torch

w = torch.Tensor([1, 2])
w.requires_grad = True

x = torch.Tensor([3, 4])
y = torch.Tensor([100])

a = w @ x
b = a - y

z = b ** 2

print('z', z)

print('w.grad before backward', w.grad)
b.retain_grad()
z.backward()
print('w.grad after backward', w.grad)
print()

for ts in ['w', 'x', 'y', 'a', 'b', 'z']:
    print(ts, '关键指标')
    for mt in ['.is_leaf', '.requires_grad', '.grad', '.grad_fn']:
        print(ts + mt + ':', eval(ts + mt))
    print()
