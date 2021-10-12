class Profile:
    
    def name(self,first=None,middle=None,last=None):
        if(first !=None  and middle !=None and last !=None):
            print(first+' '+middle+' '+last)
        elif(first !=None and middle !=None):
            print(first+' '+middle)
        else:
            print(first)

p = Profile()
p.name('Marjuk','Ahmed','Siddiki')