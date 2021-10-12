class Human:
    def __init__(self,name):
        self.name = name
    
    def show_name(self):
        print(self.name)
        print("I'm of function in Human class.")
    
    class Robot:
        def __init__(self,name):
            self.name = name
        
        def show_info(self):
            print(self.name)
            print("I'm of function in Robot class.")

class Huma(Human):
    def __init__(self,name):
        self.name = name

    def show_name_data(self):
        print(self.name)
        print("I'm of function in Huma class.")

    class Robo(Human.Robot):
        def __init__(self,name):
            self.name = name

        def show_details(self):
            print(self.name)
            print("I'm of function in Robo Class.")
    
huma = Huma('Junayed Islam')
huma.show_name()
huma.show_name_data()

robo = Huma.Robo('Safina akhter')
robo.show_details()
robo.show_info()




