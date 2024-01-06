class Algebra():
  def __init__(self, r = 0.0, i = 0.0):
    self.real=r
    self.imag = i
  def __add__(self, y):
      self.real = self.real + y.real
      self.imag = self.imag + y.imag
      return self
  def sho_val(self):
      print(self.real, self.imag)
    
num1 = Algebra(2.5,6.25)
num2 = Algebra(1.45,3.35)
num3 = num1 + num2
num3.sho_val()
