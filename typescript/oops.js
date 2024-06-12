var person = /** @class */ (function () {
    function person() {
        //data-member
        this.pname = "Ajit";
        this.pcontact = 88888;
        this.paddress = "chennai";
        this.psingle = true;
    }
    //member function
    person.prototype.personDetails = function () {
        console.log("Name : ".concat(this.pname, " Contact : ").concat(this.pcontact, " single : ").concat(this.psingle, " address : ").concat(this.paddress));
    };
    return person;
}());
// how to create object of class
var personObj = new person();
console.log(personObj.pname);
personObj.personDetails();
