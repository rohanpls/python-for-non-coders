#Example on how boolean works in python and how you can use it in conditions

feeling_hungry = True

if feeling_hungry:  #if variable has boolean value true
    print('feeling super hungry right now')
else:   #if boolean value is false then execute the following
    print('I don\'t feel hungry right now')

age = 23

checkAge = age > 20  #assigning boolean value to a variable

#comparing two things in python turns into a boolean

if checkAge:
    print('You should maintain your diet')
else:
    print('You should eat more healthy because you are growing')
