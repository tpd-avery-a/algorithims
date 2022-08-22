var arrLeft = []
var arrRight = []

function mergeSortedArrays(arr1, arr2){
    let sortedArr = [];
    while(arr1.length && arr2.length){
        if(arr1[0] < arr2[0]){
            sortedArr.push(arr1.shift())
        }
        else{
            sortedArr.push(arr2.shift())
        }
    }
    sortedArr.push(...arr1)
    sortedArr.push(...arr2)

    console.log(sortedArr)
}

