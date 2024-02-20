import math

n=int(input("Input number of sides:"))
a=int(input("Input the length of a side:"))
z=math.floor((math.pow(a, 2)*n)/(4*math.tan(math.pi/n)))
print(f"The area of the polygon is:{z}")