''' Part 3

n = 50
result1 = (n < 5)
result2 = (n >= 20)
print(result1)
print(result2)

'''

#for n = 10 --> false, false
#for n = 5 --> false, false
#for n = 20 --> false, true
# for n = -5 --> true, false



''' Part 3 

x = -2
if x < 10:
    y = x * 2
else:
    y = x / 2
print "x = " + str(x)
print "y = " + str(y)

'''

#for x = 10, y = 5
#for x = 15, y = 7
#for x = -2, y = -4

''' Part 4

n = 14
if n > 0:
    if n % 2 == 0:
	    n_type = "pos and even"
    else:
	    n_type = "pos and odd"
elif n < 0:
    n_type = "neg"
else:
    n_type = "neither pos nor neg"
print n_type

'''

''' Part 5 

x = 5
if x < 10:
    y = 20
elif x < 20:
    y = 30
else:
    y = 40
print y

'''

#for x = 10, y = 30
#for x = 15, y = 30
#for x = 25, y = 40

''' Part 6 

x = 5
if x < 10:
    y = 20
if x < 20:
    y = 30
else:
    y = 40
print y

'''

'''  Part 7 '''

#min height = 55in, max height = 75in

height = 74
in_limits = ((height > 0 and height < 55 ) or (height > 0 and height < 75))
if in_limits == True:
    print "Hooray"
else:
    print "Oops"