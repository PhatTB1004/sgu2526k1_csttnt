def docfile(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        hv = []
        for line in f:
            hv.append(line.replace("\n",""))
            pass
        pass
    return n, hv
    pass

def LietKeHoanVi(n, hv):
    hoanvi = [0] * (n+1)
    count = 0
    info = {"n": n, "hv": hv, "hoanvi": hoanvi,
            "count": count}
    TryHoanVi(info, 1, False)
    print(info["count"])
    TryHoanVi(info, 1, True)
    pass

def TryHoanVi(info, t, isprint=False):
    n, hv, hoanvi = info["n"], info["hv"], info["hoanvi"]
    for i in hv:
        if KiemTra(i, info):
            hoanvi[t] = i
            if t == n:
                info["count"] +=1
                if isprint:
                    InHoanVi(info)
                pass
            else:
                TryHoanVi(info, t+1, isprint)
            hoanvi[t] = 0
            pass
        pass
    pass

def KiemTra(x, info):
    hoanvi = info["hoanvi"]
    for i in hoanvi:
        if x == i:
            return False
    return True
    pass

def InHoanVi(info):
    for i in info["hoanvi"][1:]:
        print(i, end=" ")
    print()
    pass