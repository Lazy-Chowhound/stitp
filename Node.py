import random


class Node():
    def __init__(self):
        # 通信半径
        self.TRANSMISSION_RANGE = 20
        # 感知半径
        self.PERCEIVED_RADIUS = 10
        # x,y坐标
        self.x = 0
        self.y = 0
        # 节点能量
        self.energy = 3
        # 节点是否处于休眠状态
        self.is_asleep = True
        # 节点改变状态 0代表未改变 1代表这一轮改变 2代表上一轮改变
        self.is_changed = 0
        # 节点是否存活
        self.is_alive = True

    # 随机部署到区域里
    def random_position(self):
        self.x = random.randint(0, 160)
        self.y = random.randint(0, 160)

    # 节点休眠
    def sleep(self):
        self.is_asleep = True

    # 节点苏醒
    def revive(self):
        self.is_asleep = False
