class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first= first
        self.last= last
        self.pay = pay
        self.email = first + "." + last  + "@email.com"


    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay  * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first ,last,pay, prog_lang):
        super().__init__(first,last,pay) #bu komut ile empleyee classımızdaki argumanlara ulasiyoruz
        self.prog_lang = prog_lang
        #Employee.__init__(self,first,last,pay) -----> bu komut ustteki super komutu ile aynı islevi gorur.


class Manager(Employee):
    def __init__(self, first ,last,pay, employees=None):
            super().__init__(first,last,pay)
            if employees is None:
                self.employees = []
            else:
                self.employees = employees

    def add_emps(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())


dev1= Developer("Can","Yetkin","10000","Python")
dev2 = Developer("Baran","Durman","12000","Java")

    
mgr1 = Manager("Begum","Yildirim",20000,[dev1])

print(mgr1.email)

mgr1.add_emps(dev2)
mgr1.remove_emp(dev1)

mgr1.print_emps()    

print(isinstance(mgr1,Manager))
print(issubclass(Manager,Employee))




            







