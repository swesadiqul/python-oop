class Human:

    def __init__(self,name):
        self.name = name
    
    #instance method
    def show_name(self):
        print(self.name)

    @classmethod
    def cls_method(cls):
        print('This is a class method.')

    @staticmethod
    def emnetai():
        print('This is a static method.')

human = Human('Nobita')
# human.show_name()
# human.cls_method()
# # Human.cls_method()
human.emnetai()
Human.emnetai()
