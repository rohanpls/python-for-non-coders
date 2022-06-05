n = int(input('Enter the limit:'))
for odd_numbers in range(1, n+1):
    if odd_numbers % 2 != 0:
        print(odd_numbers)