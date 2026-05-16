import random #importing random module to generate computer's choice

options=("rock","paper","scissors")#defining the options for the game

while True:
    user_input= input("enter you choice (rock, paper, scissors) or 'q' to quit: ").lower()
#game logic
    if user_input=="q":
        print("thanks for playing!")
        break
    if user_input not in options:
        print("invalid choice, try again.")
        continue #if user input is not in options then it will ask user to enter again
    auto_choice=random.choice(options)

    print(f"Computer chose: {auto_choice}")
    print(f"You chose: {user_input}")
    print("--------RESULT-------")
#winner logic
    if user_input==auto_choice:#checking for tie
        print("It's a tie!")
    elif (user_input=="rock"and auto_choice=="scissors"
        )or(user_input=="paper"and auto_choice=="rock"
        ) or(user_input=="scissors"and auto_choice=="paper"):
        print("You win!")
    else:
        print("Computer wins!")
#score tracking computer and user score tracking
#if computer win score is add on computer score and if user win score is add on user score
    score=0
    if user_input==auto_choice:
        score+=0
    elif (user_input=="rock"and auto_choice=="scissors"
        )or(user_input=="paper"and auto_choice=="rock"
        ) or(user_input=="scissors"and auto_choice=="paper"):
        score+=1
    else:
        score-=1

print(f"Your score: {score}") 
print(f"Computer score: {-score}")#computer score is negative of user score because when user wins computer loses and vice versa
print("Game over!")
