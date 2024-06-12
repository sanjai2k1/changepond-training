class person{
    //data-member

    pname:string="Ajit"
    pcontact :number=88888;
    paddress : string="chennai"
    psingle:boolean=true

    //member function
    personDetails(){
        console.log(`Name : ${this.pname} Contact : ${this.pcontact} single : ${this.psingle} address : ${this.paddress}`)
    }

}

// how to create object of class
let personObj = new person();

console.log(personObj.pname)
personObj.personDetails()


