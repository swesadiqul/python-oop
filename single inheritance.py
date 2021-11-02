#Programmer Sadiq
#By@Sadiqul Islam
#Single Inheritance In Python

#First Example
#parent class
class Rabiul:
    def rabiul_self(self):
        print('I am Rabiul Islam')
    
    def power(self):
        print('I have a lot of power.')

#child class
class Suzana(Rabiul):
    def suzana_self(self):
        print('I am Suzana.')

#creation of an object for base/derived class
ob1 = Suzana()
ob1.power()
ob1.suzana_self()


#Second Example

#parent class
class Student:
    #constructor of parent class
    def __init__(self, name, enrollnumber):
        self.name = name
        self.enrollnumber = enrollnumber

    def display(self):
        print(self.name)
        print(self.enrollnumber)

class Collage( Student ):
    def __init__(self, name, enrollnumber, admnyear, branch):
        self.admnyear = admnyear
        self.branch = branch
        #invoking the __init__ of the parent class
        Student.__init__(self, name, enrollnumber)

#creation of an object for base/derived class
obj = Collage('Zamal', 45363237473, 2021, 'CSE' )
obj.display()



#Third Example
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person( object ):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
