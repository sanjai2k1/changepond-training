using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterfaceTask
{
    internal interface IProduct
    {
        public string ProductName { get; set; }
        public string ProductPrice { get; set; }

        public string ProductCategory { get; set; }

        public void GetProductDetails();
    }
}
