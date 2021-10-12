#Special / Magic / Dunder Method
#__init__,__add__,__sub__,__mul__,__div__ method

#for exmaple
# a = 5
# b = 5

# print(a+b)
# print(a.__add__(b))

# c = 10 
# d = 4
# print(c-d)
# print(c.__sub__(d))


class Number:
    def __init__(self,no):
        self.no = no

    def __mul__(self,others):
        return 'you can write anything here.' * 10

    def show(self):
        print(self.no)


a = Number(4)
b = Number(6)

print(a*b)

#Note: if you can see + oparetor, you have to understood there is working a magic method __add__
#Note: if you can see - oparetor, you have to understood there is working a magic method __sub__
#Note: if you can see * oparetor, you have to understood there is working a magic method __mul__
#Note: if you can see / oparetor, you have to understood there is working a magic method __div__
