using GenericsDemo;
using System.Collections;
using System.Net.Http.Headers;

internal class Program
{
    private static void Main(string[] args)
    {
        //string[] weekdays = { "Sun",  "Tue", "Mon", "Wed", "Thu", "Fri", "Sat" };
        //Array.Reverse(weekdays);

        //foreach (string day in weekdays)
        //{
        //    Console.WriteLine(day);
        //}
        ////Console.WriteLine(weekdays[1]);
        //Console.WriteLine(weekdays.Length);
        ///* for (int i = 0; i < weekdays.Length; i++)
        // {
        //     Console.WriteLine(weekdays[i]);
        // }
        //*/



        //foreach (string day in weekdays)
        //{
        //    Console.WriteLine(day);
        //}


        ///*Array.Sort(weekdays);

        //Console.WriteLine("Sorted in Ascending");

        //foreach (string day in weekdays )
        //{
        //    Console.WriteLine(day);
        //}

        //Array.Reverse(weekdays);

        //Console.WriteLine("Sorted in Descending ");

        //foreach (string day in weekdays)
        //{
        //    Console.WriteLine(day);
        //}
        //*/
        //int daypos = Array.IndexOf(weekdays, "Wed");

        //Console.WriteLine("Wednesday is " + (daypos + 1) + " day of week ");

        //Array.Clear(weekdays, 0, 2);

        //weekdays[0] = "Sunday";
        //Array.Resize(ref weekdays, 7);
        //weekdays[6] = "Some Special Day";

        //string[] weekdays_copy = new string[7];
        ////weekdays.Append("independance day");
        //weekdays.CopyTo(weekdays_copy, 0);

        //foreach (string day in weekdays_copy)
        //{
        //    Console.WriteLine(day);
        //}


        //List<string> products = new List<string>() {"Butter","Bread","Milk","Cheese" };

        //foreach(string product in products)
        //    Console.WriteLine(product);

        //char flag = 'Y';
        //string item;
        //while (flag == 'Y' || flag == 'y')
        //{
        //    Console.WriteLine("Enter the Product to Add : ");
        //    item = Console.ReadLine();
        //    products.Add(item);
        //    Console.Write("Want to add mpre products press Y : ");
        //    flag = Console.ReadLine()[0];
        //}
        //Console.WriteLine("Products List add at start");
        //item = Console.ReadLine();
        //products.Insert(0, item);

        //List <string> fruits = new List<string>() {"Apple","Kiwi","Banana" };

        //products.AddRange(fruits);

        //Console.WriteLine("Products List");
        //foreach (string product in products)
        //    Console.WriteLine(product);

        ////Console.WriteLine(products);

        //Console.WriteLine("Which item to Remove : ");
        //item = Console.ReadLine();
        //products.Remove(item);
        //foreach (string product in products)
        //    Console.WriteLine(product);





        //List <string> products = new List<string>();
        //List<int> prices = new List<int>();

        //while (true)
        //{
        //    Console.WriteLine("Add product Name : ");
        //    string productName = Console.ReadLine();
        //    Console.WriteLine("Add product Price : ");
        //    int productPrice = int.Parse(Console.ReadLine());
        //    Console.WriteLine("do you want to continue ? y / n");
        //    products.Add(productName);
        //    prices.Add(productPrice);
        //    char choice = Console.ReadLine()[0];
        //    if (choice != 'y')
        //    {
        //        break;
        //    }

        //}
        //while (true) {
        //    Console.WriteLine("What do you want to do next ? ");
        //    Console.WriteLine("1. Update \n2.Remove \n3.Show the e list\n4.Exit");
        //    int choice = int.Parse(Console.ReadLine());

        //    if (choice == 1)
        //    {
        //        Console.WriteLine("Which value you want to Update ?");
        //        Console.WriteLine("enter 0" + "-" + (products.Count()-1));
        //        int index = int.Parse(Console.ReadLine());
        //        Console.WriteLine("Enter item to be Updated : ");
        //        string updatename = Console.ReadLine();
        //        int updateprice = int.Parse(Console.ReadLine());
        //        products.RemoveAt(index);
        //        prices.RemoveAt(index);
        //        products.Insert(index, updatename);
        //        prices.Insert(index, updateprice);
        //    }
        //    else if (choice == 2)
        //    {
        //        Console.WriteLine("Which value you want to remove");
        //        string item = Console.ReadLine();
        //        if (products.Contains(item))
        //        {
        //            int index = products.IndexOf(item);
        //            products.RemoveAt(index);
        //            prices.RemoveAt(index);
        //        }
        //        else
        //        {
        //            Console.WriteLine("element not in list...");
        //        }
        //    }
        //    else if (choice == 3)
        //    {

        //        Console.WriteLine("List of Items :");
        //        for (int i = 0; i < products.Count; i++)
        //        {
        //            Console.WriteLine(products[i] + "  " + prices[i]);
        //        }
        //    }
        //    else
        //    {
        //        break;
        //    }

        //};




        //List<string> list = new List<string> { "cheese", "butter", "tea", "jam", };
        //Console.WriteLine(list);
        //foreach (var items in list)
        //{
        //    Console.WriteLine(items);
        //}
        //string flag = "y";
        //string item = "";
        //while (flag == "y" || flag == "y") 
        //{
        //    Console.WriteLine("enter the list to add:");
        //    item = Console.ReadLine();
        //    list.Add(item);
        //    Console.WriteLine("want to add more list:");
        //    flag = Console.ReadLine();

        //}
        //Console.WriteLine("enter the list to add to start:");
        //item = Console.ReadLine();
        //list.Insert(0, item);
        //Console.WriteLine("want to add items");
        //foreach (string lists in list) 
        //{
        //    Console.WriteLine(list);
        //}
        //List<string> vege = new List<string>() { "carrot", "beans", "onion", "tomato", "brinjal" };
        //Console.WriteLine(vege);
        //foreach (var items in vege)
        //{
        //    Console.WriteLine("Do you want to clear the list before adding the fruit list");
        //}
        //flag = Console.ReadLine();
        //if (flag == "Y" || flag == "y") 
        //{
        //    list.AddRange(vege);
        //    Console.WriteLine("products list in vege");
        //}
        //foreach (string product in vege)

        //{
        //    Console.WriteLine("product");
        //}
        //Console.WriteLine("which item want to remove");
        //item = Console.ReadLine();
        //vege.Remove(item);
        //Console.WriteLine("List after removing the item: " + item);
        //foreach (string product in vege) 
        //{
        //    Console.Write("Which position item to be removed: ");
        //    int pos = Convert.ToInt32(Console.ReadLine());
        //    Console.WriteLine("List after removing the item at position : " + pos);
        //    vege.RemoveAt(pos);
        //}

        //List<int> ints = new List<int> {10,15,32,49,25,33,22,66,89 };
        //List<int> evenlist = new List<int>();

        //evenlist = (from items in ints where(items%2==0) select items).ToList();

        //foreach(int i in evenlist)
        //    Console.WriteLine(i);

        //List<string> list = new List<string> { "cheese", "butter", "tea", "jam", };
        //Console.WriteLine("Enter product to find");
        //string match = Console.ReadLine();
        //List<string> ans = (from item in list where item.Equals(match) select item ).ToList();
        //if(ans.Count == 1)
        //{
        //    Console.WriteLine("available");
        //}
        //else
        //{
        //    Console.WriteLine("not available");
        //}

        //Product p1, p2, p3;
        //p1=new Product()
        //{
        //    Id = 1,
        //    Name="Shirts",
        //    Price = 250
        //};
        //p2 = new Product()
        //{
        //    Id = 1,
        //    Name = "T-Shirts",
        //    Price = 301
        //};
        //p3 = new Product()
        //{
        //    Id = 1,
        //    Name = "V-Neck T-Shirts",
        //    Price = 310
        //};
        //List<Product> products = new List<Product>() { p1, p2 ,p3};
        //List<Product> cartList = new List<Product>() ;

        //for (int i = 0; i < products.Count; i++)
        //{
        //    Product product = products[i];
        //    if (product.Price > 300)
        //    {
        //        cartList.Add(product);
        //    }
        //}


        //for (int i = 0; i < cartList.Count; i++)
        //{
        //    Product product = cartList[i];
        //        Console.WriteLine(product.Name+" " +product.Price);

        //}

        //foreach(Product product in products) {
        //    Console.WriteLine(product.Id+" " +product.Name + " " + product.Price);
        //}


        Dictionary<int, string> empdetails = new Dictionary<int, string>();
        empdetails.Add(100, "Parag");
        empdetails.Add(102, "Prachi");
        empdetails.Add(103, "Mans");
        empdetails.Remove(100);

        foreach (int key in empdetails.Keys)
        {
            Console.WriteLine(key + " " + empdetails[key]);
        }
        Console.WriteLine(empdetails.ContainsKey(102));
        //Dictionary<int, string> check = new Dictionary<int, string>();
        //check.Add(500, "orange");

        Console.WriteLine(empdetails.Values);

        string ename = empdetails[102];

        Console.WriteLine(ename);

        empdetails.Clear();

        SortedList<string, int> marks;
        marks = new SortedList<string, int>();
        
        marks.Add("Maths", 80);
        marks.Add("Physics", 90);
        marks.Add("Chemistry", 75);
        

        foreach (string key in marks.Keys)
        {
            Console.WriteLine(key+" "+marks[key]);
        }

        








    }
}