import random
group = [0,'00',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
random  = random.choice(group)
print ("The spin resulted in",random,'...')
if random == 0:
    print ('Pay',random)
elif random == '00':
    print ('Pay',random)
else:
    print ('Pay',random)
if (random !=0) or (random !='00'):
    if (random == 1) or (random ==3) or (random ==5) or (random ==7) or (random ==9) or (random ==12) or (random ==14) or (random ==16) or (random ==18) or (random ==19) or (random ==21) or (random ==23) or (random ==25) or (random ==27) or (random ==30) or (random ==32) or (random ==34) or (random ==36):
        print ('Pay Red')
        if random % 2 == 0:
            print ('Pay Even')
        elif random % 2 != 0:
            print ('Pay Odd')
    elif (random ==2) or (random ==4) or (random ==6) or (random ==8) or (random ==10) or (random ==11) or (random ==13) or (random ==15) or (random ==17) or (random ==20) or (random ==22) or (random ==24) or (random ==26) or (random ==28) or (random ==29) or (random ==31) or (random ==33) or (random ==35):
        print ('Pay Black')
        if random % 2 == 0:
            print ('Pay Even')
        elif random % 2 != 0:
            print ('Pay Odd')
if random != '00':
    if (random >=1) and (random <= 18):
        print ('Pay 1 to 18')
    elif random > 18:
        print ('Pay 19 to 36')