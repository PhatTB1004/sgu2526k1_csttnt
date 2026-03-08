actions = [(-1,0),(1,0),(0,-1),(0,1)]
h = 11

def result_path(path, start, end):
    if end not in path:
        return []
    rev_path = []
    u = end
    while u is not None:
        rev_path.append(u)
        u = path[u]
    rev_path.reverse()
    return rev_path
    pass

def AStartSearch(G, start, goal, wall_ngang, wall_doc):
    path = {}
    g = {}
    f = {}
    OPEN = MinHeap()
    CLOSED = set()  

    path[start] = None
    g[start] = 0
    h_start = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    f[start] = g[start] + h_start
    OPEN.push((f[start], start))

    while not OPEN.empty():
        _, p = OPEN.pop()
        if p in CLOSED:
            continue
        CLOSED.add(p)

        if p == goal:
            print("Found goal:", p)
            break

        x, y = p

        for dx, dy in actions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 6 and 0 <= ny < 6):
                continue
            if dx == -1 and wall_ngang[x][y] == 1: continue
            if dx == 1 and wall_ngang[x+1][y] == 1: continue
            if dy == -1 and wall_doc[x][y] == 1: continue
            if dy == 1 and wall_doc[x][y+1] == 1: continue

            new_g = g[p] + 1
            new_h = abs(nx - goal[0]) + abs(ny - goal[1])
            new_f = new_g + new_h

            if (nx, ny) not in g or new_g < g[(nx, ny)]:
                g[(nx, ny)] = new_g
                f[(nx, ny)] = new_f
                path[(nx, ny)] = p
                if (nx, ny) in CLOSED:
                    CLOSED.remove((nx, ny))
                OPEN.push((new_f, (nx, ny)))

    return path, g
    pass 

import heapq
class MinHeap:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        heapq.heappush(self.items, item)

    def pop(self):
        return heapq.heappop(self.items)
    
    pass

def create_maze():
    G = [[0]*6 for _ in range(6)]
    G[0][0] = 'S' #Start
    G[5][5] = 'E' #End
    return G
    pass

def read_wall(file_name) -> tuple[list, list]:
    wall_ngang = []
    wall_doc   = []

    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        i = 0
        while i < len(lines):
            if lines[i] == 'ngang':
                i += 1
                for _ in range(7):
                    wall_ngang.append(list(map(int, lines[i].split())))
                    i += 1
                    pass
                pass
            elif lines[i] == 'doc':
                i += 1
                for _ in range(6):
                    wall_doc.append(list(map(int, lines[i].split())))
                    i += 1
                    pass
                pass
            else: i += 1
            pass

    return wall_ngang, wall_doc 
    pass

def print_maze_walls(G, wall_ngang, wall_doc, path = []):
    n = len(G)
    if path != []:
        path_set = set(path)
        for i in range(n):
            for j in range(n):
                if (i, j) in path_set:
                    G[i][j] = 1
            pass
        pass
    for i in range(n):
        for j in range(n):
            if wall_ngang[i][j] == 1:
                print("+---", end="")
            else:
                print("+   ", end="")
            pass
        print("+")
        
        for j in range(n):
            if wall_doc[i][j] == 1:
                print("|", end="")
            else:
                print(" ", end="")
            print(f" {G[i][j]} ", end="")
            pass
        if wall_doc[i][n] == 1:
            print("|")
        else:
            print(" ")
        pass
    
    for j in range(n):
        if wall_ngang[n][j] == 1:
            print("+---", end="")
        else:
            print("+   ", end="")
        pass
    print("+")
    pass

def print_dep(G):
    for row in G:
        print(' '.join(str(x) for x in row))
    pass