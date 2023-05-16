# purpose: to calculate the volume of a specific 3d shape
# updates:
# 1. 2022-10-04 12:13:15 : created this project
# 2. 2022-10-04 14:47:13 : added 6 shapes (for now)
# 3. 2022-10-06 15:12:00 : Added 2 new shapes
# 4. 2022-10-11 17:11:45 : fixed the invalid loop
# to do


###############################################################################

# Welcome to my attempt to Create a volume finder for 6 specific shapes!!  (more coming soon)

from cmath import sqrt


print("----------------")
print("created by: ")
print("https://github.com/ChefYeshpal")
print("for: hacktober")
print("----------------")


# add's, subtract's, multiply's and divide' numbers
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
print("7.Torus(Donut)")
print("8.Hexagonal Prism")
print("-----------------------")
while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
    print("-----------------------")

    if choice in ("1", "2"):
        num1 = float(input("Enter Length: "))
        num2 = float(input("Enter Breadth/Width: "))
        num3 = float(input("Enter Height: "))
        print("-----------------------")

        if choice == "1":
            print("The volume of the Cube/cuboid is: ", num1 * num2 * num3, "unit's")

        elif choice == "2":
            print("The volume of the Pyramid is: ", (num1 * num2 * num3) / 3, "unit's")

    if choice in ("3", "4", "5"):
        R = float(input("Enter the raduis: "))
        H = float(input("Enter the height: "))
        print("-----------------------")

        if choice == "3":
            print("Finding the volume for Cylinder")
            print("-----------------------")

            print("The volume of the Cylinder is: ", 22 / 7 * ((R) ** 2) * H, "unit's")

        elif choice == "4":
            print("Finding the volume for Sphere")
            print("-----------------------")

            print(
                "The volume of the Sphere is: ", 4 / 3 * 22 / 7 * ((R) ** 3), "unit's"
            )

        elif choice == "5":
            print("Finding the volume of Cone")
            print("-----------------------")

            print("The volume of the cone is: ", 22 / 7 * ((R) ** 2) * H / 3)
    if choice in ("6"):
        Axs = float(input("a axis: "))
        Bxs = float(input("b axis: "))
        Cxs = float(input("c axis: "))

        print("-----------------------")

        if choice == "6":
            print(
                "The volume of the Ellipsoid is: ",
                4 / 3 * 22 / 7 * Axs * Bxs * Cxs,
                "unit's",
            )

    if choice in ("7"):
        R = float(input("Enter the Major Radius: "))
        print("Make sure that what Major Radius > Minor Radius")
        r = float(input("Enter the Minor Radius: "))

        print("-----------------------")

        print(
            "The volume of the Torus is: ",
            ((22 / 7 * ((r) ** 2)) * (2 * 22 / 7 * R)),
            "unit's",
        )

        print("-----------------------")

    if choice in ("8"):
        a = float(input("Enter the Base edge: "))
        h = float(input("Enter the Height: "))

        print("-----------------------")

        print(
            "The volume of the Right Regular Hexagonal Prism is:",
            (3 * sqrt(3) / 2 * a * a * h),
            "unit's",
        )

    else:
        print("Invalid Input")

print("thank you for using my program!!")
