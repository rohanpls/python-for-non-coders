#Program to tell order of list

list = [7,6,5,4,1,2,3]   #Given a list

a,b = list[0],list[1]
z,y = list[-1],list[-2]

print(list)

if a < b:
  patternOne = 'increasing'
elif a > b:
  patternOne = 'decreasing'

if y < z:
  patternTwo = 'increasing'
elif z < y:
  patternTwo = 'decreasing'

#It will compare first two and last two numbers with each other to find the order

if patternOne == patternTwo:
  print(patternOne)
else:
  print(f'{patternOne} then {patternTwo}')
