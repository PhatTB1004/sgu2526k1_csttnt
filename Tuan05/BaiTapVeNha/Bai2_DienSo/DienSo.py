def DocFile(filename):
    with open(filename, 'r') as f:
        bs = []
        for line in f:
            row = [0 if c == '.' else int(c) for c in line.strip()]
            bs.append(row)
            pass
        pass
    return bs
    pass

def LietKeDienSo(bs):
    if TryDienSo(bs):
        InDep(bs)
    else:
        print('IMPOSSIBLE')
    pass

def TryDienSo(bs):
    for i in range(9):
        for j in range(9):
            if bs[i][j] == 0:
                for x in range(1,10):
                    if KiemTra(x, i, j, bs):
                        bs[i][j] = x
                        if TryDienSo(bs):
                            return True
                        bs[i][j] = 0
                        pass
                    pass
                return False
                pass
            pass
        pass
    return True
    pass

def KiemTra(x, r, c, bs):
    for j in range(9):
        if bs[r][j] == x:
            return False
    for i in range(9):
        if bs[i][c] == x:
            return False
    sr = (r//3)*3
    sc = (c//3)*3
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if bs[i][j] == x:
                return False
    return True
    pass

def InDep(bs):
    for i in range(len(bs)):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(len(bs)):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(bs[i][j], end=" ")
            pass
        print()
        pass
    pass
