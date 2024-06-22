import random

#get system desition
choices_list = ["rock","paper","scissors"]
system_choice=random.choices(choices_list)
system_choice_str=("".join(system_choice))
print(system_choice_str)

#get input from player 
user = input("choose : ""rock"" , ""paper"" or  ""scissors""  :  ")
use_answer = user
# print(answer , system_choice_str)

#guess who win 
# if system choose rock
def Check_2 (answer):
    if system_choice_str == "rock" and use_answer == "paper" :
        print("YOU WIN !!!!!")
    elif system_choice_str == "rock" and use_answer == "scissors" :
        print("YOU Lose !!!!!")
    # if system choose paper
    elif system_choice_str =="paper" and use_answer == "rock":
        print("YOU Lose !!!")
    elif system_choice_str =="paper" and use_answer == "scissors":
        print("YOU WIN !!!")
    # if system choose scissors
    elif system_choice_str == "scissors" and use_answer == "rock" :
        print("YOU WIN !!!")
    elif system_choice_str == "scissors" and use_answer == "paper" :
        print("YOU Lose !!!")

    # if both of them be same 
    def check (answer):
        
        if system_choice_str == use_answer :
            print(answer)
    check("TIE !!!") 


#     if use_answer != ["rock , scissors , paper"] :
#         print(answer)
# Check_2("plz enter correct value")