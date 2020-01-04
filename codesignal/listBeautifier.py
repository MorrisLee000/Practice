def listBeautifier(a):
    b = []
    l = len(a)
    if l == 0:
        return b
    else:
        while a and a[0] != a[-1]:
            a.pop(0)
            a.pop(-1) 
        return a
