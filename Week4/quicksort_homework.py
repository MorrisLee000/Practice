def quicksort(list):
    smalllist = []
    biglist = []
    pivotlist = []
    #設置3個list
    pivot = list[(len(list)//2)]#使用list最中間的數字做為基準點:
    for i in list:
        if i < pivot:
            smalllist.append(i)
        elif i > pivot:
            biglist.append(i)
        else:
            pivotlist.append(i)
