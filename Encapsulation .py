#why Encapsulation
#Data Hiding
#Public, Private,Protected

#public data,you can access and modify if it share with you.
# class Nobita:
#     def __init__(self):
#         self.book = "Comics"
#         self.no = 30
    
#     def show(self):
#         print(self.no)

# class Sonio(Nobita):
#     def show_nobita(self):
#         print("Sonio: ",self.no)

# class Shizuka(Nobita):
#     def show_nobita(self):
#         print("Shizuka:",self.no)

# nobita = Nobita()
# sonio = Sonio()
# shizuka = Shizuka()

# # nobita.show()
# # nobita.no = 45


# nobita.show()
# sonio.show_nobita()
# shizuka.show_nobita()




#how to protected data
#for protecting data just you have to use single underscore(_)

# class Nobita:
#     def __init__(self):
#         self.book = "Comics"
#         self.no = 10
#         self._no = 20
    
#     def show(self):
#         print(self.no,self._no)

# class Sonio(Nobita):
#     def show_nobita(self):
#         print("Sonio: ",self.no)

# class Shizuka(Nobita):
#     def show_nobita(self):
#         print("Shizuka:",self._no)

# nobita = Nobita()
# sonio = Sonio()
# shizuka = Shizuka()

# nobita.show()
# nobita._no = 45


# nobita.show()
# sonio.show_nobita()
# shizuka.show_nobita()




#how to hiding data in privately
#for protecting data you have to use double underscore(__) before the variable name.

class Nobita:
    def __init__(self):
        self.book = "Comics"
        self.no = 10
        self._no = 20
        self.__no = 30

    def change_book_count(self):
        self.__no = 45
    
    def show(self):
        print(self.no,self._no,self.__no)

class Sonio(Nobita):
    def show_nobita(self):
        print("Sonio: ",self._Nobita__no) #sonia access private data

class Shizuka(Nobita):
    def show_nobita(self):
        print("Shizuka:",self._no)

nobita = Nobita()
sonio = Sonio()
shizuka = Shizuka()

nobita.show()
nobita.change_book_count()


nobita.show()
sonio.show_nobita()
shizuka.show_nobita()

#Note: you can access private data, but before to see these data you have to use _super class name before this variable.
