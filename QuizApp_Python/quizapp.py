print("Welcome to All")

player=input("Do you want Play?:")

if player.lower() != "yes":
    quit()

print("ok lets Play!")

score=0

question=input("How many days do we have in a week?")

if question.lower() =="seven":
    print("Correct")
    score=score+1

else:
    print("Incorrect")

question=input("In which direction does the sun rise?")

if question.lower() =="east":
    print("Correct")
    score=score+1
else:
    print("Incorrect")

question=input("What is our national bird?")

if question.lower() =="peacock":
    print("Correct")
    score=score+1
else:
    print("Incorrect")

question=input("Which is the fastest animal on the land?")

if question.lower() =="cheetah":
    print("Correct")
    score=score+1
else:
    print("Incorrect")

question=input("Which is the largest ocean in the world?")

if question.lower() =="pacific Ocean":
    print("Correct")
    score=score+1
else:
    print("Incorrect")

print("Your Score "+str(score))
print("Correct Answer is:\n 1.Seven\n 2.East\n 3.Peacock\n 4.Cheetah\n 5.Pacific Ocean\n")

      
