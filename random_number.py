import random

print(random.randint(1, 10)) #prints random integer between 1-10
print(random.random()) #prints random float value between 0-1

val = random.randint(1,3)  
if val == 1:
    print('Yes')
elif val == 2:
    print('No')
elif val == 3:
    print('Maybe')
else:
    print('strange exception')  #just in case, NOT REQUIRED