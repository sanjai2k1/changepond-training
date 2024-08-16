using OopsAdvancedDemo;

internal class Program
{
    private static void Main(string[] args)
    {
        //Person P = new Person() { };
        ////P.FirstName = "Parag";
        ////P.LastName = "Joshi";
        ////P.Gender = "Male";

        ////Console.WriteLine("Name : "+P.FirstName+" "+P.LastName);
        ////Console.WriteLine("Gender : " + P.Gender);
        ////Console.WriteLine();
        //P.DisplayDetails();



        Student student = new Student() {FirstName= "Allen", LastName="Jacob", Gender="Male", StudentId= 1, Marks= 80 };
        //student.FirstName = "Allen";
        //student.LastName = "Jacob";
        //student.Gender = "Male";
        //student.StudentId = 1;
        //student.Marks = 80;
        //Console.WriteLine("Name : "+student.FirstName+" "+student.LastName);
        //Console.WriteLine("Gender : "+student.Gender);
        //Console.WriteLine("ID : " + student.StudentId);
        //Console.WriteLine("Marks : " + student.Marks);
        //Console.WriteLine();
        student.DisplayDetails();
        Employee employee = new Employee() {FirstName= "Prachi",LastName= "Joshi", Gender="Female", EmpId= 1,Salary= 20000 };
        //employee.FirstName = "Prachi";
        //employee.LastName = "Joshi";
        //employee.Gender = "Female";
        //employee.EmpId = 1;
        //employee.Salary = 20000;


        //Console.WriteLine("Name : " + employee.FirstName + " " + employee.LastName);
        //Console.WriteLine("Gender : " + employee.Gender);
        //Console.WriteLine("ID : " + employee.EmpId);
        //Console.WriteLine("Salary : " + employee.Salary);
        //Console.WriteLine();

        employee.DisplayDetails();

        //BMW b = new BMW();
        //   b.brand = "BMW";
        //   b.model = "5-Series";
        //   b.specialFeatures = "Message Seats";
        //   Console.WriteLine(b.GetCardDetails());



        //   Mercedez m = new Mercedez();
        //   m.model = "Mercedez";
        //   m.model = "M-15";
        //   m.mileage = 13;
        //   Console.WriteLine(m.GetCardDetails());  



    }
}