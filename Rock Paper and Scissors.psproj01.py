#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     28-05-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#------------------------------------------------------------------------------

import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp =='R':
        if you=='P':
            return True
        elif you=='S':
            return False
    elif comp=='P':
        if you=='S':
            return True
        elif you=='R':
            return False
    elif comp =='S':
        if you=='R':
            return True
        elif you=='P':
            return False


print("Comp turn: Rock(R) Paper(P) or Scissor(S)?")
randNo =random.randint(1,3)
print(randNo)
if randNo==1:
    comp='R'
elif randNo==2:
    comp='P'
elif randNo==3:
    comp='S'
you=input("Your turn: Rock(R) Paper(P) or Scissors(S)?")
a=gamewin(comp,you)
if a==None:
    print("the game is a tie!")
elif a:
    print("You Win!")
else:
    print("You lose!")