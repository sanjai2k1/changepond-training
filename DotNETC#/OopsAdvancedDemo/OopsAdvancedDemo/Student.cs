using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OopsAdvancedDemo
{
    internal class Student : Person
    {
        public int StudentId {  get; set; }
        public int Marks { get; set; }

        //public Student(string FirstName,string LastName,string Gender,int StudentId,int marks) : base(FirstName,LastName,Gender)
        //{

        //    this.StudentId = StudentId;
        //    this.Marks = marks;
        //}

        public override void DisplayDetails()
        {
            //Console.WriteLine("Student FirstName : "+base.FirstName);
            //Console.WriteLine("Student LastName : " + base.LastName);
            //Console.WriteLine("Student Gender : " + base.Gender);
            Console.WriteLine("Student FirstName : " + base.FirstName);
            Console.WriteLine("Student LastName : " + base.LastName);
            Console.WriteLine("Student Gender : " + base.Gender);
            Console.WriteLine("Student ID : " + this.StudentId);
            Console.WriteLine("Student ID : " + this.Marks);

        }

    }
}
