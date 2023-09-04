# 导包(放在最上方)
import random

# 1. 控制台出拳(石头1/剪刀2/布3)
player = int(input('请出拳 石头1/剪刀2/布3:'))
# 2. 电脑出拳 computer = 电脑的结果。 产生 随机数
computer = random.randint(1, 3)
# 3. 判断胜负
# 3.1 玩家胜利
# 3.1.1 玩家出石头1, 电脑出剪刀2；          
# 3.1.2 玩家出剪刀2, 电脑出 布3；      
# 3.1.3 玩家出布3, 电脑出 石头1。 \续行符，看着多行，但代码只有一行
if (player == 1 and computer == 2) or \
    (player == 2 and computer == 3) or \
    (player == 3 and computer == 1):
    print('玩家胜利')
# 3.2 平局  玩家和电脑出的内容一样,
elif player == computer:
    print('平局')
# 3.3 电脑胜利
else:
    print('电脑胜利')
