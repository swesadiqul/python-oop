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
    
    class Robo:
        def __init__(self,name):
            self.name = name

        def show_details(self):
            print(self.name)
            print("I'm of function in Robo Class.")



human = Human('Nadim Hossian')
human.show_name()

robot = Human.Robot('Jubayer Rahman')
robot.show_info()

robo = Human.Robo('Masipul Islam Siam')
robo.show_details()




