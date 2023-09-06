import random

count = 0

while True:
    # 1. 控制台出拳(石头1/剪刀2/布3)
    player = int(input('请出拳 石头1/剪刀2/布3/退出0/结束4:'))
    # print(0==4)  
    if player == 0:
        print('重新开始游戏')
        continue  # 0结束本次循环,继续下一次循环
    elif player == 4:
        print('欢迎下次游戏')
        break  # 4结束循环
    elif player > 4:
        print('你输入的有误,请重新输入')
        continue
    # 2. 电脑出拳 computer = 电脑的结果
    computer = random.randint(1, 3)
    # 3. 判断胜负
    # 3.1 玩家胜利
    # 3.1.1 玩家出1石头, 电脑出2剪刀        # 3.1.2 玩家出2剪刀, 电脑出3布      # 3.1.3 玩家出3布, 电脑出1石头
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        count += 1  # 胜利一次,加 1
        print('玩家胜利')
        if count == 3:  #玩家胜利3次结束循环
            break  
    # 3.2 平局  玩家和电脑出的内容一样,
    elif player == computer:
        print('平局')
    # 3.3 电脑胜利
    else:
        print('电脑胜利')
