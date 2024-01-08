class Listwork():
  def __init__(self,list):
    self.lst = list
    self.lenlst = len(list)
    self.l1 = 0
    self.l2 = 1
  def __iter__(self):
    return (self)
  def __next__(self):
    if self.l2 == self.lenlst:
      raise StopIteration
    else:
      self.sum = self.lst[self.l1] + self.lst[self.l2]
      self.l1 += 1
      self.l2 += 1
      return self.sum

Liist = Listwork([12,24,36,48,50])
for i in Liist:
  print(i)
