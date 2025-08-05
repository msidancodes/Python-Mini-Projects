import time
import random

def guesser_1():
     while True:
         step_1=input("add 10 with the your number, 'y' To continue and 'q' to Quit: ").lower()
         if step_1=="y":
                print()
                print("Now add 16 to it....")
                print("...")
                time.sleep(3)
                print("Now add 6... ")
                print(".....")
                time.sleep(3)
                print("now add 2 to it....")
                print("........")
                time.sleep(3)
                print("And finally substract the First Number,i mean the number you Thinked and " \
                "the Final Asnwer is.....")
                print("..........")
                time.sleep(3)
                print("The Final Answer is you got ---- 34 ,am i right??")
                break
         elif step_1=="q":
              print("Good Bye!")
              quit()
         else:
              print("Enter something valid!!")
              continue
def guesser_2():
     while True:
         step_1=input("add 26 with the your number, 'y' To continue and 'q' to Quit: ").lower()
         if step_1=="y":
                print()
                print("Now add 3 to it....")
                print("...")
                time.sleep(3)
                print("Now add 8... ")
                print(".....")
                time.sleep(3)
                print("now add 4 to it....")
                print("........")
                time.sleep(3)
                print("And finally substract the First Number,i mean the number you Thinked and " \
                "the Final Asnwer is.....")
                print("..........")
                time.sleep(3)
                print("The Final Answer is you got ---- 41 ----,am i right??")
                break
         elif step_1=="q":
              print("Good Bye!")
              quit()
         else:
              print("Enter something valid!!")
              continue
def guesser_3():
      while True:
         step_1=input("add 31 with the your number, 'y' To continue and 'q' to Quit: ").lower()
         if step_1=="y":
                print()
                print("Now add 9 to it....")
                print("...")
                time.sleep(3)
                print("Now add 3... ")
                print(".....")
                time.sleep(3)
                print("now add 10 to it....")
                print("........")
                time.sleep(3)
                print("And finally substract the First Number,i mean the number you Thinked and " \
                "the Final Asnwer is.....")
                print("..........")
                time.sleep(3)
                print("The Final Answer is you got ---- 53 ----,am i right??")
                break
         elif step_1=="q":
              print("Good Bye!")
              quit()
         else:
              print("Enter something valid!!")
              continue
def guesser_4():
      
      while True:
         step_1=input("add 13 with the your number, 'y' To continue and 'q' to Quit: ").lower()
         if step_1=="y":
                print()
                print("Now add 2 to it....")
                print("...")
                time.sleep(3)
                print("Now add 20... ")
                print(".....")
                time.sleep(3)
                print("now add 11 to it....")
                print("........")
                time.sleep(3)
                print("And finally substract the First Number,i mean the number you Thinked and " \
                "the Final Asnwer is.....")
                print("..........")
                time.sleep(3)
                print("The Final Answer is you got ---- 46 ----,am i right??")
                break
         elif step_1=="q":
              print("Good Bye!")
              quit()
         else:
              print("Enter something valid!!")
              continue     
print("--Welcome to the magical number Guesser--")
print("Rule: Think of any number from 1 to 100, but don't tell me! "
      "Follow the instructions carefully, and I will magically guess your final result!\n")
guessers = [guesser_1,guesser_2,guesser_3,guesser_4]
while True:
    user_num=input("Think Any number from 1 - 100. Type 'yes' to continue Or 'q' to quit: ").lower()
    if user_num=="yes":
        print("Welcome to the game Hold the number in mind lets gets started!!")
        print()
        break
    elif user_num=="q":
        quit()
    else:
        print("Invalid input sorry,Try Again")
        continue
random.choice(guessers)()
print("Good Bye..")