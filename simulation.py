# -- coding:utf-8 --
import Node
import function
import matplotlib.pyplot as pyplot
import matplotlib
import copy
import Settings
import turtle

# 使matplotlib能正常显示中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


# 设置画布，画笔
# turtle.setup(600, 400)
# painter = turtle.Pen()


def improved_one_turn(sensor):
    """
    # 每过一段时间进行的一轮操作(改进的算法)
    :param sensor:
    :return:
    """
    sleeping_nodes = function.get_all_sleeping_nodes(sensor)
    for node in sleeping_nodes:
        if node.is_changed == 0:
            active_nodes = function.get_active_nodes(node, sensor)
            # 没有处于活跃状态的节点
            if len(active_nodes) == 0:
                # 节点进入活跃状态
                node.revive()
            # 有处于活跃状态的节点
            else:
                # 获取上一轮未改变状态的活跃节点
                unchanged_active_nodes = function.get_unchanged_active_nodes(active_nodes)
                if len(unchanged_active_nodes) == 0:
                    # 节点继续休眠
                    node.sleep()
                else:
                    function.choose_sleep(node)
                    if not node.is_asleep:
                        function.random_select(unchanged_active_nodes)
    function.change(sensor)


def one_turn(sensor):
    """
    每过一段时间进行的一轮操作(之前的算法)
    :param sensor:
    :return:
    """
    sleeping_nodes = function.get_all_sleeping_nodes(sensor)
    for node in sleeping_nodes:
        active_nodes = function.get_active_nodes(node, sensor)
        # 没有处于活跃状态的节点
        if len(active_nodes) == 0:
            node.revive()


def compare_a():
    """
    比较a的大小对存活数的影响
    :return:
    """
    # 绘图横纵坐标数据
    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []
    # 计时
    t = 0
    # 所有节点列表
    sensor = []
    for i in range(Settings.node_count):
        node = Node.Node()
        node.set_scope(Settings.scope)
        node.random_position()
        sensor.append(node)
    # 所有节点以P的概率苏醒
    for node in sensor:
        function.choose_sleep(node)
        node.is_changed = 0

    # 节点列表保持一致
    sensor2 = copy.deepcopy(sensor)
    sensor3 = copy.deepcopy(sensor)

    # a=0.7
    Settings.set_a(0.7)
    while function.count_alive_nodes(sensor) != 0:
        x1.append(t)
        y1.append(function.count_alive_nodes(sensor))
        function.consume_energy_per_second(sensor)
        function.remove_deadnodes(sensor)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor)
            function.remove_deadnodes(sensor)

    t = 0
    # a=0.8
    Settings.set_a(0.8)
    while function.count_alive_nodes(sensor2) != 0:
        x2.append(t)
        y2.append(function.count_alive_nodes(sensor2))
        function.consume_energy_per_second(sensor2)
        function.remove_deadnodes(sensor2)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor2)
            function.remove_deadnodes(sensor2)

    t = 0
    # a=0.9
    Settings.set_a(0.9)
    while function.count_alive_nodes(sensor3) != 0:
        x3.append(t)
        y3.append(function.count_alive_nodes(sensor3))
        function.consume_energy_per_second(sensor3)
        function.remove_deadnodes(sensor3)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor3)
            function.remove_deadnodes(sensor3)

    line1, = pyplot.plot(x1, y1, linewidth=2)
    line2, = pyplot.plot(x2, y2, linewidth=2)
    line3, = pyplot.plot(x3, y3, linewidth=2)
    legend = pyplot.legend([line1, line2, line3], ['a=0.7', 'a=0.8', 'a=0.9'], loc='upper right')
    pyplot.title(u"节点存活数目随时间变化图", fontsize=23)
    pyplot.xlabel("时间")
    pyplot.ylabel("生存节点数")
    pyplot.savefig("a对节点存活数的影响" + str(Settings.node_count) + " P=" + str(Settings.P) + ".jpg")
    pyplot.show()


def compare_P():
    """
    比较P的大小对存活数的影响
    :return:
    """
    # 绘图横纵坐标数据
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    # 计时
    t = 0
    # 所有节点列表
    sensor = []
    for i in range(Settings.node_count):
        node = Node.Node()
        node.set_scope(Settings.scope)
        node.random_position()
        sensor.append(node)
    # 所有节点以P的概率苏醒
    for node in sensor:
        function.choose_sleep(node)
        node.is_changed = 0

    # 节点列表保持一致
    sensor2 = copy.deepcopy(sensor)
    sensor3 = copy.deepcopy(sensor)
    sensor4 = copy.deepcopy(sensor)
    sensor5 = copy.deepcopy(sensor)

    # P=0.5
    Settings.set_P(0.5)
    while function.count_alive_nodes(sensor) != 0:
        x1.append(t)
        y1.append(function.count_alive_nodes(sensor))
        function.consume_energy_per_second(sensor)
        function.remove_deadnodes(sensor)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor)
            function.remove_deadnodes(sensor)

    t = 0
    # P=0.6
    Settings.set_P(0.6)
    while function.count_alive_nodes(sensor2) != 0:
        x2.append(t)
        y2.append(function.count_alive_nodes(sensor2))
        function.consume_energy_per_second(sensor2)
        function.remove_deadnodes(sensor2)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor2)
            function.remove_deadnodes(sensor2)

    t = 0
    # P=0.7
    Settings.set_P(0.7)
    while function.count_alive_nodes(sensor3) != 0:
        x3.append(t)
        y3.append(function.count_alive_nodes(sensor3))
        function.consume_energy_per_second(sensor3)
        function.remove_deadnodes(sensor3)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor3)
            function.remove_deadnodes(sensor3)

    t = 0
    # P=0.8
    Settings.set_P(0.8)
    while function.count_alive_nodes(sensor4) != 0:
        x4.append(t)
        y4.append(function.count_alive_nodes(sensor4))
        function.consume_energy_per_second(sensor4)
        function.remove_deadnodes(sensor4)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor4)
            function.remove_deadnodes(sensor4)

    t = 0
    # P=0.9
    Settings.set_P(0.9)
    while function.count_alive_nodes(sensor5) != 0:
        x5.append(t)
        y5.append(function.count_alive_nodes(sensor5))
        function.consume_energy_per_second(sensor5)
        function.remove_deadnodes(sensor5)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor5)
            function.remove_deadnodes(sensor5)

    line1, = pyplot.plot(x1, y1, linewidth=2)
    line2, = pyplot.plot(x2, y2, linewidth=2)
    line3, = pyplot.plot(x3, y3, linewidth=2)
    line4, = pyplot.plot(x4, y4, linewidth=2)
    line5, = pyplot.plot(x5, y5, linewidth=2)
    legend = pyplot.legend([line1, line2, line3, line4, line5], ['P=0.5', 'P=0.6', 'P=0.7', 'P=0.8', 'P=0.9'],
                           loc='upper right')
    pyplot.title(u"节点存活数目随时间变化图", fontsize=23)
    pyplot.xlabel("时间")
    pyplot.ylabel("生存节点数")
    pyplot.savefig("P对节点存活数的影响" + str(Settings.node_count) + " a=" + str(Settings.a) + ".jpg")
    pyplot.show()


def compare_algorithm():
    """
    算法性能比较
    :return:
    """
    # 绘图横纵坐标数据
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    # 计时
    t = 0
    # 所有节点列表
    sensor = []
    for i in range(Settings.node_count):
        node = Node.Node()
        node.set_scope(Settings.scope)
        node.random_position()
        sensor.append(node)
    # 所有节点以P的概率苏醒
    for node in sensor:
        function.choose_sleep(node)
        node.is_changed = 0

    # 原有算法的节点列表 保持一致
    sensor2 = copy.deepcopy(sensor)

    # 改进的算法
    while function.count_alive_nodes(sensor) != 0:
        x1.append(t)
        y1.append(function.count_alive_nodes(sensor))
        function.consume_energy_per_second(sensor)
        function.remove_deadnodes(sensor)
        t = t + 1
        if t % 10 == 0:
            improved_one_turn(sensor)
            function.remove_deadnodes(sensor)
        # 绘制存活的节点
        # if t == 40 or t == 70 or t == 80 or t == 95:
        #     all_active_nodes = function.get_all_active_nodes(sensor)
        #     function.paint_rectangle(painter)
        #     function.paint_nodes(all_active_nodes, painter)
        #     time.sleep(30)
        #     painter.reset()

    t = 0
    # 原有的算法
    while function.count_alive_nodes(sensor2) != 0:
        x2.append(t)
        y2.append(function.count_alive_nodes(sensor2))
        function.consume_energy_per_second(sensor2)
        function.remove_deadnodes(sensor2)
        t = t + 1
        if t % 10 == 0:
            one_turn(sensor2)
            function.remove_deadnodes(sensor2)
        # 绘制存活的节点
        # if t == 40 or t == 70 or t == 80 or t == 95:
        #     all_active_nodes = function.get_all_active_nodes(sensor2)
        #     function.paint_rectangle(painter)
        #     function.paint_nodes(all_active_nodes, painter)
        #     time.sleep(30)
        #     painter.reset()

    # 绘制存活节点图表
    line1, = pyplot.plot(x1, y1, linewidth=2)
    line2, = pyplot.plot(x2, y2, linewidth=2)
    legend = pyplot.legend([line1, line2], ['改进的算法', '原来的算法'], loc='upper right')
    pyplot.title(u"节点存活数目随时间变化图", fontsize=23)
    pyplot.xlabel("时间")
    pyplot.ylabel("生存节点数")
    pyplot.savefig("picture" + str(Settings.node_count) + " a=" + str(Settings.a) + " P=" + str(Settings.P) + ".jpg")
    pyplot.show()


if __name__ == "__main__":
    # compare_a()
    # compare_P()
    compare_algorithm()
