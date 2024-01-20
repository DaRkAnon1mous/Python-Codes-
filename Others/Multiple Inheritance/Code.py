class Number1():
  def __init__(self):
    self.num1 = int(input())

class Number2():
  def __init__(self):
    self.num2 = int(input())

class Number(Number1,Number2):
  def __init__(self):
    Number1.__init__(self)
    Number2.__init__(self)
  def show(self):
    print(self.num1 + self.num2)

n = Number()
n.show()
  
