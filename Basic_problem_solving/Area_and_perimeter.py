

def rectangle_calculations(L,W):
    area = L*W
    perimeter = 2*(L+W)
    print("Area of Rectangle:", area, "cm square")
    print("Perimeter of Rectangle:", perimeter, "cm")
L = int(input("Enter the length of rectangle (in cm): "))
W = int(input("Enter the width of rectangle (in cm): "))
rectangle_calculations(L,W)
