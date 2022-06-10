import random

def gameWin(comp,you):
    if comp==you :
        return None
    elif comp=="w" :
        if you=="g":
            return False
        elif you=="s":
            return True  
    elif comp=="s" :
        if you=="w":
            return False
        elif you=="g":
            return True  
    elif comp=="g" :
        if you=="s":
            return False
        elif you=="w":
            return True                            


print("computer turn : snake(s) , water(w) or gun(g) ?")       
randomNo = random.randint(1,3)
if(randomNo==1):
    comp= "s"
elif randomNo==2:
    comp = "w"
else:
    comp = "g"

you = input("your turn : snake(s) , water(w) or gun(g) ?")    
a = gameWin(comp,you)

print(f"you chose {you}") 
print(f"computer chose {comp}") 
if a==True:
    print("you win!")
elif a==False:
    print("you lose!")   
elif a==None:
    print("It's a tie")     
