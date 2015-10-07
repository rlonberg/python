""" mergeSort
"""

def mergeSort(aList):
    #base
    if len(aList)==1:
            return aList[0]

    midpoint = len(aList)//2
    left = aList[0:midpoint]
    right = aList[midpoint:]

    #recursion on sublists
    left = mergeSort(left)
    right = mergeSort(right)

    #merge?
    return merge(left,right)

def merge(left,right):
    """ only two elements?"""
    if (type(left) == int):
        if left>right:
            return [right,left]
        else:
            return [left, right]
    """ merging elements greater than size 1 """
    merg = []
    while notEmpty(left) or notEmpty(right):
        
        if isEmpty(left):
            merg += right
            right = []
        if isEmpty(right):
            merg += left
            left = []
        else:
            if left[0] > right[0]:
                merg+=[right[0]]
                right = right[1:]
            else:
                merg+=[left[0]]
                left = left[1:]

    return merg


def isEmpty(aList):
    return len(aList)==0

def notEmpty(aList):
    return len(aList)!=0
        
