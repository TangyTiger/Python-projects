import time


print("Welcome to the Cube Solver")
time.sleep(1)
print(" ")
side_length = int(input("What is the side length of the cube? "))
if side_length. isdigit():
    if side_length>0:
        surface_area = side_length*side_length*6
        volume = side_length**3
        print("The surface area of the cube is", surface_area)
        time.sleep(0.5)
        print("The volume of the cube is", volume)
    else:
        print("This number cannot be the side length of a cube")
else:
    print("This string cannot be the side length of a cube")
