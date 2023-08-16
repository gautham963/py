import requests
import json
import random
import pprint
import html

url = "https://opentdb.com/api.php?amount=1"
endGame = ""

score_correct = 0
score_incorrect = 0

while endGame != "quit":
    data_valid = False
    r = requests.get(url)
    r.status_code
    if(r.status_code !=  200):
        endGame = input("Sorrt there was an error on retreiving the page, If you want to try again press enter else type 'quit' to quit")
    else:
        answer_nos = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question),"\n")

        for answer in answers:
            print(str(answer_nos) +":-"+answer)
            answer_nos += 1
            
        while data_valid == False:
            user_ans = input("Enter your number of choice: ")
            try:
                user_ans = int(user_ans)
                if user_ans > len(answers) or user_ans <= 0:
                    print("Invalid, choose from the givn answers")
                else:
                    data_valid = True
            except:
                print("Invalid, only numbers")
        user_ans = answers[int(user_ans)-1]

        if user_ans == correct_answer:
            print("CORNGRASS "+correct_answer+" is the right option")
            score_correct += 1
        else:
            print("OOPS, wrong answer, the correct answer is: ",correct_answer)
            score_incorrect += 1

        print("*************************")
        print("Your score is: \n")
        print("Correct answer: ",str(score_correct))
        print("Incorrect answer: ",str(score_incorrect))
        print("***************************")
        endGame = input("Enter to continue else type 'quit' to quit\n")
print("THANK U FOR PLAYING")





