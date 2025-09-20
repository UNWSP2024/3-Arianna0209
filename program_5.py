#Title: Hot Dog Price Calculator
#Author: Arianna Endres
#Date 09/19/2025

hot_dog_type = input('Choose a hot dog type. You may select either a hot dog or a chili dog. ')
if hot_dog_type == 'hot dog':
    hot_dog_price = 3.50
else:
    hot_dog_price = 4.50

toppings = input('Choose a topping. You may select cheese, peppers, or grilled onions. ')
if toppings == 'cheese':
    toppings_price = 0.50
elif toppings == 'peppers':
    toppings_price = 0.75
else:
    toppings_price = 1.0

subtotal = hot_dog_price + toppings_price
print(f'Your subtotal is: ${subtotal:.2f}')

tax = subtotal * 0.07
print(f'Your tax is: ${tax:.2f}')

total = subtotal + tax
print(f'Your total is: ${total:.2f}')
