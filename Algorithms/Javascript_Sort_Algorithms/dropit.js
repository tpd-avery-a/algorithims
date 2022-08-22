const arr1 = [1,3,2,9,6,4,2,6,7,4,2]
const callback1 = (elem) => {
    return 5 < elem
}
function dropit(arr,callback){
    for(let i=0; i < arr.length; i++){
        if(callback(arr[0]) == false){
            arr.shift()  
        }
        else{
            break;
        }
    }
    console.log(arr)
}

dropit(arr1,callback1)