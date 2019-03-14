items = [1, 2, 3, 4, 5]

dataset = [ [1, 2, 3, 4],
            [1, 2, 3, 4, 5],
            [2, 3, 4],
            [1, 2, 4],
            [2, 3, 5],
            [1, 3, 4],
            [2, 3, 4, 5],
            [1, 3, 4, 5],
            [3, 4, 5],
            [1, 2, 3, 5]
          ]

def getFreq(s):
    count = 0
    for i in dataset:
        if all(elem in i for elem in s):
            count = count + 1
    return count

def subsets(s):
    sets = []
    for i in range(1 << len(s)):
        subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
        sets.append(subset)
    return sets

def is_bit_set(num, bit):
    return num & (1 << bit) > 0

def apriori(minSupport):
    L = []
    L.append([[x] for x in items if getFreq([x]) >= minSupport])
    p = 0
    for k in range(1, len(items)):
        C = []
        S = L[k-1]
        for i in range(len(S) - 1):
            for j in range(i+1, len(S)):
                l = S[i]
                h = S[j]
                if l[:p] == h[:p] and l[-1] < h[-1]:
                    sets = subsets(l[:p])
                    temp = []
                    for s in sets:
                        x = [l[-1], h[-1]]
                        x.extend(s)
                        temp.append(x)
                    if all(getFreq(t) >= minSupport for t in temp):
                        tmp = l[:p]
                        tmp.append(l[-1])
                        tmp.append(h[-1])
                        C.append(tmp)
        p = p + 1
        if not C:
            break
        L.append(C)
    return L

def getRules(L, minConfidence):
    for k in L[1:]:
        for l in k:
            maxDen = getFreq(l) * 100 / minConfidence
            for x in range(1, len(l)):
                left = l[:x]
                right = l[x:]
                if getFreq(left) <= maxDen:
                    print(str(left).replace('[', '').replace(']', '').replace(' ', '') + '->' + str(right).replace('[', '').replace(']', ''))
                if getFreq(right) <= maxDen:
                    print(str(right).replace('[', '').replace(']', '').replace(' ', '') + '->' + str(left).replace('[', '').replace(']', ''))

if __name__ == '__main__':
    L = apriori(4)
    print(L)
    print()
    getRules(L, 80)
