import datetime
today=datetime.date.today()
year=today.year

class Company:
    area = "SIPCOT,Siruseri"
    __city = "Chennai"
    def __init__(self,cname):
        self._cname=cname
    def displayCname(self):
        print("company name : ",self._cname)
    def address(self):
        return self.area +" , "+self.__city+", TAmilNadu"

class Employee:
    empcount=0
    isMarried=False
    def __init__(self,fname,lname,yob):
        self._fname=fname
        self._lname=lname
        self.__age=year-yob
        Employee.empcount+=1
        self.__id=self.empcount
        self._address="hia"    
    def getEmpDetails(self):
        print("EMp id : ",self.__id)
        print("FullName : ",self._fname," ",self._lname)
        print("Age : ",self.__age,"years")
        print("martial status : ",self.isMarried)
    def address(self):
        print('address : ',super().address())
        return self._address
        

c1 = Company("Changepond technologies")
c1.displayCname()
c1.__city="Pune"
print(c1.__city)
print("Address: ",c1.address())

print("*"*70)

e1 = Employee("Parag","Joshi",1980)
e1.isMarried=True
e1.getEmpDetails()
print("*"*70)