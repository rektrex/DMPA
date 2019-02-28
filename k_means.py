import copy
import random
from math import sqrt

def dist(x, y):
    sum = 0
    for i in range(len(x)):
        t = x[i] - y[i]
        sum = sum + t * t
    return sqrt(sum)

def mean(lot):
    p = len(lot[0])
    l = len(lot)
    t = [0 for _ in range(p)]
    for i in range(l):
        for j in range(p):
            t[j] = t[j] + lot[i][j]

    t = tuple(map(lambda x: x / l, t))
    return t

def k_means(points, k):
    centres = []
    pcentres = random.sample(list(range(len(points))), k)
    for i in pcentres:
        centres.append(points[i])

    oldclusters = [[] for _ in range(k)]
    while True:
        clusters = [[] for _ in range(k)]
        for p in points:
            dists = list(map(lambda x: dist(x, p), centres))
            c = dists.index(min(dists))
            clusters[c].append(p)

        if clusters == oldclusters:
            return clusters

        centres = list(map(mean, clusters))
        oldclusters = copy.deepcopy(clusters)

if __name__ == '__main__':
    points = [(1.0, 1.0), (1.5, 2.0), (3.0, 4.0), (5.0, 7.0), (3.5, 5.0), (4.5, 5.0), (3.5, 4.5)]
    k = 3
    result = k_means(points, k)
    for r in result:
        print(r)
