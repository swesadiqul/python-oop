class Rabiul:
    def rabiul_self(self):
        print("I'm Rabiul Islam.")

    def power(self):
        print("I've a lot of power.")

class Suzana(Rabiul):
    def suzana_self(self):
        print("I'm suzana Rahman.")

class Karima(Rabiul):
    def karima_self(self):
        print("Hey, I'm Karima Jannat.")


obj = Suzana()
obj.suzana_self()
obj.power()

obj2 = Karima()
obj2.karima_self()
obj2.power()