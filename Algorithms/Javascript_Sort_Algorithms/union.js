function ba(arr1,arr2){
    i =0
    j=0
    newArr = []
    //console.log("step: Before start")
    while (i< arr1.length && j < arr2.length){
        if(arr1[i] < arr2[j] && arr1[i-1] !== arr1[i] && arr1[i+1] !== arr1[i]){
            newArr.push(arr1[i])
            i++
            console.log("Pushed1: " + arr1[i])
        }
        else if(arr2[j] < arr1[i] && arr2[j-1] !== arr2[j] && arr2[j+1] !== arr2[j]){
            newArr.push(arr2[j])
            j++
            console.log("Pushed2: " + arr2[j])
        }
        else if(arr1[i] == arr2[j]){
            i++
            j++
            newArr.push(arr1[i])
            console.log("pushed3" + arr1[i])
        }
        else if(arr1[i-1] || arr1[i+1] == arr1[i]){
            i++
            console.log("step: Third if" + i)
        }
        else if(arr2[j-1] || arr2[j+1] == arr2[j]){
            j++
            console.log("step: Fourth if" + j)
        }
    } 
    while(i < arr1.length){
        if(arr1[i-1] || arr1[i+1] == arr1[i]){
            i++
        }
        else{
            newArr.push(arr1[i])
            i++
            console.log("step: push" + " "+ arr1[i])
        }
    }
    while(j < arr2.length){
        if(arr2[j-1] || arr2[j+1] == arr2[j]){
            j++
        }
        else{
            newArr.push(arr2[j])
            j++
            console.log("step: push" + " "+ arr1[i])
        }
    }
    console.log(newArr)
}

arr1 = [2,3,3,8,10]
arr2 = [1,3,4,6]
ba(arr1,arr2)