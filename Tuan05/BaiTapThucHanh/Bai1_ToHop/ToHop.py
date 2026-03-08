def docfile(filename):
    with open(filename, 'r') as f:
        content = f.readlines()
        n, k = [int(si.replace('\n', '')) for si in content[0].split(' ')[:2]]
        th = [si.replace('\n', '') for si in content[1:]]
        pass
    return n, k, th
    pass
def InDapAn(tohop, th):
    for i in range(1, len(tohop)):
        print(th[tohop[i]-1], end=' ')
    print()
    pass
def LietKeToHop(n, k, th):
    tohop = [-1]*(k+1)
    tohop[0] = 0
    info = dict(tohop = tohop, count = 0, n = n, k = k, th = th)
    tryToHop(info, 1, False)
    print(info['count'])
    tryToHop(info, 1, True)
    pass
def tryToHop(info, i, isprint=False):
    tohop, k, n = info["tohop"], info["k"], info["n"]
    for j in range(tohop[i-1]+1, n-k+i+1):
        tohop[i] = j
        if i == k:
            info['count'] += 1
            if isprint:
                InDapAn(tohop, info['th'])
        else:
            tryToHop(info, i+1, isprint)
        tohop[i] = -1
        pass
    pass