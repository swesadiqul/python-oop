class Human:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def show_name(self):
        print("The name of Human = ",self.name)

    def show_age(self):
        print("The age of Human = ",self.age)

    class Robot:
        def __init__(self,food):
            self.food = food
        
        def show_food(self):
            print("The food of Robot = ",self.food)



# human = Human('Babul Islam',25)
# human.show_name()
# human.show_age()

robot = Human.Robot('no-food')
robot.show_food()
