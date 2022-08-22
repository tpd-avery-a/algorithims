function findByIdAndUpate(id, object, collection){
    change = Object.keys(object)
    for(obj of collection){
        if(obj["id"] == id){
            for(i=0; i < change.length; i++){
                obj[change[i]] = object[change[i]]
            }
            console.log("New: ",collection)
        }
    }
}

id = "10"
object = {"k1":"Glee"}
collection = [
    {"id" : "1","k1" : "po","k2" : "g"},
    {"id" : "2","k1" : "po","k2" : "g"},
    {"id" : "3","k1" : "po","k2" : "g"},
    {"id" : "4","k1" : "po","k2" : "g"},
]
findByIdAndUpate(id, object, collection)