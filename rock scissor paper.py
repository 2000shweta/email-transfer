import random
s=["rock","paper","scissor"]
computer= random.choice(s)
user=input("My Choice is")
print("Computer choice is",computer)
if computer==user:
    print("It's a Tie!!")
elif computer=="rock":
     if user=="paper":
         print("You Win!")
     else:
        print("You Loose!")
elif computer=="paper":
     if user=="scissor":
        print("You Win!")
     else:
        print("You Loose!")
elif computer=="scissor":
     if user=="rock":
        print("You Win!")
     else:
        print("You Loose!")
else:
 print("invalid")
    
