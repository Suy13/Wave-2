coord = input()
a = int(coord[1])
if (coord[0] == 'a') or (coord[0] == 'c') or (coord[0] == 'e') or (coord[0] == 'g'):
    if a % 2 > 0:
        print ('black')
    else: 
        print ('white')
if (coord[0] == 'b') or (coord[0] == 'd') or (coord[0] == 'f') or (coord[0] == 'h'):
    if a % 2 > 0:
        print ('white')
    else:
        print ('black')