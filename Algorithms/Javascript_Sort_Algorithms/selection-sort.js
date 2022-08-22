function test(){

    console.log("Start Function")
    //Given an array of unsorted numbers return an array of sorted smallest to largest
    const myArr = [3,4,5,6,54,3,]
    //Start a loop through array with i
    for(let i =0 ; i < myArr.length; i++){
        console.log("first loop start")
        //Set a min
        min = i;
        //Start a loop through array +1 after i with j
        for(let j = i + 1; j < myArr.length; j++){
        console.log("second loop start")
            //if myArr[j] is less than myArr[min] than j is the new minimum
            if (myArr[j] < myArr[min]){
                min = j 
            }
        }

        console.log("End For loop")
        //Temporarily hold i
        temp = myArr[i]
        //Set min to i
        myArr[i] = myArr[min]
        //Set temp to myArr[min] 
        myArr[min] = temp
        
    }

    console.log(myArr)

}

console.log(test())
console.log("test")

