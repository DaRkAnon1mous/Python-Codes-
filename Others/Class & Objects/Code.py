class Instructor:

  def __init__(self, name, age, address):
    self.name = name;
    self.age = age;
    self.address = address;
    self.salary = 50;


i = Instructor("Shrey", 21, "Mumbai")
print(i.name)
print(i.age)
print(i.address)
print(i.salary)
