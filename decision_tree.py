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

def findMinGain(columns, titles, level = 0, pClass = ''):

    if len(set(columns[-1])) == 1:
        res = ' ' * level * 2 + pClass + '->' + str(columns[-1][0])
        print(res)
        return

    if len(columns) == 1:
        counts = countsOfTypes(columns[-1])
        vals = list(counts.values())
        keys = list(counts.keys())
        label = keys[vals.index(max(vals))]
        res = ' ' * level * 2 + pClass + '->' + label
        print(res)
        return

    colCount = len(columns[0])
    types = list(map(lambda col: len(set(col)), columns))

    counts = [countsOfTypes(col) for col in columns]

    globalEntropy = 0
    for i in counts[-1].values():
        globalEntropy += i/colCount * log2(i/colCount)
    globalEntropy *=-1

    localEntropies = [0] * (len(columns) - 1)
    for (j, c) in enumerate(counts[:-1]):
        for i in c.items():
            dClasses = []
            for (k,cs) in enumerate(columns[j]):
                if cs == i[0]:
                    dClasses.append(columns[-1][k])

            dCounts = countsOfTypes(dClasses)
            tmp = 0
            for k in dCounts.values():
                tmp += k * log2(k/i[1])
            tmp *= -1 / colCount
            localEntropies[j] += tmp

    minIndex = localEntropies.index(min(localEntropies))
    if level == 0:
        res = titles[minIndex]
    else:
        res = ' ' * level * 2 + pClass + '->' + titles[minIndex]
    print(res)
    titles = titles[:minIndex] + titles[minIndex+1:]
    for part in counts[minIndex]:
        tColumns = [[] for i in range(len(columns) - 1)]
        for i in range(len(columns[0])):
            if part == columns[minIndex][i]:
                k = 0
                for j in range(len(columns)):
                    if j != minIndex:
                        tColumns[k].append(columns[j][i])
                        k += 1

        findMinGain(tColumns, titles, level + 1, pClass = part)

if __name__ == '__main__':
    titles = readTitles()
    data = readData()
    columns = [[rows[i] for rows in data] for i in range(len(titles))]
    findMinGain(columns, titles)
