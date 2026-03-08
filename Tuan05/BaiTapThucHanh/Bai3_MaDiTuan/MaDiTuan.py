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

def soNuocDi(x, y, bc):
    count = 0
    for dx, dy in move:
        if KiemTra(x + dx, y + dy, bc):
            count += 1
        pass
    return count
    pass

def ListMa(x, y, bc):
    listMa = []
    for dx, dy in move:
        if KiemTra(x + dx, y + dy, bc):
            listMa.append((x + dx, y + dy))
        pass
    listMa.sort(key=lambda p: soNuocDi(p[0], p[1], bc))
    return listMa
    pass

def canReturn(x, y, x0, y0):
    for dx, dy in move:
        if x + dx == x0 and y + dy == y0:
            return True
        pass
    return False
    pass    

def TryMa(x, y, info):
    if info["coDapAn"] and info["action"] == "find":
        return
    bc, n = info["bc"], info["n"]
    x0, y0 = info["x0"], info["y0"]
    for x1, y1 in ListMa(x, y, bc):
        info["buoc"] += 1
        bc[x1][y1] = info["buoc"]
        if info["buoc"] == n*n:
            if canReturn(x1, y1, x0, y0):
                info["coDapAn"] = True
                info["count"] += 1
                InBanCo(info)
                pass
            pass
        else:
            TryMa(x1, y1, info)
        info["buoc"] -= 1
        bc[x1][y1] = 0
        pass
    pass

def InBanCo(info):
    print(info['count'])
    for i in range(1, info['n']+1):
        for j in range(1, info['n']+1):
            if info['bc'][i][j] < 10:
                print(" ", end="")
            print(info['bc'][i][j], end=" ")
        print()
        pass
    print()
    pass