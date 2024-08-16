using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterfaceTask
{
    class Shop : IProduct, IOutlet
    {

        public string Shopname;

        public string ProductName { get ; set ; }
        public string ProductPrice { get ; set ; }
        public string ProductCategory { get ; set ; }
        public string OutletName { get ; set ; }
        public string  OutletCity { get ; set ; }
        public string  OutletLocation { get ; set ; }

        public void GetOutletDetails()
        {

            Console.WriteLine("----------- O U T L E T --------------");
            Console.WriteLine(this.OutletName);
            Console.WriteLine(this.OutletCity);
            Console.WriteLine(this.OutletLocation);

        }

        public void GetProductDetails()
        {

            Console.WriteLine("----------- P R O D U C T S --------------");
            Console.WriteLine(this.ProductName);
            Console.WriteLine(this.ProductPrice);
            Console.WriteLine(this.ProductCategory);

        }
    }
}
