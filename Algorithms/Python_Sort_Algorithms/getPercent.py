
from tempfile import tempdir


arr = [19,45,89,63,34]

#get total
# for each create new array with percent
def get(arr):
    total = sum(arr)
    newArr = []
    for i in arr:
        temp = (i/total) * 100
        newArr.append(temp)
    print(total)
    print(newArr)

get(arr)