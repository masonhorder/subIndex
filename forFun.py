def subList(a):
    b = str(a)
    b = b.replace('[','')
    b = b.replace(']','')
    c = b.split(', ')
    i = 0
    for d in c:
        c[i]=int(d)
        i+=1

    return(c)



print(subList([34, 3, 5, 9, 12, 53, 9, [4, 3, 1, 56, 8, [1, 3, 5], [3, 9, 9, [5, 3]], 9, 3], [3, 5, [3, 3, 2], [3, 2, 5]]]))