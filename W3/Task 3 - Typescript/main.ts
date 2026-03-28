class Person {
    #age;
    first_name: string;
    last_name: string;

    constructor(first_name: string, last_name: string, age: number){
        this.first_name = first_name;
        this.last_name = last_name;
        this.#age = age;
    }
    getAge(): number{
        return this.#age;
    }
    ageUp(): void{
        this.#age++;
    }
    getFullname(): string{
        return (`${this.first_name} ${this.last_name}`);
    }
    printFullName(): void{
        console.log(this.getFullname());
    }
}

class Main{
    constructor(){
    console.log("Program starting.")
    console.log("Creating person...")
    const newperson: Person = new Person("John", "Doe", 30)
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