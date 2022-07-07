def increasingLengths(n):
    ret = []
    sample = [i + 1 for i in range(n)]
    for i in range(1, n):
        aList = []
        maxItems = n - i + 1
        for j in range(maxItems):
            aList.append(sample[j:j + i])
        ret.append(aList)
    return ret