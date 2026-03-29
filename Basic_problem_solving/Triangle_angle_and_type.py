A=int(input("enter 1st angle in degrees A:"))
B=int(input("enter 2nd angle in degrees B:"))
C=(180-(A+B))
print("C=",C,"degrees")
if(A==90 or B==90 or C==90):
    print("Right-angled-triangle")
elif (A==B or B==C or C==A):
    print("isosceles triangle ")
else:
    print("Neither")
