console.log("good afternoon you all")

//1. number data type

let num1:number = 100,num2:number=0.5,num3:number=123456;
console.log(num1,num2,num3)

//2.string

let fname:string = 'sanjai',lname:string = 'j'
console.log(fname,lname)

//3.boolean
let cond1:boolean = true,cond2:boolean=false
console.log(cond1,cond2)

//4.array
let students:string[] = ["Ajit","kartik","Prashant"]
let emp:Array<string> =["Radha","Shradha"]

// for (let student of students){
//     console.log(student)
// }

// students.forEach((student)=>console.log(student))


//5.tuple data : it allow user to store multiple multiple type of data in array.
let product:[number,string] = [101,"laptop"]

// 6.enum data : it is use to create constant variable with value
enum days{sun,mon,tue=101,wed,thurs,fri,sat}
let date1 = days.sun;
let date2 = days.mon;

console.log(date1,date2)

//7.union data : it allow user to store multiple type of data in single variable.
let items :string|number = 25645


//8.any data type:when we don't know wat type of data is going to store in variable
let futureData:any = true




