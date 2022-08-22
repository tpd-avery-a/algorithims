def insert_sort(myArr):
    for i in range(1,len(myArr)):
        temp = myArr[i]
        for j in range (i-1, myArr *-1, -1):
            if myArr[j] > temp:
                myArr[j +1] = myArr[j]
                myArr[j] = temp

    print(myArr)
