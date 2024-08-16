using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class User
    {


        private string username; 
        private string password; 
        private string message;
        private string address;
        private bool isMarried = false;

        public User(string username, string password)
        {
            this.username = username;
            this.password = password;
        }

        public User(string username, string password, string message)
        {
            this.username=username;
            this.password=password;
            this.message = message;
        }

        public User(string username, string password, string message, string address)
        {
            this.username = username;
            this.password = password;
            this.message = message;
            this.address = address;

        }

        public User(string username,string password,string message,string address,bool isMarried)
        {
            this.username = username;
            this.password = password;
            this.message = message;
            this.address = address;
            this.isMarried = isMarried;

        }

        public string getMessage()
        {
            return this.message;
        }

        public void getDetails()
        {
            Console.WriteLine("User Name : " + username);
            Console.WriteLine("Password : " + password);
            if (this.address != null)
            {
                Console.WriteLine("Address : " + this.address);
            }
            Console.WriteLine("Is Married : " + this.isMarried);
        }

        public string CheckLogin()
        {
            if (this.username == "Admin" && this.password == "manager")
            {
                if(this.message == null)
                {
                    this.message = "you are logged in as Admin";
                }
            }
            else if (this.username.StartsWith("User") && this.password == "Password")
            {
                if(this.message == null)
                {
                    this.message = "You are logged in as a normal user";
                }
            }

            else
            {
                if (this.message == null)
                {
                    this.message = "Invalid User";
                }
            }
            return this.message;
        }
    }
}
