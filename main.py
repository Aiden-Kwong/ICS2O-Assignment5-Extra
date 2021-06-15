import math

loop = True

print("-----------------------------------------")
print("Thanks for using this circle calculator.\n")
print("-----------------------------------------")


while loop == True:

    print("Please enter the diameter of the circle (radius x 2)\n")

    diameter = int(input("Enter the diameter: "))

    while True:
        correct = str(input("Is the diameter correct? (Y/N): "))
        correct = correct.upper()
        if correct in ("Y", "N"):
            if correct == "N":
                while correct == "N":
                    diameter = int(input("Enter the diameter: "))
                    break
            else: 
                break
        else:
            print("Invalid input.")

    if diameter > 0:
        radius = diameter / 2
        area = (radius * radius) * (math.pi)
        circ = diameter * (math.pi)

        print("Area: ")
        print(area)

        print("Circumference: ")
        print(circ)
        print("\n")
        while True:
            restart = str(input("Do you want to calculate a new circle? (Y/N): "))
            restart = restart.upper()
            if restart in ("Y", "N"):
                if restart == "N":
                    print("Goodbye!")
                    loop = False
                    break
                elif restart == "Y":
                    print("\n")
                    break
            else:
                print("Invalid input")
      
      else:
        print("Please enter a positive number.")
        print("\n")
