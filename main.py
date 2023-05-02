import json
import requests
from random import shuffle
from termcolor import cprint


# prints welcome message
cprint("Welcome to Onyeali's football quiz game\n", "green", 'on_red',attrs=['reverse', 'blink'])
cprint("Test your knowledge about sports\n\n", "blue",attrs=['blink'])
# get user name
userName = input("What is your name? ")
# check that name is valid
if not userName.isalpha():
    cprint("Enter a valid name!\n", "red",attrs=['bold'])
    userName = input("What is your name? ")
else:
    cprint(f"Welcome,{userName}!\n\n", "blue",attrs=['bold'])

    cprint(f"Let's play!{userName}\n","red")
    games = []
    play = "Y"
    while play == "Y":   
    
        # gets data from API
        questions_url = "https://opentdb.com/api.php?amount=10&category=21"
        data = requests.get(questions_url)
        questions = data.content.decode()

        questions_dict = json.loads(questions)
        questions_list = questions_dict["results"]

        num_correct = 0
        quest_num = 1
        while quest_num <= len(questions_list):
          # get question and options
          row = questions_list[quest_num-1] 
          question = row['question']
          answer = row['correct_answer']
          options = row['incorrect_answers'] + [answer]
          shuffle(options)
          question_type = row["type"]

          # print question and options
          cprint(f"Question {quest_num}: {question}", "yellow",attrs=['bold'])
          options_list_dict = {
            "multiple": ["A", "B", "C", "D"],
            "boolean":["A", "B"]
          }
          options_list = options_list_dict[question_type]
          options_dict = dict(zip(options_list, options))
          for e, f in options_dict.items():
              cprint(f"{e}. {f}", "magenta",attrs=['bold'])

          # get user input and check if it's correct
          user_ans = input("\nEnter one of the options: ").upper()
          if user_ans in options_list:
              user_answ = options_dict[user_ans]

              if user_answ == answer:
                  cprint('Correct answer!', "blue",attrs=['bold'])  
                  num_correct += 1
              else:
                  cprint('Oops! Wrong answer', "white",attrs=['bold'])
              cprint(f'The correct answer is {answer}.\n', "cyan",attrs=['bold'])
              quest_num += 1
          else:
            cprint("Enter a valid opption!\nA,B,C or D\n", "blue",attrs=['bold'])
            continue
                  

        cprint(f'final score {num_correct * 10 }%', "yellow",attrs=['bold'])
        cprint(f'You got a total of {num_correct} questions', "blue",attrs=['bold'])
        cprint(f'You failed {quest_num - 1 - num_correct}.', "red",attrs=['bold'])
        games.append(num_correct * 10)
        play = input("Do you want to play again ?\n Enter Y,else press any key to end the game:  ").upper()

    else:
        print("\n-----Scores-----")
        for ind, game in enumerate(games):
          
           print(f"Game {ind+1}: {game}%\n")
        print("\n---------------")
        cprint("Bye!\n Thanks for playing!", "magenta",attrs=['bold'])  

      
    

          