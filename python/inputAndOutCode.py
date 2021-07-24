# 常用的输入

# 读取一个数据不读换行符
input()

# 读取一行数据 strip()去前后空格
list(map(int, input().strip().split()))
[int(i) for i in input().split()]  # strip()去前后空格

# 常用的输出
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))
