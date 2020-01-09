def checkPalindrome(inputString):
    i = inputString
    a = len(i)
    b = 0
    count = 1
    while b <= (a/2):
        if i[b] == i[a-b-1]:
            count = 1
            b += 1
        else:
            count = 0
            break
    if count != 0:
        return True
    else:
        return False
