#calling of class without constractor
'''class Student:#class and classname
    Stu_qualification='m.tech'#variable
    def stu_detail(name,age):#method
        print("enter student name:")
        print("enter student age")
        print("stu.qualification:",Student.Stu_qualification)
obj=Student
obj.stu_detail("SANCHITA",23)'''
#with constractor
'''class Student:
    Stu_qualification='m.tech'
    def __init__(self):#magic ,dunder,speacial method constractor auto call ho jata h __init use karne par ye constractor ka body h
        print("constactor called")
obj=Student()#responcibal for constractor call
print(obj)'''
#==============variable======================>
#three type instance,static,local variable
#instance variable---variable ko object  badlna ke sath  me value badal de jaye to usko instance variable kahte h
#AGAR INSTANCE LO CALL KARNA H TO CLASS KE SELF PASS KARNA PADEGA   QKI SELF KE PASS HI USKA REFRENCE HOLD HOGA OR BAHAR OJECT KE THROW
'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("self name")
        print("self age")
        print(obj.name)
        print(obj.age)
obj=student("sanchita",22)
obj.display()'''
#static variable 
'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def school(self):
        
    def display(self):
        print("self name")
        print("self age")
        print(obj.name)
        print(obj.age)
obj=student("sanchita",22)
obj.display()'''

#object ke upar dependt nhi karta static kahlata h
#combine variable
#instance methoad ko class ,using constractor
#how to declare instance variable
'''class student:
    quali="m.tech"#static variable
    def __init__(self,name):
        self.name=name
    def display(self):
        age=37
        print("name=",self.name)
        print("age=",age)
        print("quali=",student.quali)
obj=student("sanchita")
obj.display()'''
#instance methoda --jinka pahla parameter self hoga instance method kahte h
#throught instance method
'''class student:
    def display(self,name):
        self.name=name
    def show(self):
        print("name=",self.name)
obj=student()
obj.display("sanchita")
obj.show()'''
#through object
'''class student:
    def __init__(self,name):
        self.name=name#throught constractor
    def display(self,age):
        self.age=age#throught instance method
    def show(self):
        print("name=",self.name)
        print("age=",self.age)
        print("quali=",self.quali)
obj=student("sanchita")
obj.display(55)
obj.quali="bsc"#throught object
obj.show()'''
# how we acces instance variable
#1.inside the class
#2.outside the class
#static variable
'''class Student:
    quali = "M.Tech"   # static variable declare inside the class   
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.school = "SHSS"  # static variable declare inside the constructor
    def display(self):
        Student.gread = "P.hd"   # static variable declare inside the instence variable
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Quali =",Student.quali)  # static variable access inside the class through class name
        print("School = ",Student.school) # static variable access inside the class through class name
        print("Gread = ",Student.gread) # static variable access inside the class through class name
        print("Achivment = ",Student.achivment)   # static variable access inside the class through class name

obj=Student("Neeraj",37)
Student.achivment="Gate-qualified"   # static variable declare outside of the class
print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name
print("Access through object = ",obj.quali) # static variable access outside the class through object
obj.display()
print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name
print("Access through class_Name = ",Student.school)# static variable access outside the class through class name
print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# obj.display()'''
#local variable access karne ke two tarike
'''class student:
    def display(self):
        global a
        a=10
        print("value of a=",a)
    def show(self):
        print("value of a=",a)
    def new():
            print("valus of a=",a)
obj=student()
obj.display()
obj.show()
student.new()'''
# instance method
'''class student:
    def display(self,name):
        self.name=name
        print("name=",self.name)
    def show(self,age):
        self.age=age
        self.display("rahul")
        print("age=",self.age)
obj=student()
obj.display("sanchita")
obj.show(32)
#student.display("savu")'''
#class method
'''class Book:
    price=1000
    def book_detail(self,name,author):
        self.name=name
        self.author=author
    @classmethod
    def update_price(cls,price):
        cls.price=price
    def show_detail(self,page):
        self.page=page
        print("book_page=",self.page)
        print("book_name=",self.name)
        print("book_author=",self.author)
        print("book_price=",Book.price)
obj=Book()
obj.book_detail("python","sanchita")
obj.update_price(2000)
obj.show_detail(1000)'''
#static method
'''class Student:
    @staticmethod
    def great():
        print("thank u for visit")
    def great1(self):
        print('welcome again')
obj=Student()
obj.great()
Student.great()
#Student.great1()
obj.great1()
#Student.great1()'''
'''def my_fun(x, y):
    while x<=y:
        yield x
        x+=1
var= my_fun(5, 10)
print("object from generator :",next(var))
print("object from generator :",next(var))
print("object from generator :",next(var))
print("object from generator :",next(var))
print("object from generator :",next(var))'''
#single inheritance
'''class A:
    name="sanchita"
    def M1(self):
        return"this is m1 method"
class B(A):
    def m2(self):
        print("name=",A.name)
        print("M1=",self.M1())
obj=B()
obj.m2()'''
#multilevel inheritance
'''class A:
    name="sanchita"
    def M1(self):
        return"this is m1 method"
class B(A):
    age=37
    def m2(self):
        print("name=",A.name)
        print("M1=",self.M1())
class C(B):
    def m3(self):
        print("Age=",B.age)
        self.m2()
obj=C()   
obj.m3()'''
#multipal inheritance
#mro method resolution order
'''class parent1:
    def m1(self):
        print("parent1 methodcalled")
class parent2:
    def m1(self):
        print("parent2 method called")
class child(parent1,parent2):
    def m2(self):
        self.m1()
obj=child()
obj.m2()'''
'''class parent1:
    def m1(self):
        print("parent1 method called")
class parent2:
    def m2(self):
        print("parent2 method called")
class child(parent1,parent2):
    def m3(self):
        self.m1()
        self.m2()
obj=child()
obj.m3()'''
#super method --inheit for parent class and child class same hoto  
# variable ya method ka name same hoto super method use karte h ISKO HI OVERRIDE METHOD KAHTE H
'''class A:
    def m1(self):
        print("m1 called from a")
class B:
    def m1(self):
        print("m1 called from b")
obj=B()
obj.m1()'''
#polimorphism
#
#yak hi class ke same type ke method ke andar parameter alag hoto isko overloading
'''class A:
    def new(self,a,b):
        return a+b
    def new(self,x,y,z):
        return x+y+z
obj=A()
obj.new(3,4,5)
print(obj.new(5,6,7))
obj.new(4,5)'''
'''class A:
    def new(self,x=0,y=0,z=0):
        return x+y+z
        
obj=A()
print(obj.new(5,6))
print(obj.new(5,6,7))
print(obj.new(6))
print(obj.new())'''
#python overloading support nhi karta overloading support karne ke liye dispatch  moudeln nam ka intall karna padta h
'''from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def add(self,x,y):
        print(x+y)
    @dispatch(int,int,int)
    def add(self,x,y,z):
        print(x+y+z)
obj=A()
obj.add(4,6)
obj.add(4,5,6)'''
#overriding












