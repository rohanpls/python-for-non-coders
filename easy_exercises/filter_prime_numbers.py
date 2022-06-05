#Program to filter prime numbers from list of user input values

numberBank = [] #Declare an empty list

arrayLimit = int(input('Enter List limit: '))   #Get list limit value from user
for arrayInput in range(0, arrayLimit):
   userInput = int(input('Enter List value: '))  #Assign user input value to variable 
   numberBank.append(userInput) #Append the variable to list
    
print(numberBank)

for primeCheck in numberBank:  #Iterate over the list
    counter = 0  # Set prime check counter to 0 each time the loop runs
    for divisiblityCheck in range(1, primeCheck+1):  #Another loop to divide and check each list value
        if primeCheck % divisiblityCheck == 0:   #Prime number can only be divided 2 times: by 1 and number itself
            counter+=1 
            
    if counter == 2:  #If value was divisible only 2 times during second loop, then declare it as prime number
        print(primeCheck)