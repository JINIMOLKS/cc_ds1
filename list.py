cars=["Volvo","Benz","Toyota"]
print(cars[0])
print(cars[1:3])
cars.append("Nano")
print(cars)
if "Benz" in cars:
    print("Benz is present in cars")
else:
    print("Benz is not present in cars")
cars.remove("Toyota")
print(cars)
for i,it in enumerate(cars,start=1):
    print(i,it)
