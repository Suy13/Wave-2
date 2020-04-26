import math
a = float(input())
b = float(input())
c = float(input())
discr = ((b**2) - (4*a*c))
if discr > 0:
    print ('2 real roots')
    print (((-b) + math.sqrt(discr))/(2*a))
    print (((-b) - math.sqrt(discr))/(2*a))
elif discr == 0:
    print ('1 real root')
    print (((-b) + math.sqrt(discr))/(2*a))
else:
    print ('no real roots')