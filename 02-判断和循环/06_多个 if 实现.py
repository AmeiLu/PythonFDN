# 1. 定义 score 变量记录考试分数
score = int(input('请输入分数'))
# 2. 如果分数是 大于等于 90分 显示 优
if score >= 90:
    print('优')
# 3. 如果分数是 大于等于 80分 并且 小于 90分 显示 良
if (score >= 80) and score < 90:
    print('良')
# 4. 如果分数是 大于等于 70分 并且 小于 80分 显示 中
if (score >= 70) and score < 80:
    print('中')
# 5. 如果分数是 大于等于 60分 并且 小于 70分 显示 差
if (score >= 60) and score < 70:
    print('差')
# 6. 其它分数显示 不及格
if score < 60:
    print('不及格')


# 也可以全部都用if来写，全部if写法会每一个if都继续判断完；而if，elif结构只要有一个条件成立了，后面的就不判断了。