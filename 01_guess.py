import random
arrayone = ["happy", "lions", "parul", "shark", "right"]
word = random.choice(arrayone)
letter = word[0]
print("The secret word beings with the letter %s" % (letter))

count = 0
while count<1:
    asking = input("Type in a five letter word:" )
    if len(asking) == 5 and asking[0] != letter:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    elif asking == "":
        print("You wasted a guess =P")
        count = count + 1
    elif len(asking) > 5 or len(asking)<5:
        print("0,1,2,3,4 that is how we count to 5")
        count = count + 1
    elif word == asking:
        print("Good Job! You are one with the source.")
        break
    elif len(asking) == 5 and asking[0] == letter:
        print("You used %s guesses left" % (count))

