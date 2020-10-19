import sys

selection = 1

while (selection != 0):
    selection = eval(input("Type a number from 1 to 3 to calculate the rectangular moment of inertia, or 4 to exit: "))
    print(" ")
 
 
#ask for user input to determine type of beam
    if (selection == 1):
        print("You have selected an I-beam.")
        B = eval(input("Please enter a value for B: "))
        H = eval(input("Please enter a value for H: "))
        b = eval(input("Please enter a value for b: "))
        h = eval(input("Please enter a value for h: "))
        answer = ((B * (H * H * H)) - (b * (h * h * h)))/12
        print("The rectangular moment of inertia for an I-beam is: ", answer, "inches ^ 4.")
        print(" ")

    if (selection == 2):
        print("You have selected a rectangular beam.")
        b = eval(input("Please enter a value for b: "))
        h = eval(input("Please enter a value for h: "))
        answer = (b * (h * h * h))/12
        print("The rectangular moment of inertia for an R-beam is: ", answer, "inches ^ 4.")
        print(" ")
        
    if (selection == 3):
        print("You have selected a cylindrical beam.")
        r = eval(input("Please enter a value for r: "))
        answer = (3.14159 * (r * r * r * r))/12
        print("The rectangular moment of inertia for a C-beam is: ", answer, "inches ^ 4.")
        print(" ")

    if (selection == 4):
        print("You have chosen to quit the program.")
        sys.exit()

#user input invalid
    if (selection < 1 or selection > 4):
        print("Error, please try again.")
        print(" ")
