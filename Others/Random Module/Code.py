
from random import *

print(random())
print(randint(1,2))
print(uniform(3,4))
print(randrange(0,100,2)) #even
print(randrange(1,101,3))

lst= [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
shuffle(lst)
print(lst)
print(choice(lst))
print(sample(lst,3))
