def XayBanCo(n):
    hau = [0] * (n+1)
    return hau
    pass

# Back Tracking
def DocFile(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
    return n
    pass

def LietKeHau(n, action = "list"):
    hau = XayBanCo(n)
    info = {"hau": hau, "n": n, "count": 0,
            "coDapAn": False, "action": action,
            "laInDapAn": True}
    XepHau(1, info)
    if info["count"] == 0:
        print(0)
    pass

def KiemTra(hang, cot, hau):
    for i in range(1, hang):
        if hau[i] == cot:
            return False
        if abs(i - hang) == abs(hau[i] - cot):
            return False
    return True
    pass

def XepHau(hang, info):
    if info["coDapAn"] is True and info["action"] == "find":
        return
    
    n, hau = info["n"], info["hau"]
    for cot in range(1, n+1):
        if KiemTra(hang, cot, hau):
            hau[hang] = cot
            if hang == n:
                info['coDapAn'] = True
                info['count'] += 1
                if info["laInDapAn"] is True:
                    InBanCo(info)
            else:
                XepHau(hang + 1, info)
            hau[hang] = 0
            pass
        pass
    pass

def InBanCo(info):
    print(info['count'])
    for i in range(1, info['n']+1):
        for j in range(1, info['n']+1):
            if info['hau'][i] == j:
                print(1, end=' ')
            else:
                print(0, end=' ')
            pass
        print()
        pass
    print()
    pass

# Greedy
def XepHauGreedy(info):
    n, hau = info["n"], info["hau"]
    for hang in range(1, n+1):
        dat_duoc = False
        for cot in range(1, n+1):
            if KiemTra(hang, cot, hau):
                hau[hang] = cot
                dat_duoc = True
                break
            pass
        if not dat_duoc:
            return False
        pass
    info["coDapAn"] = True
    info["count"] = 1
    return True
    pass

def LKHGreedy(n):
    hau = XayBanCo(n)
    info = {"hau": hau, "n": n, "count": 0,
            "coDapAn": False,
            "laInDapAn": True}
    
    XepHauGreedy(info)
    if info["coDapAn"]:
        InBanCo(info)
    else:
        print(0)
    pass