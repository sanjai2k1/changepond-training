using InterfaceTask;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Ennter Shop Name: ");
        string sn = Console.ReadLine();

        Console.WriteLine("Enter Product Name : ");
        string pn = Console.ReadLine();
        Console.WriteLine("Enter Product Price");
        string pp = Console.ReadLine();

        Console.WriteLine("Enter Product Category");
        string pc = Console.ReadLine();

        Console.WriteLine("Enter Outlet Name : ");
        string on = Console.ReadLine();

        Console.WriteLine("Enter Outlet City : ");
        string oc = Console.ReadLine();

        Console.WriteLine("Enter Outlet Location : ");
        string ol = Console.ReadLine();


        Shop shop = new Shop() {Shopname=sn, ProductName = pn,ProductPrice=pp,ProductCategory=pc,OutletName=on,OutletCity=oc,OutletLocation=ol};
        Console.WriteLine(shop.Shopname);

        shop.GetProductDetails();
        shop.GetOutletDetails();






    }
}