class Human:
    #class variable
    cls_v = 'this is a class variable.'

    def __init__(self,name):
        #instance variable
        self.name = name
    
    #instance method
    def show_name(self):
        print(self.name)
        print(self.cls_v)

    @classmethod
    def cls_method(cls):
        print(cls.cls_v)
        print('This is a class method.')

    @staticmethod
    def emnetai():
        print('This is a static method.')

human = Human('Nobita')
# human.show_name()
# human.cls_method()
# Human.cls_method()
human.cls_method()
# human.emnetai()
# Human.emnetai()
# print(Human.cls_v)