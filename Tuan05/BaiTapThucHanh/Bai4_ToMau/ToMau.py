def DocFile(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        city = {}
        for line in f:
            u, v = map(int, line.split())
            if u not in city:
                city[u] = []
            if v not in city:
                city[v] = []
            city[u].append(v)
            city[v].append(u) 
            pass
        pass
    return n, city
    pass

def LietKeCity(n, city):
    Mau = [0] * (n+1)
    info = {"Mau": Mau, "city": city, "n": n}
    if TryCity(info, 1):
        InCity(info)
    pass

def TryCity(info, t):
    city, n = info["city"], info["n"]
    if t > n:
        return True
    for c in range(1, n+1):
        info["Mau"][t] = c
        if KiemTra(t, info):
            if TryCity(info, t+1):
                return True
            info["Mau"][t] = 0
            pass
        pass
    return False
    pass

def InCity(info):
    Mau = info["Mau"]
    k = max(Mau[1:])   
    print(k)
    for c in range(1, k+1):
        for i in range(1, len(Mau)):
            if Mau[i] == c:
                print(i, end=' ')
            pass
        print()
        pass
    pass 

def KiemTra(u, info):
    city, Mau = info["city"], info["Mau"]
    for v in Neighbor(city, u):
        if Mau[v] == Mau[u]:
            return False
    return True
    pass

def Neighbor(city, u):
    if u in city:
        return city[u]
    return []
    pass