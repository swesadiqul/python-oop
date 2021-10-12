from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def go_school(self):
        pass
    
    #concrete method
    def result(self):
        print("Yes, I've gone to school.")

class Nobita(Father):

    def go_school(self):
        super().result()

    def playing(self):
        print('Playing Football.')
    
    def singing(self):
        print('Singing')


nobita = Nobita()
nobita.go_school()
nobita.playing()