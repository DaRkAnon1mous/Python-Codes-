class Number():
  def __init__(self):
    self.num = 0
  def mul(self):
   
    self.num = self.num * 2
  def div(self):
   
    self.num = self.num / 2
  def add(self):
    
    self.num = self.num + 2
  def sub(self):
    
    self.num = self.num - 2

class Number2(Number):
  def __init__(self):
    super().__init__()
  def show(self):
    print("Current value:" + str(self.num))

pr = Number2()
pr.show()
pr.add()
pr.add()
pr.mul()
pr.div()
pr.sub()
pr.show()
