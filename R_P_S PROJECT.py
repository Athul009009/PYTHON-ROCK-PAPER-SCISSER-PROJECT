import random
c=random.randint(1,3)
# print(c)

def game(you,comp):
    
    if comp==you:
        print("Its a TIE!!!")
    if comp=='R':
        if you =='P':
            return True
        if you == 'S':
            return False
    if comp=='P':
        if you =='R':
            return False
        if you == 'S':
            return True
    if comp=='S':
        if you =='P':
            return True
        if you == 'R':
            return False


print("computers turn :ROCK[R] PAPER[P] SCISSOR[S]")
import random
c=random.randint(1,3)
if c==1:
        comp='R'
elif c==2:
        comp='P'
elif c==3:
        comp='S'


you=input("Players turn :ROCK[R] PAPER[P] SCISSOR[S]    :")

a=game(you,comp)

if a==None:
    print("The Game is a tie")
elif a:
    print("You win")
else :
    print("You lose")
print("Computr chose",{comp})
print("yOU chose",{you})




