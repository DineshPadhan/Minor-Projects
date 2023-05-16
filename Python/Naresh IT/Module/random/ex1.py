import random as r
print(r.randrange(0,10,2))
print(r.randint(0,10))
print('%0.3f'%r.random())   #only 3 number after decimal
print(round(r.random(),2))  #only 2 number after decimal
print(round(r.uniform(10,12.1),2))  #random between number



s = 'Python'
print(r.choice(s))
t = [1, 2, 3, 4, 5]
r.shuffle(t)
print(t)