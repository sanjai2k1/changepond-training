using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
     class Employee
    {
        public int age;
        public string name;
        public int salary;
        public string company;
        private int _empid;
        public int empid
        {
            get { return _empid; }
            set
            {
                if (value > 3999 && value < 5000) {
                _empid = value;

                }
            }
        }
        public Employee() { }
        //public Employee(string name, int age)
        //{
        //    this.name = name;
        //    this.age = age;
        //}
        //public Employee(string name, int age, int salary)
        //{
        //    this.name = name;
        //    this.age = age;
        //    this.salary = salary;
        //}
        //public Employee(string name, int age, int salary, string company)
        //{
        //    this.name = name;
        //    this.age = age;
        //    this.salary = salary;
        //    this.company = company;
        //}

        public void getDetails()
        {
            Console.WriteLine("name : "+name);
            Console.WriteLine("age : " + age);
            if (salary != 0)
            {
                Console.WriteLine("salary : " + salary);
            }
            if (company != null)
            {
                Console.WriteLine("Company : " + company);
            }

        }



    }
}
