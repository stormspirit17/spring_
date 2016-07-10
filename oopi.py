setA = [int(n) for n in input().split()]
setB = [int(n) for n in input().split()]

def merge_sort(set):
     if len(set) == 1:
         return set
     m = len(set) / 2
     return merge(merge_sort(set[:m]), merge_sort(set[m:]))

def merge(setA, setB):
    setC = []
    i = j = 0
    while i < len(setA) and j < len(setB):
        if setA[i] < setB[j]:
            setC.append(setA[i])
            i += 1
        else:
            setC.append(setB[j])
            j += 1
    setC += setA[i:]
    setC += setB[j:]

    return setC

setA = merge_sort(setA)
setB = merge_sort(setB)