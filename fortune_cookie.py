import random

lucky_number = random.randint(10,90)

random_number = random.randint(1,3)

if random_number == 1:
    fortune_wish = 'Something interesting will happen today.'
elif random_number == 2:
    fortune_wish = 'Might not be the best day but at least it was needed.'
elif random_number == 3:
    fortune_wish = 'Looks like someone will get rich soon :).'

print(f'{fortune_wish} Your lucky number is {lucky_number}.')
