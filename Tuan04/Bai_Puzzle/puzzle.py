import heapq
import itertools

class State:
    actions = [(-1,0),(1,0),(0,-1),(0,1)]

    def __init__(self, key, parent=None, cost=0):
        self.key = [[v for v in row] for row in key]
        self.parent = parent
        self.pos0 = State.find0(key)
        self.g = cost   
        self.h = 0        
        self.f = 0         
        pass
    
    @staticmethod
    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return (i, j)
        return (-1, -1)
        pass
    
    @staticmethod
    def convert_key(key):
        return tuple(tuple(row) for row in key)
        pass

    def tokey(self):
        return State.convert_key(self.key)
        pass

    def expand(self):
        d, c = self.pos0
        for action in State.actions:
            dn, cn = d + action[0], c + action[1]
            if 0 <= dn < 3 and 0 <= cn < 3:
                staten = [[v for v in row] for row in self.key]
                staten[d][c], staten[dn][cn] = staten[dn][cn], staten[d][c]

                yield staten
                pass
            pass
        pass

    @staticmethod
    def compare(key1, key2):
        for i in range(3):
            for j in range(3):
                if key1[i][j] != key2[i][j]:
                    return False
        return True   
        pass

def heuristic(current, goal):
    distance = 0
    goal_pos = {}

    for i in range(3):
        for j in range(3):
            goal_pos[goal[i][j]] = (i, j)

    for i in range(3):
        for j in range(3):
            val = current[i][j]
            if val != 0:
                gi, gj = goal_pos[val]
                distance += abs(i - gi) + abs(j - gj)

    return distance
    pass

def astar(start, goal):
    open_list = []
    states = {}
    counter = itertools.count()

    start_node = State(start, None, 0)
    start_node.h = heuristic(start, goal)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_list, (start_node.f, next(counter), start_node))
    states[start_node.tokey()] = start_node

    closed = set()

    while open_list:
        _, _, current = heapq.heappop(open_list)

        # nếu current đã bị thay bằng node tốt hơn trong states, bỏ qua (stale)
        cur_key = current.tokey()
        if cur_key in states and current.g != states[cur_key].g:
            continue

        if State.compare(current.key, goal):
            return states

        closed.add(cur_key)

        for childk in current.expand():
            child_key = State.convert_key(childk)

            if child_key in closed:
                continue

            g_new = current.g + 1

            # nếu đã có node tốt hơn thì bỏ qua
            if child_key in states and g_new >= states[child_key].g:
                continue

            child_node = State(childk, current, g_new)
            child_node.h = heuristic(childk, goal)
            child_node.f = child_node.g + child_node.h

            states[child_key] = child_node
            heapq.heappush(open_list, (child_node.f, next(counter), child_node))

    return states
    pass

def result(start, goal):
    states = astar(start, goal)
    gkey = State.convert_key(goal)

    if gkey not in states:
        return []

    path = []
    curNode = states[gkey]

    while curNode is not None:
        path.append(curNode.key)
        curNode = curNode.parent

    return path[::-1]
    pass



def read_puzzle(file_name):
    start, goal = [], []

    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        i = 0

        while i < len(lines):
            if lines[i] == 'start':
                i += 1
                for _ in range(3):
                    start.append(list(map(int, lines[i].split())))
                    i += 1
                    pass
                pass
            elif lines[i] == 'goal':
                i += 1
                for _ in range(3):
                    goal.append(list(map(int, lines[i].split())))
                    i += 1
                    pass
                pass
            else: i += 1
            pass
    return start, goal

def print_dep(G):
    for row in G:
        for val in row:
            print(f"{val:3}", end=" ")
        print()
    pass