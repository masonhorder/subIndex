returnList = []
def repeatCheck(a, returnList):
    # print(returnList)
    for b in a:
        if type(b) == list:
            repeatCheck(b,returnList)
        else:
            returnList.append(b)
    return returnList

# def subListConvert(a):


# if type(a) == list:
#     repeatCheck(a,returnList)
# else:
#     returnList.append(a)            




print(repeatCheck([34, 3, 5, 9, 12, 53, 9, [4, 3, 1, 56, 8, [1, 3, 5], [3, 9, 9, [5, 3]], 9, 3], [3, 5, [3, 3, 2], [3, 2, 5]]], returnList))