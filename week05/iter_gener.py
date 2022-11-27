# 这个叫函数
def fun(x):
    for ii in range(x):
        return ii


type(fun(5))
type(fun)


# 这个叫生成器
def gen(x):
    for ii in range(x):
        yield ii


type(gen(5))

gen1 = gen(6)
next(gen1)

for ii in gen1:
    print(ii)


# 这个是可迭代，但不是一个迭代器
ll = [0, 1, 2, 3, 4]
next(ll)  # TypeError: 'list' object is not an iterator
for ii in ll:
    print(ii)
# 可以这样变成迭代器
ll_iter = iter(ll)
next(ll_iter)

# 总结：
# 有yield的函数是生成器
# 能next()的是迭代器
# 能用在 for _ in xxxx 的叫可迭代
# 可迭代概念范围最大，生成器和迭代器肯定都可迭代，但可迭代不一定都是迭代器和生成器
# 内置的集合类是可迭代，但不是迭代器
# 生成器一定是迭代器
# 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器，然后对获取到的迭代器不断调用next()方法
# https://www.runoob.com/python3/python3-iterator-generator.html
# https://www.cnblogs.com/jiba/p/14047159.html

# 参考信息
# 迭代器与可迭代
ll = [1, 2, 3, 4, 5]
print(2 in ll)
print(3 in ll)
print(2 in ll)
print(3 in ll)

ll = iter([1, 2, 3, 4, 5])
print(2 in ll)
print(3 in ll)

ll = iter([1, 2, 3, 4, 5])
print(3 in ll)
print(2 in ll)

ll = iter([1, 2, 3, 4, 5])
print(9 in ll)
print(2 in ll)

it = gen(5)
print(2 in it)
print(3 in it)

it = gen(5)
print(3 in it)
print(2 in it)
