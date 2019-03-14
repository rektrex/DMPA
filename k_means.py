from random import sample
from copy import deepcopy

def k_means(points, k):
    centres = sample(points, k)
    oldclusters = [[] for _ in range(k)]
    while True:
        clusters = [[] for _ in range(k)]
        for p in points:
            dists = list(map(lambda x: sum(list(map(lambda t: (t[0] - t[1]) ** 2, list(zip(x, p))))) ** (0.5), centres))
            clusters[dists.index(min(dists))].append(p)

        if clusters == oldclusters:
            return clusters

        centres = list(map(lambda c: tuple([sum(t) / len(t) for t in zip(*c)]), clusters))
        oldclusters = deepcopy(clusters)

if __name__ == '__main__':
    with open('points.txt', 'r') as f:
        t = f.readlines()
        p = list(map(lambda x: x.rstrip('\n'), t))
        points = list(map(lambda y: tuple(map(float, y.split(','))), p))
        result = k_means(points, k = 3)
        print(*result, sep = '\n')
