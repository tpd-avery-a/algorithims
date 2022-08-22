function diagonal(p){
    /*
    Return the positive sum of a cubed array
    The array.length and array[0].length are equal
    */
    arr[[]] = p
    
    i=0
    sum1 =0, sum2=0 
    while(i < arr[[0]].length){
        sum1 += arr[i][i]
        sum2 += arr[i][(arr.length-1)-i]
        i++
        console.log("sum"+sum1,sum2)
    }
    //console.log(sum1,sum2)
    total = sum1-sum2
    if (total < 0){
        return console.log(total * -1)
    }else{
        return console.log(total)
    }
}

arr = [
        [9,2,3],
        [4,5,6],
        [7,8,9]
]

diagonal(arr)