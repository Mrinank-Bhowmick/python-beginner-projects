#purpose: to calculate the volume of a specific 3d shape
#updates:
    #1. 2022-10-04 12:13:15 : created this project
    #2. 2022-10-04 14:47:13 : added 6 shapes (for now)

#to do
    #Fix the "invalid input" loop further
    #Add more shapes
    #make easier selection for shapes
#Welcome to my attempt to Create a volume finder for 6 specific shapes

print("----------------")
print("created by: ")
print("https://github.com/ChefYeshpal")
print("for: hacktober")
print("----------------")

#add's, subtract's, multiply's and divide' numbers
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("-----------------------")
print("Select operation.")
print("1.Cube/cuboid")
print("2.Pyramid(RightRectangular)")
print("3.Cylinder")
print("4.Sphere")
print("5.Cone")
print("6.Ellipsoid")
print("-----------------------")
while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")
    print("-----------------------")

    if choice in ('1', '2'):
        num1 = float(input("Enter Length: "))
        num2 = float(input("Enter Breadth/Width: "))
        num3 = float(input("Enter Height: "))
        print("-----------------------")


        if choice == '1':
            print("The volume of the Cube/cuboid is: ",num1 * num2 * num3, "unit's")

        elif choice == '2':
            print("The volume of the Pyramid is: ",(num1 * num2 * num3)/3, "unit's")

        
    if choice in ('3', '4', '5'):
            R = float(input("Enter the raduis: "))
            H = float(input("Enter the height: "))
            print("-----------------------")
            

            if choice == '3':
                print("The volume of the Cylinder is: ",22/7*((R)**2)*H, "unit's")

            elif choice == '4':
                print("The volume of the Sphere is: ",4/3*22/7*((R)**3), "unit's")

            elif choice == '5':
                print("The volume of the cone is: ", 22/7*((R)**2)*H/3)
    if choice in ('6'):
            Axs = float(input("a axis: "))
            Bxs = float(input("b axis: "))
            Cxs = float(input("c axis: "))

            print("-----------------------")

            if choice == '6':
                print("The volume of the Ellipsoid is: ",4/3 * 22/7 * Axs * Bxs * Cxs, "unit's")



            print("-----------------------")    
    break
else:
    print("Invalid Input")



#insert from line 50
'''if choice == '1':
            print("The volume of the Cube/cuboid is: ",num1 * num2 * num3, "unit's")

        elif choice == '2':
            print("The volume of the Pyramid is: ",(num1 * num2 * num3)/3, "unit's")'''