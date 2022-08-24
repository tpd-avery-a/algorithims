
arr = [54,42,65,24,5]
function getPercent(myArr){
    let newArr = []
    let total = 0
    arr.map(item => {
        total = total+item
    })

    for(item in myArr){
        temp = (item/total) * 100
        newArr.push(temp)
    }
    console.log(newArr)
}

getPercent(arr)
