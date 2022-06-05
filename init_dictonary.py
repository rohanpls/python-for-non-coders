# Code to initialise Dictionary in python

# It will give values to defined key
last_names = {'Jeff':'Bezos', 'Bill':'Gates', 'Elon':'Musk', 'Satya':'Nadella'}

#'Jeff' is called Key, 'Bezos' would be it's value

#Array is stored with [], Dictionary is stored with {}


print(last_names)

print(f"Founder of Amazon: {last_names['Jeff']}")  #Print a specific key

# Add an entry to dictionary
last_names['Rohan'] = 'Shahshankar' 

print(last_names)

#Delete a key from dictionary
del(last_names['Bill'])

print(last_names)

#Print the dictorionary using for loop

#There are two methods for doing that.

#1. Using items()
for first,last in last_names.items():
    print(first,last)
    
#2. Without using items()
for names in last_names:
    print(names, last_names[names])
    
#Using 1st way is more ideal