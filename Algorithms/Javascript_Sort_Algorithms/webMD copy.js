/*

    Take in array of objects
    Loop
        for each object in medications
            for each item in treatableSymptoms
                if treatableSymptoms[i] == checkSymptom
                    treatsIt++
                    highestTemp = MEDICATION OBJECT NAME
                    how many does it treat = treatsIt

    Counter for number of symptoms it treats

*/

function doesItTreatIt(symptoms, medications){
    for (med of medications){
        count = 0
        for(item of med["treateableSymptoms"]){
            for(i=0; i < symptoms.length; i++){
                if (symptoms[i] == item){
                    count++
                    highestTemp = count
                    console.log(`Count is ${count} `+ symptoms[i] , ` Med is: ${med["name"]} `)
                }
            }
        }
    }
}


const symp = ["pain"]
const medication = [
    {
        name: "Sulforaphane",
        treateableSymptoms: [
            "dementia",
            "alzheimeirs",
            "inflamation",
        
        ]
    },
    {
        name: "Test",
        treateableSymptoms: [
            "pain",
            "inflamation"
        ]
    },   
    {
        name: "Test2",
        treateableSymptoms: [
            "pain",
            "pain",
            "inflamation"
        ]
    }
]

doesItTreatIt(symp, medication)