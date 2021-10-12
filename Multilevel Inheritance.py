class Rabiul:
    def rabiul_self(self):
        print("I'm Rabiul Islam.")
    
    def power(self):
        print("I've a lot of power.")

class Suzana(Rabiul):
    def suzana_self(self):
        print("I'm Suzana Rahman.")

class Karima(Suzana):
    def karima_self(self):
        print("Hey,I'm Karima Akhter.")

obj = Karima()
obj.karima_self()
obj.power()