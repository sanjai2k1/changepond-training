console.log("good afternoon you all");
//1. number data type
var num1 = 100, num2 = 0.5, num3 = 123456;
console.log(num1, num2, num3);
//2.string
var fname = 'sanjai', lname = 'j';
console.log(fname, lname);
//3.boolean
var cond1 = true, cond2 = false;
console.log(cond1, cond2);
//4.array
var students = ["Ajit", "kartik", "Prashant"];
var emp = ["Radha", "Shradha"];
// for (let student of students){
//     console.log(student)
// }
// students.forEach((student)=>console.log(student))
//5.tuple data : it allow user to store multiple multiple type of data in array.
var product = [101, "laptop"];
// 6.enum data : it is use to create constant variable with value
var days;
(function (days) {
    days[days["sun"] = 0] = "sun";
    days[days["mon"] = 1] = "mon";
    days[days["tue"] = 101] = "tue";
    days[days["wed"] = 102] = "wed";
    days[days["thurs"] = 103] = "thurs";
    days[days["fri"] = 104] = "fri";
    days[days["sat"] = 105] = "sat";
})(days || (days = {}));
var date1 = days.sun;
var date2 = days.mon;
console.log(date1, date2);
