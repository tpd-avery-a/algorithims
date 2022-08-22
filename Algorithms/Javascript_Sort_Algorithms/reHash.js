const str1 = "b70a164c32a20c10"
const expected1 = "a184b70c42"

function rehash(str){
    dict = {}
    for(let i=0; i < str.length; i++){
        if(dict[str[i]] == false){
            temp = ""
            for(j= i+1; j< str.length; j++){
                temp += str[j]
            }
            dict[str[i]] = temp
            while(isInteger(str[j])){
                temp = temp.append(str[i])
                j++
            }
            dict[str[i]] = [str[i]]
            dict[str[i]] += parseInt(temp)
        }
    }
}

rehash(str1)