

try:
    user_input =int(input("Please enter an integer: "))
except ValueError:
    print("Unpeacefully converted to integer")
else:
    print("Great, you successfully entered an integer!")
