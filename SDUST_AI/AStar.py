from math import sqrt

times = 0


def value_h(st_x, st_y, ed_x, ed_y):
    # return sqrt((st_x - ed_x) * (st_x - ed_x) + (st_y - ed_y) * (st_y - ed_y))
    return abs(st_x - 1 - ed_x) + abs(st_y - ed_y)


class Map(object):
    def __init__(self, tmp_mp, st, ed):
        st_x, st_y = st
        ed_x, ed_y = ed
        self.mp = tmp_mp
        self.st_x = st_x
        self.st_y = st_y
        self.ed_x = ed_x
        self.ed_y = ed_y


class Node(object):
    def __init__(self, x, y, g, h, father):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.father = father

    def update_surround(self, cur_ground, ed_x, ed_y):
        global times
        times = times + 1
        x = self.x
        y = self.y
        ans = []
        if x != 0 and cur_ground[x - 1][y] != 1:
            upNode = Node(x - 1, y, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(upNode)
        # 下
        if x != len(cur_ground) - 1 and cur_ground[x + 1][y] != 1:
            downNode = Node(x + 1, y, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(downNode)
        # 左
        if y != 0 and cur_ground[x][y - 1] != 1:
            leftNode = Node(x, y - 1, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(leftNode)
        # 右
        if y != len(cur_ground[0]) - 1 and cur_ground[x][y + 1] != 1:
            rightNode = Node(x, y + 1, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(rightNode)
        # 左上
        if x != 0 and y != 0 and cur_ground[x - 1][y - 1] != 0:
            wnNode = Node(x - 1, y - 1, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(wnNode)
        # 右上
        if x != 0 and y != len(cur_ground[0]) - 1 and cur_ground[x - 1][y + 1] != 0:
            enNode = Node(x - 1, y + 1, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(enNode)
        # 左下
        if x != len(cur_ground) - 1 and y != 0 and cur_ground[x + 1][y - 1] != 0:
            wsNode = Node(x + 1, y - 1, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(wsNode)
        # 右下
        if x != len(cur_ground) - 1 and y != len(cur_ground[0]) - 1 and cur_ground[x + 1][y + 1] != 0:
            esNode = Node(x + 1, y + 1, self.g + 1, value_h(x, y, ed_x, ed_y), self)
            ans.append(esNode)
        return ans

    def changeG(self, surround):
        for i in surround:
            if i.x == self.x and i.y == self.y:
                if i.g > self.g:
                    i.g = self.g


def sort_rule(element: Node):
    return element.g + element.h


def solve(workMap):
    st_x, st_y = workMap.st_x, workMap.st_y  # 起始结点位置
    ed_x, ed_y = workMap.ed_x, workMap.ed_y  # 目的结点位置
    startNode = Node(st_x, st_y, 0, 0, None)  # 创建起始结点
    opening = []  # OPEN表，可以走的
    closed = [startNode]  # 走过的
    currNode = startNode  # 当前结点
    while (currNode.x, currNode.y) != (ed_x, ed_y):  # 循环搜索，直到到达目的地
        valid_surround = currNode.update_surround(workMap.mp, ed_x, ed_y)  # 更新可用结点与对应G值
        for i in valid_surround:  # 遍历周围结点
            if i not in closed:  # 如果没走过
                if i in opening:  # 如果在OPEN表中
                    i.changeG(opening)  # 更新G值
                else:  # 不在open也不在close中
                    opening.append(i)  # 添加到open表
        opening.sort(key=sort_rule)  # 把最小（G + H）值的排前面
        currNode = opening.pop(0)  # 将最小值结点弹出作为当前节点
        closed.append(currNode)  # 标记当前结点已经走过
    # 搜索完成
    ans = []
    while currNode.father is not None:  # 根据父亲结点回溯路径
        ans.append((currNode.x, currNode.y))
        currNode = currNode.father
    ans.append((currNode.x, currNode.y))
    ans.reverse()  # 将从后往前的顺序颠倒过来，变成从前往后的方向
    return ans


def show(ground):
    print("=====================================")
    final_map = []
    for i in range(len(ground)):
        temp_str = ""
        for j in range(len(ground[i])):
            if ground[i][j] == 0:
                temp_str += '.'
            elif ground[i][j] == 1:
                temp_str += '@'
            elif ground[i][j] == 2:
                temp_str += '*'
        final_map.append(temp_str)
    for line in final_map:
        print(line)
    print("=====================================")


def main():
    ground = [
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    print(f"原地图")
    show(ground)
    start = (0, 0)
    end = (4, 4)
    current_map = Map(ground, start, end)
    result = solve(current_map)
    for point in result:
        ground[point[0]][point[1]] = 2
    print(f"最佳路径地图")
    show(ground)
    print(f"起点{start}, 终点{end}")
    for i in range(len(result)):
        result[i] = (result[i][0] + 1, result[i][1] + 1)
    print(f"最佳路径{result}")
    print(f"总搜索步数{times}")


main()
