class Students:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def show_name(self):
        print(self.name)

    def show_roll(self):
        print(self.roll)


class Human:
    
    def __init__(self,name,roll,food):
        self.name = name
        self.roll = roll
        self.food = food
    
    def show_name(self):
        print(self.name)
    
    def show_roll(self):
        print(self.roll)
    
    def show_food(self):
        print(self.food)