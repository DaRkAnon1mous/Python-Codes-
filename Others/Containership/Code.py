class Dev():
  def __init__(self):
    self.name = 'Dev'
    self.age = '20'
  def show(self):
    print(f'Name : {self.name}')
    print(f'Age : {self.age}')

class Dev1():
   def __init__(self):
     self.pri = Dev()
   def sho(self): 
     self.pri.show()
     

jas = Dev1()
jas.sho()
