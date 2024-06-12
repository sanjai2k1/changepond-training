export class person{
    //data-member

    pname:string="Ajit"
    pcontact :number=88888;
    paddress : string="chennai"
    psingle:boolean=true

    //constructor
    constructor(pname:string,pcontact:number,paddress:string,psingle:boolean){
        this.pname=pname
        this.pcontact=pcontact
        this.paddress=paddress
        this.psingle = psingle
    }

    //member function
    personDetails(){
        console.log(`Name : ${this.pname} Contact : ${this.pcontact} single : ${this.psingle} address : ${this.paddress}`)
    }

}

// how to create object of class
// let personObj = new person();

// console.log(personObj.pname)
// personObj.personDetails()



// let personObj = new person("Prashant",9999,"Mumbai",true)

// personObj.personDetails()

// let personObj1 = new person("vijay",7777,"banglore",true)
// personObj1.personDetails()


// let personObj2 = new person("suresh",5555,"Hyderabad",true)
// personObj2.personDetails()

export default person;