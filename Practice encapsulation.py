class Person:

    def __init__(self):
        self.name = 'Samiul Islam'
        self._age = 23
        self.__salary = '40,000 Tk(Only)'

    def get_salary(self):
        self.__salary = 50000


    def show_person(self):
        print(self.name,self._age,self.__salary)


class Najma(Person):

    def show_name(self):
        print(self.name)
    
    def show_age(self):
        print(self._age)

    def show_salary(self):
        print(self._Person__salary)

ob1 = Person()
ob1.show_person()
ob1.get_salary()
ob1.show_person()

ob2 = Najma()
# ob2.show_name()

# ob2.show_age()
# ob2.show_salary()