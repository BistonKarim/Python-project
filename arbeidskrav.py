

def main():
    
 login_info()
 quizGame()
    

def login_info():
    userExit = False
    username = 'PGR107'
    password = 'Python'

    while not userExit:
        print("\n-----Welcome to guiz game-----")
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password:")
        if entered_username == username and entered_password == password:
            print("\nLogin successful")
            userExit = True
        else:
            print("Wrong username or password! Please try again")
            
def quizGame():
   
    
    score = 0
    wrongAnswer = 0
    
    
    print("\nPlease answer the guestions by choucing a, b, c, or d:\n")
    #question1
    Q1 = "1: What is the capital of Norway?\n(a) Bergen\n(b) Oslo\n(c) Stavanger\n(d) Trondheim\n:"
    answer1 = input(Q1).strip().lower()
    if answer1 == 'b':
        score += 1
        print("Correct!")
    else:
        wrongAnswer += 1        
        print("Incorrect!\n")
    
    
    #question2
    Q2 = "2: What is the currency of Norway?\n(a) Euro\n(b) Pound\n(c) Krone\n(d) Deutsche Mark\n:"
    answer2 = input(Q2).strip().lower()
    if answer2 == 'c':
        score += 1
        print("Correct!")
    else:
        wrongAnswer += 1
        print("Incorrect!\n")

    
    #question3
    Q3 = "3: Whats is the largest city in Norway?\n(a) Oslo\n(b) Stavanger\n(c) Bergen\n(d) Trondheim\n:"
    answer3 = input(Q3).strip().lower()
    if answer3 == 'a':
        score += 1
        print("Correct!")
    else:
        wrongAnswer += 1
        print("Incorrect!\n")
        
        
     #question4   
    Q4 = "4: When is consitition day  (the national day) of Norway?\n(a) 27th May\n(b) 17th May\n(c) 17th April\n(d) 27th April\n:"
    answer4 = input(Q4).strip().lower()
    if answer4 == 'b':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!\n")


    #question5
    Q5 = "5: What color is the background of the Norwegian flag?\n(a) Red\n(b) White\n(c) Blue\n(d) Yellow\n:"
    answer5 = input(Q5).strip().lower()
    if answer5 == 'a':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!\n") 
    
    
    #question6
    Q6 = "6: How many countries dose Norway border?\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n:"
    answer6 = input(Q6).strip().lower()
    if answer6 == 'c':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!\n")

         
    #question7     
    Q7 = "7: What is the name of the university in Trondheim?\n(a) UiS\n(b) Uio\n(c) NMBU\n(d) NTNU\n:"
    answer7 = input(Q7).strip().lower()
    if answer7 == 'd':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!\n")
 
                
    #question8
    Q8 = "8: How long is the border between Norway and Russia?\n(a) 96 km\n(b) 196 km\n(c) 296 km\n(d) 396 km\n:"
    answer8 = input(Q8).strip().lower()
    if answer8 == 'b':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!\n")


    #question9
    Q9 = "9: Where in Norway is Stavanger?\n(a) North\n(b) South\n(c) South-west\n(d) South-east\n:"
    answer9 = input(Q9).strip().lower()
    if answer9 == 'c':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!\n")


    #question10
    Q10 = "10: From which Norwegian city did the world’s famous composer Edvard Grieg come?\n(a) Oslo\n(b) Bergen\n(c) Stavanger\n(d) Tromsø\n:"         
    answer10 = input(Q10).strip().lower()
    if answer10 == 'b':
         score += 1
         print("Correct!")
    else:
         wrongAnswer += 1
         print("Incorrect!")
    
    print("\n______________________________________________________________\n")    
    print("\nYour right answars is          : ", score, "of 10")
    print("Your wrong answares is         : ", wrongAnswer, "of 10")
    
    
    #Printing those questions which have answred wrong and print the right answer
    if wrongAnswer <=0:
        print("\nYou have answred alle the questions correctly!")
    else:
        print("\n_____________________________________________________________\n",
        "\nCorrect answers to questions that have been answered incorrectly:\n")
        if answer1 != 'b':
            print(Q1)
            print("Your answar:", answer1)
            print("Correct answer is: b (Oslo)\n\n")
        
        if answer2 != 'c':
            print(Q2)
            print("Your answar:", answer2)
            print("Correct answer is: c (Krone)\n")
         
        if answer3 != 'a':
            print(Q3)
            print("Your answar:", answer3)
            print("Correct answer is: a (Oslo)\n\n")
        
        if answer4 != 'b':
            print(Q4)
            print("Your answar:", answer4)
            print("Correct answer is: b (17th May)\n")
        
        if answer5 != 'a':
            print(Q5)
            print("Your answar:", answer5)
            print("Correct answer is: a (Red)\n")    
        
        if answer6 != 'c':
             print(Q6)
             print("Your answar:", answer6)
             print("Correct answer is: c (3)\n")
         
        if answer7 != 'd':
             print(Q7)
             print("Your answar:", answer7)
             print("Correct answer is: d (NTNU)\n")
             
        if answer8 != 'b':
             print(Q8)
             print("Your answar:", answer8)
             print("Correct answer is: b (196 km)\n")
             
        if answer9 != 'c':
             print(Q9)
             print("Your answar:", answer9)
             print("Correct answer is: c (South-west)\n")
             
        if answer10 != 'b':
             print(Q10)
             print("Your answar:", answer10)
             print("Correct answer is: b (Bergen)\n")
        playAgain()
        
def playAgain():
    quit = True
    play = input("Do you want to play again? (Yes) to continue (No) to quit: ").strip().lower()
    while quit:
        if play == 'yes':
            login_info()
            quizGame() 
        elif play == 'no':
            quit = False
        else:
            play = input("Invalid input. Please enter (Yes) to continue or (No) to quit: ").strip().lower()

            
    
       
    
main()