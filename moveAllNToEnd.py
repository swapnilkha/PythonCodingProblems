//*Given a list, move all n's to the end*

def moveAllNToEnd(lst, n):
    pos = 0
    for i in range(len(lst)):
        if lst[i] != n:
            lst[pos] = lst[i]
            pos += 1
    while pos < len(lst):
        lst[pos] = n
        pos += 1
    return lst
   
