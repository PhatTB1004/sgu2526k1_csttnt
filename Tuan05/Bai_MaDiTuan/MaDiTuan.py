def DocFile(filename):
    with open(filename, 'r') as f:
        n, xo, yo = map(int, f.readline().strip().split())
    return n, xo, yo
    pass

move = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

def LietKeMa(n, x0, y0, action = "list"):
    bc = [[0] * (n+1) for _ in range(n+1)]
    bc[x0][y0] = 1
    info = {"bc": bc, "n": n, "x0": x0, "y0": y0,
            "buoc": 1, "count": 0, "coDapAn": False, "action": action,}
    TryMa(x0, y0, info)
    if info["count"] == 0:
        print(0)
    pass

def KiemTra(x, y, bc):
    n = len(bc) - 1
    if x < 1 or x > n or y < 1 or y > n:
        return False
    if bc[x][y] != 0:
        return False
    return True
    pass

def TryMa(x, y, info):
    if info["coDapAn"] is True and info["action"] == "find":
        return
    bc, n = info["bc"], info["n"]
    x0, y0 = info["x0"], info["y0"]
    for dx, dy in move:
        x1, y1 = x + dx, y+ dy
        if KiemTra(x1, y1, bc):
            info["buoc"] += 1
            bc[x1][y1] = info["buoc"]
            if info["buoc"] == n*n:
                for dx, dy in move:
                    if x1 + dx == x0 and y1 + dy == y0:
                        info["coDapAn"] = True
                        info["count"] += 1
                        InBanCo(info)
                        pass
                    pass
                pass
            else:
                TryMa(x1, y1, info)
            info["buoc"] -= 1
            bc[x1][y1] = 0
            pass
        pass
    pass

def InBanCo(info):
    print(info['count'])
    for i in range(1, info['n']+1):
        for j in range(1, info['n']+1):
            print(info['bc'][i][j], end=' ')
        print()
        pass
    print()
    pass