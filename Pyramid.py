import math

def pyramidize_min(h):
    if len(h) == 1 or len(h) == 0:
        return h
    h0 = getdepth(h, 0, 1)
    i = int(math.floor(len(h) / 2)) - 1
    while i != -1:
        heapify_min(h, i)
        i -= 1
    X = h
    for i in range(1, h0 + 1):
        pc1 = int(math.pow(2, i - 1))
        pc2 = pc1 << 1
        if i == h0:
            X[(pc1 - 1):(len(h))] = pyramidize_min(h[(pc1 - 1):(len(h))])
        else:
            X[(pc1 - 1):(pc2 - 1)] = pyramidize_min(h[(pc1 - 1):(pc2 - 1)])
    for i in range(1, h0):
        pc1 = int(math.pow(2, i - 1))
        pc2 = pc1 << 1
        pc3 = pc2 << 1
        if i == h0 - 1:
            M = merge_min(X[(pc1 - 1):(pc2 - 1)], X[(pc2 - 1):(len(h))])
            
            X[(pc1 - 1):(pc2 - 1)] = M[0:(pc2 - pc1)]
            X[(pc2 - 1):(len(h))] = M[(pc2 - pc1):(len(h) - pc1 + 1)]
        else:
            M = merge_min(X[(pc1 - 1):(pc2 - 1)], X[(pc2 - 1):(pc3 - 1)])
            X[(pc1 - 1):(pc2 - 1)] = M[0:(pc2 - pc1)]
            X[(pc2 - 1):(pc3 - 1)] = M[(pc2 - pc1):(pc3 - pc1)]
    return X

def heapify_min(h, i):
    visit = i
    while True:
        least = visit
        if 2*visit + 1 < len(h) and h[least] > h[2*visit + 1]:
            least = 2*visit + 1
        if 2*visit + 2 < len(h) and h[least] > h[2*visit + 2]:
            least = 2*visit + 2
        if visit != least:
            tmp = h[least]
            h[least] = h[visit]
            h[visit] = tmp
            visit = least
        else:
            break

def merge_min(x, y):
    if len(x) == 0:
        return y
    if len(y) == 0:
        return x
    if x[0] <= y[0]:
        return [x[0]] + merge_min(x[1:], y)
    else:
        return [y[0]] + merge_min(x, y[1:])

def getdepth(t, i, depth):
    if 2*i + 1 >= len(t):
        return depth
    else:
        ldepth = getdepth(t, 2*i + 1, depth + 1)
        rdepth = 0
        if 2*i + 2 < len(t):
            rdepth = getdepth(t, 2*i + 2, depth + 1)
        if ldepth > rdepth:
            return ldepth
        else:
            return rdepth

def find_min(p, height):
    h0 = getdepth(p, 0, 1)
    return p[int(math.pow(2, h0 - height)) - 1]

def find_max(p, height):
    if height > 1:
        h0 = getdepth(p, 0, 1)
        return p[int(math.pow(2, h0 + 1 - height)) - 2]
    else:
        return p[len(p) - 1]

def insert(p, x):
    merge_min(p, [x])

def status(p):
    if len(p) > 1:
        s = 0
        h0 = getdepth(p, 0, 1)
        for i in range(h0, 2, -1):
            max = find_max(p, i)
            min = find_min(p, i - 1)
            if max <= min and ((s == 0 and i == h0) or s == 1):
                s = 1
            elif max >= min and ((s == 0 and i == h0) or s == 2):
                s = 2
            else:
                return 0
        return s
    else:
        return 0
