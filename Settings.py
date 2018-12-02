import math

# 节点个数
node_count = 1500
# 节点密度保持在50
scope = round(math.sqrt(node_count * 50))
# 区域范围
WIDTH = 300
# 邻近区域系数
a = 0.7
# 活跃系数
P = 0.5
Eelec = 0.0000005
Eamp = 0.0000000001
# 工作功率 电压3V 工作电流10mA
p1 = 0.03
# 休眠功率 电压3V 休眠电流2uA
p2 = 0.000006


def set_a(_a):
    global a
    a = _a


def set_P(_P):
    global P
    P = _P
