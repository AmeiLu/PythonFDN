# 1. 提示用户输入用户姓名，并保存到变量中
name = input('请输入姓名:')
# 2. 提示用户输入用户年龄，保存到变量中，并转换成整数
age = int(input('请输入年龄:'))
# 3. 提示用户输入用户身高，保存到变量中，并转换成浮点数
height = float(input('请输入身高:'))
# 4. 在控制台输出用户姓名、年龄、身高对应变量的数据类型
print(type(name), type(age), type(height))
# 5. 按照以下格式输出用户信息:“姓名:xxx 年龄:xxx 身高:xxx”
print(f"姓名:{name} 年龄:{age} 身高:{height}")
# 6. 在控制台输出该用户5年之后的年龄，格式:“张三 5 年之后的年龄是 25”
age = age + 5
print(f"{name} 5 年之后的年龄是 {age}")
# 7. 在控制台输出该用户现在是否成年，格式:“张三是否成年:True”
print(f"{name}是否成年:{age >= 18}")
