import random
options=["rock","paper","scissor"]
user_point=0
computer_point=0
#Muhammed Sidan Mini Projects.
while True:
    user_choice=input("Chose yours Rock,Paper,Scissor Or 'q' To Quit: ").lower()
    if user_choice=="q":
        break
    if user_choice not in options:
        continue
    random_choice=random.randint(0,2)
    computer_choice=options[random_choice]
    # 1 for rock, 2 for paper, 3 for scissor 
    if user_choice=="rock" and computer_choice=="scissor":
        print("You won!")
        user_point+=1
    elif user_choice=="paper" and computer_choice=="rock":
        print("You won!!")
        user_point+=1
    elif user_choice=="scissor" and computer_choice=="paper":
        print("You won!!")
        user_point+=1
    else:
        print("Computer Won")
        computer_point+=1
print(f"Your score is {user_point}.")
print(f"computer score is {computer_point}.")
if user_point>computer_point:
    print("You Won The Game,Congrats")
elif user_point==computer_point:
    print("Its A Tie.")
else:
    print("The Computer Won the Game")
print("Good bye!")