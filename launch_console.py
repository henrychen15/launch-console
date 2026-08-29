print("Welcome to the Launch Console!")

name = input("What is your name? ")
print(f"Hi, {name}!")

menu = ["About me", "My goals", "My happiness", "Exit"]

def about_me(name):
    print(f"My name is {name}.")

def my_goals():
    print("My goals are to have fun and eat food!")

def my_happiness():
    print("My mood is looking great!")

def display_menu():
    for index in range(len(menu)):
        print(f"{[index + 1]} {menu[index]}")

running = True

while running:
    display_menu()
    option = input("Select an option with a number: ")

    if option == "1":
        about_me(name)
    elif option == "2":
        my_goals()
    elif option == "3":
        my_happiness()
    elif option == "4":
        running = False
    else:
        print("Invalid input!")

print(f"Goodbye, {name}!")