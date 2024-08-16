using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class MathOperation
    {
        private int num1;
        private int num2;

        public MathOperation(int num1, int num2)
        {
            this.num1 = num1;
            this.num2 = num2;
        }

        private int addition()
        {
            return num1+num2;
        }

        private int subtraction()
        {
            return num1 - num2;
        }

        private int multiplication()
        {
            return num1 * num2;
        }

        private int division()
        {
            return num1 / num2;
        }
        
        public void displayOperations()
        {
            Console.WriteLine(this.num1 + "  +  " + this.num2+" = "+this.addition());
            Console.WriteLine(this.num1 + "  -  " + this.num2+" = "+ this.subtraction());
            Console.WriteLine(this.num1 + "  *  " + this.num2 + " = "+ this.multiplication());
            Console.WriteLine(this.num1 + "  /  " + this.num2 + " = "+ this.division());

        }

    }
}
