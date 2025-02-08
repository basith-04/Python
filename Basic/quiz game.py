#----------------------------
def new_game():
    guesses=[]
    correct=0
    question_num = 1

    for key in question:
        print("----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D:")
        guess = guess.upper()
        guesses.append(guess)
        correct += check_answer(question.get(key),guess)
        question_num += 1
    display_score(correct,guesses)




#----------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0

#----------------------------
def display_score(correct,guesses):
    print("----------------------------")
    print("results")
    print("----------------------------")
    print("answeres :",end="")
    for i in question:
        print(question.get(i),end=" ")
    print()
    print("guesses :", end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score = int((correct/len(question))*100)
    print("your score is ",score)


#----------------------------
def play_again():
    choice = input("do you want to play again ? (yes or no) : ")
    choice = choice.upper()
    if choice == "YES":
        return True
    else:
        return False
#----------------------------

question ={
    "How many districts are in kerala : " : "A",
    "which is the most populated district in kerala : " : "B",#dictionaries
    "Capital of kerala : " : "C",
    "capital of india : " : "A"

}
options = [["A. 14","B. 13","C. 15","D. 12"],
           ["A. Kannur","B. Malappuram","C. Palakkad","D. Kasargod"],
           ["A. Eranakaulam","B. Kozhikode","C. Thiruvananthapuram","D.Kannur"],
           ["A. New Delhi","B. Kerala","C. Karnataka","D. Gujarat"]]#2d list

new_game()

while play_again():
    new_game()

print("thank you for playing ")