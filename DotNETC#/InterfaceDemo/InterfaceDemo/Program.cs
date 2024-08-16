using InterfaceDemo;

internal class Program
{
    private static void Main(string[] args)
    {
        Company c = new Company();
        c.Name = "ChangePond Technologies";
        c.addressline1 = "SIPCOT,Siruseri";
        c.city = "Chennai";
        c.state = "Tamil Nadu";
        c.postcode = 60073;
        c.email = "contact@cp.com";
        c.mobile = 987654321;
        c.addressDetails();
        c.ContactDetails();

        Employee e = new Employee();
        e.EmpName = "Nirmal Raj S";
        e.addressline1 = "SIPCOT,Siruseri";
        e.city = "Chennai";
        e.state = "Tamil Nadu";
        e.postcode = 60073;
        e.email = "contact@cp.com";
        e.mobile = 987654321;
        e.AddressDetails();
        e.ContactDetails();
    }
}