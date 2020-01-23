class robot:
   def __init__(self, x, y):
       self.x = x 
       self.y = y
   def bouge(self, mouvement):
       if (len(mouvement) == 2):
           multiple = mouvement[1]
       else:
           multiple = 1
       if mouvement == "s":
           self.y = self.y - (1*multiple)
       elif mouvement == "n":
           self.y = self.y + (1*multiple)
       elif mouvement == "o":
           self.x = self.x - (1*multiple)
       elif mouvement == "e":
           self.x = self.x + (1*multiple)
       return self.x, self.y
