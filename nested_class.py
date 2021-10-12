class Human:
    def __init__(self,name):
        self.name = name
    
    def show_info(self):
        print(self.name)
        print("Human Class.")
    
    class Robot:
        def __init__(self,name):
            self.name = name
        
        def show_name(self):
            print(self.name)
            print("Robot Class.")
        
        class Robo:
            def __init__(self,name):
                self.name = name
            
            def show_details(self):
                print(self.name)
                print('Robo Class.')
    
    



ob1 = Human('Jubayer Ahmed')
ob2 = ob1.Robot('Nusrat Mim')
ob3 = Human.Robot.Robo('Zakariya Islam')

ob1.show_info()
ob2.show_name()
ob3.show_details()
