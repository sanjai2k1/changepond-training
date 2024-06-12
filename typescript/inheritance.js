"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var oops_1 = require("./oops");
var Company = /** @class */ (function (_super) {
    __extends(Company, _super);
    function Company(name, contact, address, single, compName, compGst, compState) {
        var _this = _super.call(this, name, contact, address, single) || this;
        _this.cname = compName;
        _this.gstnumber = compGst;
        _this.state = compState;
        return _this;
    }
    Company.prototype.personDetails = function () {
        console.log("Name:".concat(this.pname, ", Contact : ").concat(this.pcontact, " , Single : ").concat(this.psingle, ",\n             CompanyName: ").concat(this.cname, ", GST Number : ").concat(this.gstnumber, " ,  State: ").concat(this.state));
    };
    return Company;
}(oops_1.default));
var compObj = new Company("Vijay", 7777, "kerala", true, "Changepond", 12345, "TamilNadu");
compObj.personDetails();
