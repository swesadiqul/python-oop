from first_module import Human


class Animal(Human):
    def __init__(self,name,roll,food,pet):
        super().__init__(name,roll,food)
        self.pet = pet

    def show_pet(self):
        print(self.pet)