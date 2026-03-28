const Person = require('./person');
class Main{
    constructor(){
    console.log("Program starting.")
    console.log("Creating person...")
    const newperson = new Person("John", "Doe", 30)
    console.log("Person created.")
    console.log(`Name: ${newperson.getFullname()}`)
    console.log(`Age: ${newperson.getAge()}`)
    console.log("Person has now birthday...")
    newperson.ageUp()
    console.log(`New age: ${newperson.getAge()}`)
    console.log("Program ending.") 
    }
}

new Main(); 