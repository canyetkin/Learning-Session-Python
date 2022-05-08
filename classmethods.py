import time
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last= last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

        Employee.num_of_emps += 1 

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,float(pay))  #bu satirdaki cls ifadesi class ın kendisine esit, yani Employee yerine geciyor.

"""
        normal methodlarla class in objeleri uzerinde islem yapiyoruz, class methodlarla ise class üzerinde islem yapiyoruz

        class method olustururken ise self yerine cls yaziyoruz
"""
       
        
emp1= Employee("Corey","Schafer",50000)
emp2= Employee("Can","Yetkin",60000)
Employee.set_raise_amt(1.05)

emp_str_1= "Selin-Sumertas-28000"
emp_str_2="Baran-Durman-30000"

new_emp1= Employee.from_string(emp_str_2)

print(new_emp1.email)
print(new_emp1.pay)

new_emp1.set_raise_amt(1.30)

new_emp1.apply_raise()

print(new_emp1.pay)










    
