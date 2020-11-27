class Employee:

    raise_amount = 9.7
    num=0
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.pay=pay
        # self.email=firstname+lastname+"@companyname.com"

        Employee.num +=1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstname,self.lastname)

    @property
    def full_name(self):
        return '{} {}'.format(self.firstname,self.lastname)

    @full_name.setter
    def full_name(self,name):
        first,last=name.split(' ')
        self.firstname=first
        self.lastname=last




    def payraise(self):
        self.pay = self.pay * self.raise_amount

    def notaraise(self):
        self.pay=self.pay-self.raise_amount



class Developer(Employee):
    raise_amount=2.4
    def __init__(self,firstname,lastname,pay,proglang):
        super().__init__(firstname,lastname,pay)
        self.proglang=proglang


class Manager(Employee):
    def __init__(self,firstname,lastname,pay,employee=None):
        super().__init__(firstname,lastname,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(sef,employee):
        if emp not in self.employee:
            self.employees.append(emp)

    def rem_emp(sef,employee):
        if emp in self.employee:
            self.employees.remove(emp)

    def print_emp(sef,employee):
        for employee in self.employee:
            print('--->'.emp.full_name())
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.firstname,self.lastname,self.pay)
    def __str__(self):
        return "{}-{}".format(self.fullname,self.email)
    def __add__(self,other):
        self.pay=self.pay+other.pay
    def __len__(self):
        return len(self.full_name())







e1=Employee('yes','bos',5000)
e2=Employee('NO','BOSS',9000)
e1.firstname
e1.lastname
e1.full_name()

Employee.full_name(e1)
e1.email
e1.pay
print(Employee.__dict__)
e1.same_one()

print(Employee.payraise(e1))

e1.notaraise()


e2.firstname
e2.full_name()
e2.email
e2.pay

e2.payraise()

print(e2.same_one())
Employee.num

dev1=Developer('abhilash','kumar',7000)
dev2=Developer('Ravi','kumar',8000)

print(dev1.email)

print(help(Developer))

e3=Developer('abhi','panda',7000,'java')

e3.proglang

mgr1=Manager('sam','jamson',90000,[dev1])

mgr1.email

isinstance(mgr1,Employee) #as manager inherits from Empployee
isinstance(mgr1,Manager)#as mag1 is instance of Manager
issubclass(Manager,Employee)
issubclass(Manager,Developer)

str(e2)
print(repr(e1))

print(e2)

len(e1)

add(e1+e2)

e1.firstname='ram'
e1.email()

e1.email

e1.full_name="abhilash panda"

e1.firstname
