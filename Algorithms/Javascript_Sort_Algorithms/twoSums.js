function twoSums(arr, target){
    newArr= []
    for (var i=0; i < arr.length; i++){
        for(var j= i+1; j< arr.length; j++){
            if(arr[i] + arr[j] === target){
                    newArr = [i,j]
                    console.log(newArr)
                    return newArr
            }
        }
    }
}

arr = [2,11,7,5]
arr2 = [3,4,5,6,7,8,9,8,9]
twoSums(arr2, 9)


function twoSUms2(arr, target){
    let idx1 =0
    let idx2 =0
    const output =[]
    while(idx1 !== arr.length){
        if(arr[idx1] + arr[idx2] === target){
            output.push(idx1);
            output.push(idx2);
        }else if (idx2 === arr.length){
            idx1++
            idx2 = idex1+1
        }else{
            idx2++
        }
    }
    return output
}