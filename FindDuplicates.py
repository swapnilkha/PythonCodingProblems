''' Given a list, return a list containing all duplicate elements in the list in O(n) time '''

''' Input: lst, a list of numbers. Output: a list containing all the duplicate values in lst '''
def find_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if lst[abs(lst[i])] >= 0:
            lst[abs(lst[i])] = -lst[abs(lst[i])]
        else:
            result.append(abs(lst[i]))
    return result
