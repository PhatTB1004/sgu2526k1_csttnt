class State:
    actions = [(-1,0),(1,0),(0,-1),(0,1)]

    def __init__(self, key, parent=None, cost=0):
        self.key = [[v for v in row] for row in key]
        self.parent = parent
        self.pos0 = State.find0(key)
        self.cost = cost
        pass

    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return (i, j)
        return (-1, -1)
        pass

    def convert_key(key):
        return tuple(tuple(row) for row in key)
        pass

    def tokey(self):
        return State.convert_key(self.key)
        pass

    def expand(self):
        d,c = self.pos0
        for i in range(len(State.actions)):
            dn, cn = d + State.actions[i][0], c + State.actions[i][1]
            if 0 <= dn < 3 and 0 <= cn < 3:
                staten = [[v for v in row] for row in self.key]
                staten[d][c], staten[dn][cn] = staten[dn][cn], staten[d][c]

                yield staten
                pass
            pass
        pass

    def compare(key1, key2):
        for i in range(3):
            for j in range(3):
                if key1[i][j] != key2[i][j]:
                    return False
        return True        
        pass

def bfs(start, goal):
    frontier = []
    states = dict({})

    sNode = State(start, None, 0)
    gNode = State(goal)

    states[sNode.tokey()] = sNode
    frontier.append(start)
    while len(frontier) > 0:
        curk = frontier.pop(0)
        curNode = states[State.convert_key(curk)]

        if State.compare(curk, goal) is True:
            break

        for childk in curNode.expand():
            childNode = State(childk)
            if states.get(childNode.tokey()) is None:
                childNode.parent = curNode
                childNode.cost = curNode.cost + 1
                states[childNode.tokey()] = childNode
                frontier.append(childk)
                pass
            pass
        pass

    return states
    pass

def result(start, goal):
    states = bfs(start, goal)
    gkey = State.convert_key(goal)

    if gkey not in states:
        return []

    path = []
    curNode = states[gkey]
    while curNode is not None:
        path.append(curNode.key)
        curNode = curNode.parent

    return path[::-1]



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
    n = len(G)
    for i in range(n):
        for j in range(n):
            print(f"{G[i][j]:3}", end=" ")
            pass
        print()
    pass