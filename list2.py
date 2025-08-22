cars=[{"name":"Innova","quantity":2,"price":5500000},
     {"name":"Audi","quantity":1,"price":3300000},
     {"name":"Toyota","quantity":4,"price":2000000},
     {"name":"Benz","quantity":1,"price":100000}]
print(cars)
cars = []
num_cars = int(input("How many cars do you want to add? "))
for i in range(num_cars):
    print(f"\nEnter details for car {i + 1}:")
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    if price>8000000:
        discount=(10/100)*price
        price=price-discount
    car = {
        "name": name,
        "quantity": quantity,
        "price": price
    }  
    cars.append(car)
print("\nFinal car list:")
print(cars)

