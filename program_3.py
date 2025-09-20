#Title: Shipping Weight Calculator
#Author: Arianna Endres
#Date: 09/19/2025


weight = float(input('Enter the weight of your shipment: '))

if weight <= 2:
    shipping_cost = weight * 1.50
elif weight > 2 and weight <= 6:
    shipping_cost = weight * 3.00
elif weight >6 and weight <= 10:
    shipping_cost = weight * 4.00
else:
    shipping_cost = weight * 4.75

print(f'Your shipping cost is: ${shipping_cost:.2f}')