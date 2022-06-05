#This code with show how to insert and delete elements in existing arrays
apple_products = ['iPhone', 'Macbook', 'Apple Watch', 'AirTag']
 
print(apple_products)

#insert at end of array
apple_products.append('Airpods')

print(apple_products)

#insert in between the array

apple_products.insert(1, 'iPad')

print(apple_products)

#add a dummy item
apple_products.insert(2, 'iPods')

print(apple_products)

#Delete an item
del(apple_products[2])


print(apple_products)