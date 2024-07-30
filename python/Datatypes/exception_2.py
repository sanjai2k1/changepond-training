import datetime
today = datetime.date.today()
year=datetime.datetime.now().year
# try :
#     num1 = int(input("enter number 1 : "))
#     num2 = int(input("enter the number 2 : "))
#     result = num1/num2
#     print(result)
#     items=["Bread","Butter","jam","cheese"]
#     items[len(items)]="spread"
#     num1=int(input("enter num 1 : "))
#     assert num1%2==0
# except ZeroDivisionError:
#     print("Error : Denominator cannot be Zero")
# except ValueError:
#     print("Only number are allowed")
# except IndexError:
#     print("Kindly insert or append method")
# except AssertionError:
#     print("Entered value is not matching the test condition")
# else:
#     print(num1,"is even")
# finally:
#     print("Program is over")
    
yob = int(input("Enter your year of birth "))
age= year-yob

if (age<18):
    raise Exception(f'The age sholud be greate than 18')