import math
# 节点个数
node_count = 1500
# 节点密度保持在50
scope = round(math.sqrt(node_count * 50))
# 区域范围
WIDTH = 300
# 邻近区域系数
a = 0.9
# 活跃系数
P = 0.9
Eelec = 0.0000005
Eamp = 0.0000000001
# 工作功率
p1 = 0.04
# 休眠功率
p2 = 0.015