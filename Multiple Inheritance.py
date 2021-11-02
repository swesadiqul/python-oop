#Programmer Sadiq
#By@Sadiqul Islam
#Multiple Inheritance In Python


#First Example

#parent class
class Student( object ):
    #constructor of parent class
    def __init__(self, name, enrollnumber):
        self.name =name
        self.enrollnumber = enrollnumber

    def display(self):
        print(self.name)
        print(self.enrollnumber)

#child class
class Collage( Student ):
    def __init__(self, name, enrollnumber, admnyear, branch):
        self.admnyear = admnyear
        self.branch = branch
        #invoking the __init__ of the parent class
        Student.__init__(self, name, enrollnumber)

#child class
class University( Student ):
    def __init__(self, name, enrollnumber, refno, branch):
        self.refno = refno
        self.branch = branch
        #invoking the __init__ of the parent class
        Student.__init__(self, name, enrollnumber)

#creation of an object for base/derived class
obj_1 = Collage('Sumon', 464667336, 2021, 'AIDT')
obj_1.display()

obj_2 = University('Rohim', 353553973, 'st2021', 'CSE')
obj_2.display()


#Second Example
# Python example to show the working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "First-1"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Second-2"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)
		

ob = Derived()
ob.printStrs()




        
