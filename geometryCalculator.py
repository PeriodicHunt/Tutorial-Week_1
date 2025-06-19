import math
# to access math functions and constants like math.pi

# --- Functions ---
def areaRectangle(length, width):
    
    area = length * width
    return area
  

def areaTriangle(base, height):
    
    area = (base * height) / 2
    return area

def areaCircle(radius):
    
    area = (radius * radius * math.pi)
    return area


# --- Main Program ---

print("Welcome to the Shape Area Calculator!")
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.")

shape = input("Your choice: ").strip().lower()

# these are called conditionals, there will be more information about them next week
# they are meant to check if a condition is true, if so, it runs
# for now, just use this template we gave you :)
if shape == "r":

    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print(length * width)

    pass

elif shape == "t":

    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print((base * height) / 2)

    pass

elif shape == "c":

    radius = float(input("Enter the radius: "))
    print (radius * radius * math.pi)

    pass

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.")
