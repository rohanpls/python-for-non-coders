
question='''You are given a number stored in a variable with the namenum

For all numbers in the range[1,num], including num

1. If the number is divisible by 3 and 5 both, print FizzBuzz

2. Else If the number is divisible by 3, print "Fizz", without quotes

3. Else If the number is divisible by 5, print "Buzz", without quotes

4. Else, print the number as it is
Input
The first line containsT, the number of test cases.

The first line of each test case contains the value stored in the variablenum


Print the required output, according to the conditions shown in the problem statement

'''

num = int(input('Enter Number: '))
for i in range(1,num):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    else:
        print(i)