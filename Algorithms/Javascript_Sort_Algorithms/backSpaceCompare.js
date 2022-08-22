i = 0
j = 0 
s11 = "a3jjd#fe#"
s21 = "a3jjd##fe#"

function backSpace(s1,s2){
    while(i < s1 & j < s2){
        if( s1[i] == "#"){
            s1.slice(i-1, i)
        }
        if(s2[i] == "#"){
            s1.slice(i-1,i)
        }
    }
    return s1 === s2
}

console.log(backSpace(s11, s21))

