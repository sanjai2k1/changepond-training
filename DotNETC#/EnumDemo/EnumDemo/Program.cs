//using System.Security.Cryptography;

//enum PaymentOptions
//{
//    CreditCard, DebitCard, NetBanking, Wallet
//}
//class Payment
//{
//    public string invoicename { get; set; }
//    public PaymentOptions options;
//    public static int noofpayments, creditcard, debitcard, netbanking;
//    static Payment()
//    {
//        noofpayments = 0;
//        creditcard = 0;
//        netbanking = 0;
//        debitcard = 0;
//    }
//    public Payment()
//    {
//        noofpayments += 1;
//    }
//    public void getPayementOptionWiseCount()
//    {
//        if (this.options == PaymentOptions.CreditCard)
//        {
//            creditcard += 1;
//        }
//        else if (this.options == PaymentOptions.DebitCard)
//        {
//            debitcard += 1;
//        }
//        else if (this.options == PaymentOptions.NetBanking)
//        {
//            netbanking += 1;
//        }
//    }
//    //public override string ToString()
//    //{
//    //    System.Console.WriteLine(base.GetHashCode());
//    //    return "Class1.ToString";
//    //}


//    internal class Program
//{
//    private static void Main(string[] args)
//    {
//            //Console.WriteLine("Hello, World!");
//            //    Payment payment = new Payment();
//            //    payment.invoivename = "BroadBandBill";
//            //    payment.options =  PaymentOptions.CreditCard;
//            //int ans = (int) PaymentOptions.Wallet;
//            //Console.WriteLine(ans);
//            //    Console.WriteLine(payment.invoivename + " is paid by "+payment.options);
//            //    payment.invoivename = "AmazonShopping";
//            //    payment.options =  PaymentOptions.Wallet;
//            //    Console.WriteLine(payment.invoivename + " is paid by " + payment.options);

//            //Payment p1, p2;
//            //p1 = new Payment();
//            //p2 = new Payment();


//            //bool b = p1.Equals(p2);

//            //Console.WriteLine(b);

//            //int t1 = p1.GetHashCode();
//            //Console.WriteLine(t1);

//            //string c = t1.ToString();
//            //Console.WriteLine(c);

//            //Console.WriteLine(p1);
//            //int lucky_number = 100;
//            //Object obj;
//            //obj = lucky_number;
//            //Object obj1 = 100;
//            //Console.WriteLine(obj1.GetType());
//            //int num = Convert.ToInt32(obj);
//            //Console.WriteLine(num.GetType());

//            Payment p = new Payment();
//            p.invoicename = "BroadBandBill";
//            p.options = PaymentOptions.CreditCard;
//            p.getPayementOptionWiseCount();
//            Console.WriteLine(p.invoicename + " is paid by " + p.options);
//            Payment p1 = new Payment();
//            p1.invoicename = "AmazonShopping";
//            p1.options = PaymentOptions.DebitCard;
//            p1.getPayementOptionWiseCount();
//            Console.WriteLine(p1.invoicename + " is paid by " + p1.options);
//            Payment p2 = new Payment();
//            p2.invoicename = "AmazonShopping - 1";
//            p2.options = PaymentOptions.NetBanking;
//            p2.getPayementOptionWiseCount();
//            Console.WriteLine(p1.invoicename + " is paid by " + p2.options);
//            Console.WriteLine("No of Payment recieved: " + Payment.noofpayments);
//            Console.WriteLine("No of times Credit Card Used: " + Payment.creditcard);
//            Console.WriteLine("No of times Debit Card Used: " + Payment.debitcard);
//            Console.WriteLine("No of times Net Banking  Used: " + Payment.netbanking);
//        }

//    //public override string tostring()
//    //{
//    //    console.writeline(base.gethashcode());
//    //    return "p01p.tostring";
//    //}

//    public override string ToString()
//    {
//        System.Console.WriteLine(base.GetHashCode());
//        return "ToString";
//    }






//}





enum PaymentOptions

{

    CreditCard, DebitCard, NetBanking, Wallet

}

class Profile<T1, T2>
{
    public T1 Gender;
    public T2 isAdult;
}

class Payment

{

    public string invoicename { get; set; }

    public PaymentOptions options;

    public static int noofpayments, paymentoptionscountC;

    static Payment()

    {

        noofpayments = 0;

        paymentoptionscountC = 0;

    }

    public Payment()

    {

        noofpayments += 1;

    }

    public void getPayementOptionWiseCount()

    {

        if (this.options == PaymentOptions.CreditCard)

        {

            paymentoptionscountC += 1;

        }

    }

    public override string ToString()

    {

        System.Console.WriteLine(base.GetHashCode());

        return "Class1.ToString";

    }

}

class Program

{

    private static void Main(string[] args)

    {

        Profile<string, bool> profile;
        profile = new Profile<string, bool>();
        profile.Gender = "Male";
        profile.isAdult = true;
        Console.WriteLine("Gender: " + profile.Gender);
        Console.WriteLine("Is Adult: " + profile.isAdult);
        Profile<int, int> profile1;
        profile1 = new Profile<int, int>();
        profile1.Gender = 0;
        profile1.isAdult = 0;
        string gender = profile1.Gender == 1 ? "Female" : "Male";
        Console.WriteLine("Gender: " + gender);

        Payment p = new Payment();

        p.invoicename = "BroadBandBill";

        p.options = PaymentOptions.CreditCard;

        p.getPayementOptionWiseCount();

        Console.WriteLine(p.invoicename + " is paid by " + p.options);

        Payment p1 = new Payment();

        p1.invoicename = "AmazonShopping";

        p1.options = PaymentOptions.Wallet;

        p1.getPayementOptionWiseCount();

        Console.WriteLine(p1.invoicename + " is paid by " + p1.options);

        Payment p2 = new Payment();

        p2.invoicename = "AmazonShopping - 1";

        p2.options = PaymentOptions.NetBanking;

        p2.getPayementOptionWiseCount();

        Console.WriteLine(p1.invoicename + " is paid by " + p2.options);

        Console.WriteLine("No of Payment recieved: " + Payment.noofpayments);

        Console.WriteLine("No of times Credit Card Used: " + Payment.paymentoptionscountC);

    }

}