#program will take user's age as input and check eligiblity for vote.
#If they are not eligible, it will tell them how many years they're below the voting age.

userAge = int(input('Enter your age: '))

if userAge >= 18:
    print('Your are eligible to vote')
else:
    print(f'You are not eligible to vote because you are {18-userAge} below the voting age')