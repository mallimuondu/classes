class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def fulldiscription(self):
        return "you have been served by {} {}".format(self.first, self.last)
    
class car:
    def __init__(self,Name,color,price):
        self.Name = Name
        self.color = color
        self.price = price
    
        
        
    def fulldiscription(self):
        return "you have boughat {} {} {}".format(self.Name, self.color, self.price) 
    
    
    
    
class developer(Employee):
    
    def __init__(self,first,last,salary,progaming_languege):
        Employee.__init__(self,first,last,salary)
        self.progaming_languege = progaming_languege
        
dev1 = developer('newton','adams',10000,'python')
dev2 = developer('malli','muondu',1000000,'java')


class maneger(Employee):
    def __init__(self,first,last,salary,employees=None):
        Employee.__init__(self,first,last,salary)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self ,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def printing(self):
        for employee in  self.employees:
            print('-->',employee.fulldiscription())
            
mn1 = maneger('malli','muondu',1000)
mn1.add_emp(dev2)
mn1.printing()


class discription(car):
    def __init__(self,Name,color,price,model=None):
        car.__init__(self,Name,color,price)
        
        if model is None:
            self.model = []
        else:
            self.model = model
            
    def add_mdl(self ,mdl):
        if mdl not in self.model:
            self.model.append(mdl)
            
    def remove_mdl(self,mdl):
        if mdl in self.model:
            self.model.remove(mdl)
            
    def printing(self):
        for car in  self.model:
            print('-->',car.fulldiscription())
            
mn_car = discription('bugati','red',1000000)
print(mn_car.Name)
mn_car.add_mdl(car_1)
mn_car.printing()
#
#    
#employee_1 = Employee('malli','muondu',100000)
#employee_2 = Employee('nesh','muondu',80000)
#employee_3 = Employee('newton','adams',10000)



#print(employee_1.fulldiscription())
    
car_1 = car('bugati1','blue_and_black',10000000)
car_2 = car('bugati2','red_blue',10000000)
#print(car_1.fulldiscription())



#
#class customer:
#    def __init__(self,first,last,Amount_to_pay):
#        self.first = first
#        self.last = last
#        self.Amount_to_pay = Amount_to_pay
#    def fulldiscription(self):
#        return "{} {} has and a price of {}".format(self.first, self.last, self.Amount_to_pay)
#        
#customer1 = customer('Dud','muondu',8000000)
#customer2 = customer('Mum','Mugambi',8100000)
#
#print(customer1.fulldiscription())


     

#print(dev2.progaming_languege)



