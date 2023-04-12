#this functions takes in a radius of float type
def areaOfCircle(radius):
    result = 3.14 * (radius ** 2)
    return result

radiusInput = input("Enter radius: ")
print("Radius: " + radiusInput)

area = areaOfCircle(float(radiusInput))

print("Area of Circle with radius  " + str(radiusInput) + " is " +str(area))

