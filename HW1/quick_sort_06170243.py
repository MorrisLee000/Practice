def quicksort(list):
    smalllist = []
    biglist = []
    pivotlist = []
    #設置3個list
    if len(list) <= 1: #判斷list是否超過一個元素，如果只有一個或沒有就直接出list
        return list
    else:
        pivot = list[-1]  #使用list最後面的值做為基準點:
        for i in list:    #讓每隔元素都去與基準點比較
            if i < pivot:
                smalllist.append(i)
            elif i > pivot:
                biglist.append(i)
            else:
                pivotlist.append(i)
            
    smalllist = quicksort(smalllist)#重複呼叫fuction，直到smalllist和biglist都只剩下最後一個才會停止
    biglist = quicksort(biglist)
    return smalllist + pivotlist + biglist  #最後把所有元素都重新組合在一起
