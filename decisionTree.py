from math import log2

def readTitles():
    with open('dt.csv', 'r') as f:
        titles = f.readline().rstrip('\n').split(',')
        return titles

def readData():
    with open('dt.csv', 'r') as f:
        f.readline()
        data = list(map(lambda x: x.rstrip('\n'), f.readlines()))
        data = list(map(lambda x: x.split(','), data))
        return data

def countsOfTypes(column):
    counts = {}
    for val in column:
        counts[val] = counts.get(val, 0) + 1

    return counts

if __name__ == '__main__':
    titles = readTitles()
    data = readData()

    columns = [[rows[i] for rows in data] for i in range(len(titles))]
    colCount = len(columns[0])

    types = list(map(lambda col: len(set(col)), columns))

    counts = [countsOfTypes(col) for col in columns]

    temp = counts[-1].values()

    globalEntropy = 0
    for i in temp:
        globalEntropy += i/colCount * log2(i/colCount)
    globalEntropy *= -1

    localEntropies = [0] * (len(columns) - 1)
    for i in range(len(columns) - 1):
        tempKeys = list(counts[i].keys())
        tempVals = list(counts[i].values())
        totalLent = 0
        for j in range(len(counts[i]) -1):
            gCounts = {}
            key = tempKeys[j]
            val = tempVals[j]
            for k in range(len(columns[i])):
                if key == columns[i][k]:
                    gCounts[columns[-1][k]] = gCounts.get(columns[-1][k], 0) + 1
            lent = 0
            for p in list(gCounts.values()):
                print(p)
                print(val)
                lent += p/val * log2(p/val)
            lent *= -1 * val / colCount
            totalLent += lent

        localEntropies[i] = totalLent

    print(globalEntropy)
    print(localEntropies)
