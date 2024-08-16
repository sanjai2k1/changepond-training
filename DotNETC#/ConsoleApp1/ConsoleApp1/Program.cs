using ConsoleApp1;
using System.Formats.Asn1;
using System.Net.Cache;
public class Age
{
    readonly int _year=100;
    public Age(int year)
    {
        _year = year;
    }
    public void getAge()
    {

        Console.WriteLine(this._year);
    }
}
internal class Program
{
    public const double pi = 3.14;
  
    class Calculation
    {
        public const double pi = 3.14;
        public readonly double area;

        public double calcaoc(int radius)
        {
            const double pi = Math.PI;

            return area;
    }
       
}
    private static void Main(string[] args)
    {
        //Student s1, s2;
        //s1 = new Student();
        //s2 = new Student();


        //Student.collegename = "JSPM";

        //s1.studentid = 1;
        //s1.studentname = "sanjai j";
        //s1.marks = 80;

        //s2.studentid = 2;
        //s2.studentname = "sanjai j 2 ";
        //s2.marks = 90;


        //Console.WriteLine("Student ID : "+s1.studentid);
        //Console.WriteLine("Student Name : " + s1.studentname);
        //Console.WriteLine("Student marks : " + s1.marks);


        //Console.WriteLine("Student ID : " + s2.studentid);
        //Console.WriteLine("Student Name : " + s2.studentname);
        //Console.WriteLine("Student marks : " + s2.marks);

        //Employee e1;
        //Employee.company = "Changepond";
        //e1 = new Employee();
        //e1.name = "sanjai j";
        //e1.age = 22;
        //e1.salary = 20000;


        //Console.WriteLine("Employee name: " + e1.name);
        //Console.WriteLine("Employee salary : " + e1.salary);
        //Console.WriteLine("Employee age: " + e1.age);
        //Console.WriteLine("Employee age: " + Employee.company);

        //Age age = new Age(2001);
        //age.getAge();

        //User u1, u2, u3,u4,u5;
        //string result;
        //u1 = new User("Admin", "Manager");
        //u1.getDetails();
        //result = u1.CheckLogin();
        //Console.WriteLine(result);
        //u2 = new User("Pankaj", "kalra", "Guest User");
        //u2.getDetails();
        //result = u2.CheckLogin();
        //Console.WriteLine(result);
        //u3 = new User("Admin", "Manager", "Guest User", "Nagpur");
        //u3.getDetails();
        //result = u3.CheckLogin();
        //Console.WriteLine(result);
        //u4 = new User("Admin", "Manager");
        //u4.getDetails();
        //result = u4.CheckLogin();
        //Console.WriteLine(result);



        //Console.Write("Enter username : ");
        //string uname = Console.ReadLine();
        //Console.Write("Enter Password : ");
        //string password = Console.ReadLine();
        //u1 = new User(uname, password);
        //Console.WriteLine(u1.CheckLogin());

        //MathOperation m = new MathOperation(10,20);
        //m.displayOperations();


        Employee emp1, emp2, emp3;
        Console.WriteLine("Enter Name : ");
        string empname = Console.ReadLine();
        Console.WriteLine("Enter age : ");
        int empage = int.Parse(Console.ReadLine());
        emp1 = new Employee() { name = empname, age = empage };
        emp1.empid = 4444;
        emp1.getDetails();
        Console.WriteLine("Employee ID : "+emp1.empid);
        Console.WriteLine("Enter salary : ");
        int empsalary = int.Parse(Console.ReadLine());
        emp2 = new Employee(){name= empname,age= empage,salary=empsalary};
        emp2.getDetails();
        Console.WriteLine("Enter Company : ");
        string empcompany = Console.ReadLine();
        emp3 = new Employee() { name = empname, age = empage, salary = empsalary ,company = empcompany};
        emp3.getDetails();













    }
}