def login(username, password, code):
    print(username,  password, code, '33333')
    if code == '6666':
        if username == 'admin' and password == '123456':
            print('登录成功')
        else:
            print('用户名或密码错误')
    else:
        print('验证码错误')