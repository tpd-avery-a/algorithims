
function check(){
    searchFor = {first_name : "Bob", Last_name: "Dylan"}
    arr = [
        {first_name : "Bob", Last_name: "Dylan"},
        {first_name : "Terry", Last_name: "Dylan"},
        {first_name : "Choice", Last_name: "Dylan"},
    ]
    holder= []
        //for each object in the arrat
        for(obj of arr){
            //for each key in object
            for(key in obj){
                //if object[key] matches the key of our object return it
                if(obj[key] === searchFor[key]){
                     const tempObj = {
                        
                     }
                    tempObj[key] = obj[key]
                    holder.push(tempObj)
                    console.log(obj[key])
                }
            }
        }
        return console.log(holder)
    }
check()