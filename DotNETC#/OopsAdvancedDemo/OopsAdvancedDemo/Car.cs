using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OopsAdvancedDemo
{
    abstract class Car
    {
        public string brand;
        public string model;

        public abstract string GetCardDetails();
        //{
        //    return brand + " has this " + model;

        //}

    }
    class BMW : Car
    {
        public string specialFeatures;

        public override string GetCardDetails()
        {
             return this.brand + "is launched a model  "+this.model+ "With new Features " + specialFeatures;
           
        }
    }
    class Mercedez : Car {
        public int mileage;

        public override string GetCardDetails()
        {
            return "";
        }
    }
}
