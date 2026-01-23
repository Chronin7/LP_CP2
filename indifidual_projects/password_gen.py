#import utill fucntions
#symbols=33-47,58-64,91-96,123-126
#digits=48-57
#upercase=65-90
#lowwercase=97-122
#define main()
#   reapete forever
#       if util input do you want to use=n
#           return
#       leng=util input How long does the password need to be: 
#       lowwerc=util input Does the password need lowercase letters (Y/N): 
#       upperc=util input Does the password need uppercase letters (Y/N): 
#       nums=util input Does the password need numbers (Y/N): 
#       symbol=util input Does the password need special characters letters (Y/N):
#       reapete 4 times
#           counter=0
#           password_set={}
#           if symbol=y:
#               rand1=random 1-4
#               if rand1 = 1
#                   rand2=random33-47
#               if rand1 = 2
#                   rand2=random58-64
#               if rand1 = 3
#                   rand2=random91-96
#               if rand1 = 4
#                   rand2=random123-126
#               password_set add(to ascii(rand2))
#               counter+=1
#           if upperc=y:
#               passwrod_set add(to ascii(random65-90))
#               counter+=1
#           if lowwerc=y:
#               passwrod_set add(to ascii(random97-122))
#               counter+=1
#           if nums=y:
#               passwrod_set add(to ascii(random48-57))
#               counter+=1
#           reapete leng-counter:
#               rand3=random1-4
#               if rand3=1:
#                   rand1=random 1-4
#                   if rand1 = 1
#                       rand2=random33-47
#                   if rand1 = 2
#                       rand2=random58-64
#                   if rand1 = 3
#                       rand2=random91-96
#                   if rand1 = 4
#                       rand2=random123-126
#                   password_set add(to ascii(rand2))
#               if rand3=2:
#                   passwrod_set add(to ascii(random65-90))
#               if rand3=3:
#                   passwrod_set add(to ascii(random97-122))
#               if rand3=4:
#                   passwrod_set add(to ascii(random48-57))
#          output(password set)
#if this curent file
#       run main
import utill_functions
import random
def main():
    while True:
        if utill_functions.get_valid_type(str,"do you want to use (y/n): ",valid=["y","n"])=="n":
            return
        leng=max(4,min(utill_functions.get_valid_type(int,"what is the length of the password (minimum of 4, max of 100): "),100))
        lowwerc=False if utill_functions.get_valid_type(str,"dose it need lowwercase letters (y/n): ",valid=["y","n"])=="n" else True
        upperc=False if utill_functions.get_valid_type(str,"dose it need uppercase letters (y/n): ",valid=["y","n"])=="n" else True
        symbol=False if utill_functions.get_valid_type(str,"dose it need speshal charicters (y/n): ",valid=["y","n"])=="n" else True
        num=False if utill_functions.get_valid_type(str,"dose it need numbers (y/n): ",valid=["y","n"])=="n" else True
        for _ in range(5):
            counter=0
            password_set={"start","starter"}
            password_set.remove("start")
            password_set.remove("starter")
            if symbol:
                rand1=random.randint(1,4)
                if rand1==1:
                    rand2=random.randint(33,47)
                if rand1==2:
                    rand2=random.randint(58,64)
                if rand1==3:
                    rand2=random.randint(91,96)
                if rand1==4:
                    rand2=random.randint(123,126)
                password_set.add(chr(rand2))
                counter+=1
            if upperc:
                password_set.add(chr(random.randint(65,90)))
                counter+=1
            if lowwerc:
                password_set.add(chr(random.randint(97,122)))
                counter+=1
            if num:
                password_set.add(chr(random.randint(48,57)))
                counter+=1
            if not num and not upperc and not lowwerc and not symbol:
                print("you need to have at least 1 yes")
                continue
            counter2=counter
            while counter2!=leng:
                rand3=random.randint(1,4)
                if rand3==1 and symbol:
                    rand1=random.randint(1,4)
                    if rand1==1:
                        rand2=random.randint(33,47)
                    if rand1==2:
                        rand2=random.randint(58,64)
                    if rand1==3:
                        rand2=random.randint(91,96)
                    if rand1==4:
                        rand2=random.randint(123,126)
                    password_set.add(chr(rand2))
                    counter2+=1
                if rand3==2 and upperc:
                    password_set.add(chr(random.randint(65,90)))
                    counter2+=1
                if rand3==3 and lowwerc:
                    password_set.add(chr(random.randint(97,122)))
                    counter2+=1
                if rand3==4 and num:
                    password_set.add(chr(random.randint(48,57)))
                    counter2+=1
            for x in password_set:
                print(x,end="")
            print()
if __name__=="__main__":
    main()