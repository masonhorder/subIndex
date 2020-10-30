def subListConvert(a):
    returnList = []

    def repeatCheck(a):
        for b in a:
            if type(b) == list:
                repeatCheck(b)
            else:
                returnList.append(b)

    if type(a) == list:
        repeatCheck(a)
    else:
        returnList.append(a)            

    return returnList



print(subListConvert([34, 3, 5, 9, 12, 53, 9, [4, 3, 1, 56, 8, [1, 3, 5], [3, 9, 9, [5, 3]], 9, 3], [3, 5, [3, 3, 2], [3, 2, 5]]]))