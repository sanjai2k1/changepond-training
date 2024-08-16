using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OopsAdvancedDemo
{
    internal class Employee :Person
    {
        public int EmpId {  get; set; }
        public int Salary { get; set; }

     
        //public Employee(string FirstName, string LastName, string Gender, int StudentId, int marks) : base(FirstName, LastName, Gender)
        //{

        //    this.EmpId = StudentId;
        //    this.Salary = marks;
        //}
        public override void DisplayDetails()
        {
            //Console.WriteLine("Employee FirstName : " + base.FirstName);
            //Console.WriteLine("Employee LastName : " + base.LastName);
            //Console.WriteLine("Employee Gender : " + base.Gender);
            Console.WriteLine("Student FirstName : " + base.FirstName);
            Console.WriteLine("Student LastName : " + base.LastName);
            Console.WriteLine("Student Gender : " + base.Gender);
            Console.WriteLine("Student ID : " + this.EmpId);
            Console.WriteLine("Student ID : " + this.Salary);




        }
    }
}
