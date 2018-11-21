import random
import math
import Settings


def find_distance(node1, node2):
    """
    求两节点间的距离
    :param node1:
    :param node2:
    :return: 距离（保留两位小数）
    """
    result = math.sqrt((node2.x - node1.x) * (node2.x - node1.x) + (node2.y - node1.y) * (node2.y - node1.y))
    # 通信消耗能量
    energy = 240 * Settings.Eelec + Settings.Eamp * 240 * result * result + Settings.Eelec * 240
    node1.energy = node1.energy - energy
    node2.energy = node2.energy - energy
    return round(result, 2)


def judge_close(node1, node2):
    """
    判断node2是否在node1的邻近区域
    :param node1:
    :param node2:
    :return:
    """
    distance = find_distance(node1, node2)
    scope = Settings.a * node1.PERCEIVED_RADIUS
    if distance <= scope:
        return True
    else:
        return False


def choose_sleep(node):
    """
    判断节点是继续休眠还是苏醒
    :param node:
    :return:
    """
    status = node.is_asleep
    coef = random.randint(1, 10)
    # 节点苏醒
    if coef <= Settings.P * 10:
        node.revive()
    # 节点休眠
    elif coef > Settings.P * 10:
        node.sleep()
    if node.is_asleep != status:
        node.is_changed = 1


def get_close_nodes(node, sensor):
    """
    获取节点邻近区域内的所有节点
    :param node:
    :param sensor:
    :return: 节点列表
    """
    node_list = []
    for node2 in sensor:
        if judge_close(node, node2):
            node_list.append(node2)
    return node_list


def get_active_nodes(node, sensor):
    """
    获取某个节点邻近区域内所有处于活跃状态的结点
    :param node:
    :param sensor:
    :return:节点列表
    """
    active_node_list = get_close_nodes(node, sensor)
    for node in active_node_list:
        if node.is_asleep:
            active_node_list.remove(node)
    return active_node_list


def get_all_sleeping_nodes(sensor):
    """
    获取当前所有处于休眠中的节点
    :param sensor:
    :return:节点列表
    """
    sleep_nodes = []
    for node in sensor:
        if node.is_asleep:
            sleep_nodes.append(node)
            node.energy = node.energy - Settings.Eelec * 240
    return sleep_nodes


def get_unchanged_active_nodes(active_nodes):
    """
    获取节点邻近区域内上一轮没有改变状态的活跃节点
    :param active_nodes:某个节点周围的活跃节点
    :return:
    """
    unchanged_active_nodes = []
    for node in active_nodes:
        if node.is_changed == 0:
            unchanged_active_nodes.append(node)
    return unchanged_active_nodes


def random_select(unchanged_active_nodes):
    """
    从节点邻近区域内随机选择一个上轮没有改变过状态的活跃节点使其休眠
    :param unchanged_active_nodes:
    :return:
    """
    select_num = random.randint(0, len(unchanged_active_nodes) - 1)
    unchanged_active_nodes[select_num].sleep()


def consume_energy_per_second(sensor):
    """
    每秒钟网络消耗能量
    :param sensor:
    :return:
    """
    for node in sensor:
        if node.is_asleep:
            node.energy = node.energy - 0.015
            if node.energy <= 0:
                node.is_alive = False
        else:
            node.energy = node.energy - 0.04
            if node.energy <= 0:
                node.is_alive = False


def change(sensor):
    """
    每轮结束时 把is_changed=1的2 把is_changed=2的改为0
    :param sensor:
    :return:
    """
    for node in sensor:
        if node.is_changed == 1:
            node.is_changed = 2
        elif node.is_changed == 2:
            node.is_changed = 0


def count_alive_nodes(sensor):
    """
    统计还存活的结点数
    :param sensor:
    :return:
    """
    return len(sensor)


def get_all_active_nodes(sensor):
    """
    获取所有处于活跃状态的结点数
    :param sensor:
    :return:
    """
    all_active_nodes = []
    for node in sensor:
        if node.is_alive and not node.is_asleep:
            all_active_nodes.append(node)
    all_active_nodes.append(node)
    return all_active_nodes


def remove_deadnodes(sensor):
    """
    移除死亡的节点
    :param sensor:
    :return:
    """
    for node in sensor:
        if not node.is_alive:
            sensor.remove(node)


def paint_rectangle(painter):
    """
    绘制长方形
    :param painter:
    :return:
    """
    painter.up()
    painter.goto(-80, 0)
    painter.left(90)
    painter.down()
    painter.forward(80)
    painter.right(90)
    painter.forward(160)
    painter.right(90)
    painter.forward(160)
    painter.right(90)
    painter.forward(160)
    painter.right(90)
    painter.forward(80)


def paint_nodes(sensor, painter):
    """
    绘制节点
    :param sensor:
    :param painter:
    :return:
    """
    for node in sensor:
        painter.up()
        painter.goto(node.x - 70, node.y - 80)
        painter.down()
        painter.circle(10)
