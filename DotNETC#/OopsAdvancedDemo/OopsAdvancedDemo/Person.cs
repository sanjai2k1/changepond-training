using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OopsAdvancedDemo
{
    internal abstract class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public string Gender { get; set; }


        //public Person (string firstName, string lastName,string gender)
        //{
        //    FirstName = firstName;
        //    LastName = lastName;
        //    Gender = gender;
        //}
        public abstract void DisplayDetails();
    }
}
