function test(myArr){
    console.log(myArr)
    for(var i = 1; i < myArr.length; i ++){
        const temp = myArr[i]
        for(var j = i - 1; j >= 0 ; j--){
            console.log("Before " + myArr)
            if(temp < myArr[j]){
                myArr[j+1] = myArr[j]
                myArr[j] = temp    
            }
            console.log("After  " + myArr)
        }
    }
    console.log(myArr)
}
const myArr = [5,2,1,7,9,0,8,6,4]
const myArr1 = [0,0,3,5,7,2,6,8,4,1]
test(myArr1)