class Actor:
    def __init__(self,n,f):
        self.family = f
        self.name = n
        

    def show(self):
        print(self.name , self.family)