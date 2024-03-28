import math


def asterisks(h, w):  # A function that prints the star triangles
    h = int(h)  # The height of the triangle
    w = int(w)  # The width of the triangle
    print(" " * int(((w - 1) / 2)) + "*" + " " * int(((w - 1) / 2)))  # First line with one asterisk
    lin = 0
    lin = (w-1)/2 - 1   # The number of odd numbers between 1 and w
    if lin == 0:  # edge cases
        lins = (h-2)  # how many lines for each odd number
        if w == 3:
                st = "*"*w
                for j in range(h-1):
                    print(st)
        if w == 1:
                st = "*"
                for j in range(h-1):
                    print(st)
    else:
        lins = (h-2)/lin  # How many lines for each odd number
        lefts = (h-2) % lin  # Division's remainer
        for i in range(3, w, 2):
            st = " "*int(((w-i)/2)) + "*"*i + " "*int(((w-1)/i))
            for j in range(int(lins+lefts)):
                print(st)
            lefts = 0
        print("*"*w)  # Last line full of asteriks


choice = 0
while choice != 3:
    print("Menu:\n 1.Rectangle\n 2.Triangular\n 3.Cancel")
    choice = int(input())
    if choice == 3:
        exit()
    if choice == 1:
        print("Type the height and width of the tower")
        height = float(input())
        width = float(input())
        if height == width or abs(height-width) > 5:
            if height == width:
                print("The area of the square: " + str(height*width))
            if abs(height-width) > 5:
                print("The area of the rectangle: " + str(height*width))
        else:
            print("The perimeter of the rectangle: " + str(2*(height+width)))
    if choice == 2:
        print("Type the height and width of the tower")
        height = float(input())
        width = float(input())
        print("Menu:\n1.Perimeter of the triangle\n2.Triangle print")
        choosetr = int(input())
        if choosetr == 1:
            peri = (width+2*math.sqrt(height**2+(width/2)**2))  # Perimeter of the triangle
            print("The perimeter of the triangle: " + str(peri))
        if choosetr == 2:
            if width % 2 == 0 or width > 2*height:
                print("The triangle cannot be printed")
            else:
                asterisks(height, width)
if choice == 3:
    exit()



