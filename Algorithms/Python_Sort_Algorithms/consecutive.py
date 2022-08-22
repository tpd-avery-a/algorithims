
def consec(arr):
    target = 16
    for i in len(arr):
        twoD = []
        count = 0 
        temp = []
        temp.push(arr[i])
        for j in len(arr)+1:
            count += arr[j]
            temp.push(arr[j])
            if count == target:
                twoD.push(temp)
    print(twoD)

arr = [2,5,3,6,7,0,0,23,16]



def consec2(arr,target):

    newArr = []
    for i in arr:
        sum = i
        for j in arr:
            if sum > target:
                break
            if sum == target:
                newArr.append(arr[i:j])
            sum += arr[j]

        
    print(newArr)

consec2(arr, 16)