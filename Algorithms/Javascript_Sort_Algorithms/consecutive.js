
function consec(arr)
{
    target = 16

    twoD = []
    for(i =0; i < arr.length; i++){
            sum = arr[i]
            temp = []
            for( j =i+1; j< arr.length +1; j++){
                if(sum > target){
                    break
                }
                if(sum == target){
                    twoD.push(arr.slice(i,j))
                }
                sum += arr[j]
            }
    if(arr != []){
            console.log(twoD)
        }
    }
}
arr = [2,5,3,6,7,0,0,23,16]
consec(arr)