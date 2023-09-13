# 设计一个函数用于获取两个数中的较大数，数据来自于函数的参数
def get_max(a, b):
    if a > b:
        return a
    else:
        return b
    print('这里的print会执行吗, 并不会执行')


# 调用
num = get_max(60, 20)
print(num)

