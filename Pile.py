class Pile:
    
    def __init__(self):
        self.val=[]
    
    def empiler(self,a):
        self.val.append(a)

    def depiler(self):
        if self.pilevide():
            return
        else:
            return self.val.pop(-1)

    def sommet(self):
        if not self.pilevide():
            return self.val[-1]

    def pilevide(self):
        return len(self.val)==0

    def __str__(self):
        return str(self.val)
