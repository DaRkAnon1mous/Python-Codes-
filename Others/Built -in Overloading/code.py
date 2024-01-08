class Number():
  def __init__(self, Str=''):
    self.str = Str
  def __iter__(self):
    return iter(self.str)

num = Number('123')
print(num.str)
max = int(num.str)*2
print(max)
for i in num:
  print(i)
