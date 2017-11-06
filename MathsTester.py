import random
import time
import datetime
import pickle
from operator import itemgetter


questions = ['q1', 'q2', 'q3']
selection = " "
marks = 0
high_scores = []

def menu():
    global selection
    print(
    """
\n\nWelcome to the Maths Tester for Kids program. This program has been developed to test your knowledge of maths.
\nCan you become the best at Maths out of all your friends....

Only the Maths Tester will tell...

Please enter a number to select an option out of the following:

1. Take the Maths Tester timed quiz

2. View the Leaderboard

3. Exit the game
    """
    )
    selection = input("\nPlease enter in your desired option: ")
    return selection

def test(): #questions
    question = 0
    global marks
    global high_scores
    print(
    """\n\n
You are about to asked a variety of questions. You have 1 minute to answer them all.

For each question you answer you will receive 1 point.

At the end you will have the option to answer a bonus question.

Your goal is to get the highest score possible by answering all the questions before the time is up.\n
    """
    )
        
    name = input("Please enter in your name and press enter to play: ")
    while len(name)>10: #if name is bigger than 10 characters, it will bring up an error message and prompt again
        print("\nThe name you entered has too many characters, please enter a shorter name (less than 10 characters)")
        name = input("\nPlease enter in your name and press enter to play: ") 
    now = datetime.datetime.now() #the time now
    nowPlus1 = now + datetime.timedelta(minutes = 1) #the time 1 minute from now
    while question < 10: 
        question+=1
        if question == 1: #question1
            print(
            """
\n\nWhich pair equals to 1.0?

1) 0.1       0.99
2) 0.11      0.9
3) 0.01      0.999
4) 0.91      0.09
5) 0.001     0.09
            """
            )
            question1 = int(input("\nEnter in the number of the pair from 1 - 5: ")) 
            if datetime.datetime.now() < nowPlus1: # Compares the time now to the time 1 minute from the start of the first question, if the time now is greater. The game will stop
                if question1 == 4:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")

            else:
                question = question + 10
                print("\n\n You have run out of time!")
        elif question == 2: #question 2
            print(
            """
\n\nJohn has 15 shirts:

    5 are black
    3 are white
    3 are red
    2 are dark blue
    1 is light blue
    1 is yellow

He is going to pick one at random
            """
            )
            question2 = input("\nWhat is the probability that the t-shirt will not be black? (enter as a simplified fraction): ")
            if datetime.datetime.now() < nowPlus1:
                if question2 == "2/3":
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\n You have run out of time!")
        elif question == 3: #question 3
            print(
            """
\n\nZak has 3/4 of a litre in a jug and pours it into another jug with millilitre measurements.
            """
            )
            question3 = int(input("\nHow many millilitres does he have?: ")) 
            if datetime.datetime.now() < nowPlus1:
                if question3 == 750:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\n You have run out of time!")
                    
        elif question == 4: #question 4
            print(
            """
\n\nKim has boxes which are all cubes of the same size.

She uses four of the boxes to make a pile with a height of 72cm.

She puts one more box on top of the pile.
            """
            )
            question4 = int(input("\nWork out the height of the pile of five boxes: "))
            if datetime.datetime.now() < nowPlus1:
                if question4 == 90:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\n You have run out of time!")
                    
        elif question == 5: #question 5
            question5 = int(input("\nWork out 15% of 360: "))
            if datetime.datetime.now() < nowPlus1:
                if question5 == 54:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
               question = question + 10
               print("\n\nYou have run out of time!")
                   
        elif question == 6: #question 6
            print(
            """
\n\n11 = 6 + a

a + 7 = 10 + b
            """
            )
            question6 = int(input("\nUse both equations to work out the value of b: "))
            if datetime.datetime.now() < nowPlus1:
                if question6 == 2:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\nYou have run out of time!")
                    
        elif question == 7: #question 7
            print(
            """
\n\nGary took part in a quiz show and won a million pounds.

He spent £20000 on a holiday.

Then he spent half of the money left on a house.

            """
            )
            question7 = int(input("\nHow much did Gary’s house cost? (only enter in the number): "))
            if datetime.datetime.now() < nowPlus1:
                if question7 == 490000:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\nYou have run out of time!")

    
        elif question == 8: #question 8
            print(
            """
\n\n27/40 = 0.675

29/40 = 0.725

            """
            )
            question8 = float(input("\nUse the above information to write the missing decimals for 31/40: "))
            if datetime.datetime.now() < nowPlus1:
                if question8 == 0.875:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\nYou have run out of time!")
                

        elif question == 9: #question 9
            print(
            """
\nIn this question, n stands for any whole number.

1. 2n must be odd
2. 2n must be even
3. 3n could be odd or even

            """
            )
            question9 = int(input("\nWhich statement is correct from 1-3: "))
            if datetime.datetime.now() < nowPlus1:
                if question9 == 3:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\nYou have run out of time!")

        elif question == 10: #question 10
            print(
            """

\n\nA necklace has 4 beads:
    3 beads are white
    1 bead is black

This gives the necklace a 1 : 3 ratio of black beads to white beads
            """
            )
            question10 = int(input("\nHow many more black beads do you need to add to make the ratio of black to white 3 : 1?: "))
            if datetime.datetime.now() < nowPlus1:
                if question10 == 8:
                    print("\nCorrect! 1 mark gained")
                    marks+=1
                else:
                    print("\nIncorrect!")
            else:
                question = question + 10
                print("\n\nYou have run out of time!")

        else:
            print("\nSorry no question could be generated")

    question = 0 #reset question number
    print("""
\n\nYou now have the chance for a bonus question.
If you get the question right, your mark will be doubled.
If you get it wrong your score will be halfed to the nearest full mark.
You will not have a time limit to answer this question.\n
         """
         )
    bonus = input("\n\nWould you like to play a bonus round? y/n: ") #bonus question
    if bonus != "n":
        random.shuffle(questions) #selects a random number from the list questions
        if questions[0] == 'q1':
            bonusQuestion1 = int(input("\n\nWhat is the difference between 3x3 and 3x3x3?: "))
            if bonusQuestion1 == 18:
                print("\nCorrect! Points doubled!")
                marks*=2 #points doubled
            else:
                print("\nIncorrect! Points halved")
                marks = round(marks/2)  #half and round if bonus question is wrong
        elif questions[0] == 'q2':
            print(
            """
\n\nThe mean of five numbers is 10

I add one more number and the mean is now 11    

            """
            )
            bonusQuestion2 = int(input("\nWhat number did I add?: "))
            if bonusQuestion2 == 16:
                print("\nCorrect! Points doubled!")
                marks*=2
            else:
                print("\nIncorrect! Points halved")
                marks = round(marks/2)

            
        elif questions[0] == 'q3':
            print(
            """
\n\ny = 1

1. 3 + y
2. 10 - y
3. y x y
4. 3 x y
5. 2 / y

            """
            )
            bonusQuestion3 = int(input("\nWhich expression has the largest value? (1-5): "))
            if bonusQuestion3 == 2:
                print("\nCorrect! Points doubled!")
                marks*=2
            else:
                print("\nIncorrect! Points halved")
                marks = round(marks/2)
                    
        
        
    print("\n\nYou have completed the test, your final score is",marks)

    high_scores.append((name, marks)) #pickle, adds to the end of a list the names and marks
    high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10] # descending, only saves the top 10 onto the file, itemgetter(1)


    with open('highscores.txt', 'ab') as f: #opens the file for appending in binary. Pointer is at the end to be able to add to the end of the program
        pickle.dump(high_scores, f) 



def hScores(): #displays top 10 high scores
    global high_scores
    print("\n\n The top 10 all time scores:\n\n")
    d = {}
    with open('highscores.txt', 'rb') as f: #unpickle
        while True: #while loop to call all the values until there is an EOFError
            try:
                high_scores = pickle.load(f)
            except EOFError:
                break
            else:
                d.update(high_scores) #updates the highscores
        if len(high_scores) == 1:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
        elif len(high_scores) == 2:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
        elif len(high_scores) == 3:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
        elif len(high_scores) == 4:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
        elif len(high_scores) == 5:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
            print("\t5.",high_scores[4][0],"-",high_scores[4][1])
        elif len(high_scores) == 6:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
            print("\t5.",high_scores[4][0],"-",high_scores[4][1])
            print("\t6.",high_scores[5][0],"-",high_scores[5][1])
        elif len(high_scores) == 7:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
            print("\t5.",high_scores[4][0],"-",high_scores[4][1])
            print("\t6.",high_scores[5][0],"-",high_scores[5][1])
            print("\t7.",high_scores[6][0],"-",high_scores[6][1])
        elif len(high_scores) == 8:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
            print("\t5.",high_scores[4][0],"-",high_scores[4][1])
            print("\t6.",high_scores[5][0],"-",high_scores[5][1])
            print("\t7.",high_scores[6][0],"-",high_scores[6][1])
            print("\t8.",high_scores[7][0],"-",high_scores[7][1])
        elif len(high_scores) == 9:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
            print("\t5.",high_scores[4][0],"-",high_scores[4][1])
            print("\t6.",high_scores[5][0],"-",high_scores[5][1])
            print("\t7.",high_scores[6][0],"-",high_scores[6][1])
            print("\t8.",high_scores[7][0],"-",high_scores[7][1])
            print("\t9.",high_scores[8][0],"-",high_scores[8][1])
        elif len(high_scores) == 10:
            print("\tName:")
            print("\t1.",high_scores[0][0],"-",high_scores[0][1])
            print("\t2.",high_scores[1][0],"-",high_scores[1][1])
            print("\t3.",high_scores[2][0],"-",high_scores[2][1])
            print("\t4.",high_scores[3][0],"-",high_scores[3][1])
            print("\t5.",high_scores[4][0],"-",high_scores[4][1])
            print("\t6.",high_scores[5][0],"-",high_scores[5][1])
            print("\t7.",high_scores[6][0],"-",high_scores[6][1])
            print("\t8.",high_scores[7][0],"-",high_scores[7][1])
            print("\t9.",high_scores[8][0],"-",high_scores[8][1])
            print("\t10.",high_scores[9][0],"-",high_scores[9][1])
        else:
            print("There are not any scores currently saved!")

def exitGame(): #exits game
    print("\n\nThank you for playing")

def main(): #main program
    global marks
    menu()
    while selection!= "3":
        if selection == "1":
            test()
            marks = 0
            input("\n\nPress enter to go back to menu")
            menu()
        elif selection == "2":
            hScores()
            input("\n\nPress enter to go back to menu")
            menu()
        else:
            print("\n\nSorry that is not an option")
            menu()
    exitGame()

#main code
main()
input("\n\nPress enter to exit")

        
