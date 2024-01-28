class Cube():
  def __init__(self,n):
    n = int(n)
    if n != 0:
      self.q = n**3
    else:
      raise ZeroCubeError

class ZeroCubeError(Exception):
  '''0 cant be input as cube'''

try:
  n = Cube(input("Enter your number: "))
  n = Cube(input("Enter your number: "))
except ZeroCubeError:
  print(ZeroCubeError.__doc__)
except:
  print("Something went wrong")
else:
  print('Cube:' + str(n.q))
finally:
  print("Code Executed")
