def cube( num ):
    result =  num ** 3 
    return result


num = input( "Enter a number: " )
val = cube(float(num))

print("Your number cubbed = " + str(val)) 