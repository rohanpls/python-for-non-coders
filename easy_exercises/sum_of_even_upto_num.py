question =''' Print the sum of even numbers upto given input num
Example:
Input: 6
Output: 12'''

num = int(input('Enter the number: '))
sum = 0
for n in range(1,num+1):
    if n % 2 == 0:
        sum+=n
    else:
        pass

print(sum)