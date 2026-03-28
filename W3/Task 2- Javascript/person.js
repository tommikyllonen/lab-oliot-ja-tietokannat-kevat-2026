class Person {
    #age;
    constructor(first_name, last_name, age){
        this.first_name = first_name;
        this.last_name = last_name;
        this.#age = age;
    }
    getAge(){
        return this.#age;
    }
    ageUp(){
        this.#age++;
    }
    getFullname(){
        return (`${this.first_name} ${this.last_name}`);
    }
    printFullName(){
        console.log(this.getFullname());
    }
}

module.exports = Person