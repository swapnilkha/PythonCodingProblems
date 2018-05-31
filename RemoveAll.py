''' Given a list of numbers, write a function to remove all occurrences of an element in O(n) time and return the list '''

''' Input: a list of numbers lst, and a value of which all occurrences of it will be removed
    Output: the list with all occurrences of value removed '''
    
def remove_all(lst, value):
    position = 0
    for i in range(len(lst)):
        if lst[i] != value:
            lst[position] = lst[i]
            position += 1
    for k in range(position, len(lst)):
        lst.pop()
    return lst
