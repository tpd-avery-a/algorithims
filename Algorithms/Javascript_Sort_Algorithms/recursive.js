function face(num){
    if(num === 1){
        return 1
    }
    return num * face(num -1)
}

console.log(face(3))