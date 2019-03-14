from random import sample
from copy import deepcopy

def k_means(points, k):
    centres = [points[i] for i in sample(list(range(len(points))), k)]
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
    points = [(1.0, 1.0), (1.5, 2.0), (3.0, 4.0), (5.0, 7.0), (3.5, 5.0), (4.5, 5.0), (3.5, 4.5)]
    result = k_means(points, k = 3)
    print(*result, sep = '\n')
