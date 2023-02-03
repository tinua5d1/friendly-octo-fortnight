import random
# 本期up
up = "夜兰"

g = []
# 可能歪的角色
w = ["迪卢克","七七","提纳里","琴","刻晴","莫娜"]

sw = 0

num_ =0
num = 0
w_ = 0
oe = []
# 概率(千分之几)
gl = 8
# up概率(千分之几)
upgl = 4
# 生成一个用于随机的列表
for i in range(1000-gl):
        oe.append('1')
for i in range(int(gl-upgl)):
        oe.append("2")
for i in range(int(upgl)):
        oe.append("3")
# 抽奖主程序
def oen(num):
    if num == 89:
        return random.choice(["2","3"])
    if num == 179:
        return "3"
    coe = random.choice(oe)
    if coe == "2" and 90<=num:
        coe = "3"
    return coe
    