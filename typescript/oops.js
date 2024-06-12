"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.person = void 0;
var person = /** @class */ (function () {
    //constructor
    function person(pname, pcontact, paddress, psingle) {
        //data-member
        this.pname = "Ajit";
        this.pcontact = 88888;
        this.paddress = "chennai";
        this.psingle = true;
        this.pname = pname;
        this.pcontact = pcontact;
        this.paddress = paddress;
        this.psingle = psingle;
    }
    //member function
    person.prototype.personDetails = function () {
        console.log("Name : ".concat(this.pname, " Contact : ").concat(this.pcontact, " single : ").concat(this.psingle, " address : ").concat(this.paddress));
    };
    return person;
}());
exports.person = person;
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
exports.default = person;
