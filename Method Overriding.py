# class Human:
#     def __init__(self,name):
#         self.name = name
    
#     def show_name(self):
#         print(self.name)
#         print("Human Class.")

# class Robot(Human):

#     def __init__(self,name):
#         self.name = name
    
#     def show_name(self):
#         print(self.name)
#         print("Robot Class.")

# human = Human('Abdur Rahman')
# robot = Robot('Shofiya')

# human.show_name()
# robot.show_name()





class Phone:

    def __init__(self):
        print('I am in Phone Class.')


class Itel(Phone):
    #init
    def __init__(self):
        super().__init__()
        print('I am in Itel Class.')


itel = Itel()