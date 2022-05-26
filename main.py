from xxlimited import Null


def credits_to_creator():
    print("|-------------------------------|")
    print("| Temperature Converter Program |")
    print("|     Made By MGkillergamer     |")
    print("|-------------------------------|")


credits_to_creator()

choice = Null
current_degree_scale = ""
new_degree_scale = ""
current_value = Null
new_value = Null

# print("Type A Degree Scale(c/k/f) Default is Celsius")
choice = input("Type A Degree Scale(c/k/f): ")

if choice == "c":
    current_degree_scale = "c"
elif choice == "f":
    current_degree_scale = "f"
elif choice == "k":
    current_degree_scale = "k"
else:
    print("You must type a legitimate scale")
    exit()

choice = input("Type The Scale you want to convert To(c/k/f): ")
while choice == current_degree_scale:
    print("You cant convert to the same scale! Please Type a different")
    choice = input("Type The Scale you want to convert To(c/k/f): ")


if choice == "c":
    new_degree_scale = "c"
if choice == "f":
    new_degree_scale = "f"
if choice == "k":
    new_degree_scale = "k"


current_value = int(input("Type The "+current_degree_scale+" Value: "))
# Celsius And Kelvin
if current_degree_scale == "c" and new_degree_scale == "k":
    new_value = current_value + 273.15
    print(str(current_value)+"°C is "+str(new_value)+" in Kelvin Scale")
elif current_degree_scale == "k" and new_degree_scale == "c":
    new_value = current_value - 273.15
    print(str(current_value)+"K is "+str(new_value)+" in °C scale")
# Fahrenheit And Celcius
if current_degree_scale == "c" and new_degree_scale == "f":
    new_value = (current_value * 9/5) + 32
    print(str(current_value)+"°C is "+str(new_value)+" in °F Scale")
elif current_degree_scale == "f" and new_degree_scale == "c":
    new_value = (current_value - 32) * 5/9
    print(str(current_value)+"°F is "+str(new_value)+" in °C")
# Fahrenheit And Kelvin
if current_degree_scale == "f" and new_degree_scale == "k":
    new_value = (current_value - 32) * 5/9 + 273.15
    print(str(current_value)+"°F is "+str(new_value)+" in Kelvin Scale")
elif current_degree_scale == "k" and new_degree_scale == "f":
    new_value = (current_value - 273.25) * 9/5 + 32
    print(str(current_value)+"K is "+str(new_value)+" in °F scale")


