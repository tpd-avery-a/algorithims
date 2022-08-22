

function ordered_intersection(a, b){
    console.log("1")
    let i = 0; let j = 0; newArr = []
    while(i < a.length && j < b.length){
        console.log("2")
        if(a[i] === b[j]){
            newArr.push(b[j])
            if(a[i] === newArr[newArr.length-1]){
                i++        
                console.log("3")
            }
            if(b[j] === newArr[newArr.length-1]){
                j++
                console.log("4")
            }
            i++
            j++
            console.log("5")
        }
        else{
            i++
            j++
            console.log("6")
        }
    }
    console.log(newArr)
    /*
    loop through both  
    compare a[i] to b[i]
    cannot be duplicate
    newArr[length-1]
    */
}

arr1 = [1,2,3,4,5]
arr2 = [1,6,7,8,9]

ordered_intersection(arr1,arr2)