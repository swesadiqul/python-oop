#Programmer Sadiq
#By@Sadiqul Islam
#Constructors in Python


#Constructors in Python
'''
-Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values)
-to the data members of the class when an object of the class is created. In Python the __init__() method is called
-the constructor and is always called when an object is created.'''

#Syntax of constructor declaration : 

#def __init__(self):
    # body of the constructor

#Types of constructors :
'''
-default constructor: The default constructor is a simple constructor which doesn’t accept any arguments.
-Its definition has only one argument which is a reference to the instance being constructed.
-parameterized constructor: constructor with parameters is known as parameterized constructor.
-The parameterized constructor takes its first argument as a reference to the instance being constructed
-known as self and the rest of the arguments are provided by the programmer.'''

#Example of default constructor :
class Employee:
  def __init__(self):
    self.name = "Sumon Ali"
  
  def display(self):
    print(self.name)
    
ob1 = Employee()
ob1.display()

#Example of the parameterized constructor : 
class Myclass:
  def __init__(self,name,age,city):
    self.name = name
    self.age = age
    self.city = city
    print('Constructor Method Invoked!')
    
    
  def print_data(self):
    print(self.name)
    print(self.age)
    print(self.city)
 

ob1 = Myclass('Suzana',12,'Rangpur')
del ob1

ob1.print_data()
