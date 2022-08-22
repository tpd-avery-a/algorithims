function entries_insert(objectIn){
    arrayOut = [[]]
    for (key in objectIn){
        arrayOut.push([key, objectIn[key]])
    }
    return console.log(arrayOut)
}

objectIn = {
    name : "pizza",
    calories: 5004
}

entries_insert(objectIn)