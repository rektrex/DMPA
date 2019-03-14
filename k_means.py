from random import sample
from copy import deepcopy
from math import sqrt

def dist(x, y):
    return sqrt(sum(list(map(lambda t: (t[0] - t[1]) ** 2, list(zip(x, y))))))

def mean(lot):
    return tuple([sum(t) / len(t) for t in zip(*lot)])

def k_means(points, k):
    centres = []
    pcentres = sample(list(range(len(points))), k)
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
        oldclusters = deepcopy(clusters)

if __name__ == '__main__':
    points = [(1.0, 1.0), (1.5, 2.0), (3.0, 4.0), (5.0, 7.0), (3.5, 5.0), (4.5, 5.0), (3.5, 4.5)]
    k = 3
    result = k_means(points, k)
    print(*result, sep = '\n')
