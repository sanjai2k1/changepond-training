using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterfaceTask
{
    internal interface IOutlet
    {
        public string OutletName { get; set; }
        public string OutletCity { get; set; }
        public string OutletLocation { get; set; }

        public void GetOutletDetails();
    }
}
