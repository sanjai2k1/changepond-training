// use of interface

interface IResult{
    totalMarks()
    percentage();
}

class Students implements IResult{
    phy:number
    che:number
    math:number
    total:number

    constructor(p:number,c:number,m:number){
        this.phy=p
        this.che=c
        this.math=m

    }

    totalMarks(){
         this.total = this.phy+this.che+this.math
    }

    percentage() {
        return (this.total/300)*100
        
    }
    Studentresult(){
        this.totalMarks()
        console.log(`Physics : ${this.phy}, Chemistry : ${this.che}, Math : ${this.math} Total : ${this.total}, Percentage : ${this.percentage()}`)
    }

}




let stdObj = new Students(95,92,99);
stdObj.Studentresult()