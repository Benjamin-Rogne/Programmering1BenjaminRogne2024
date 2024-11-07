import random

def drawCard(cardList):
    print

def dealerDrawCard(cardList):
    print

def wantToPlay():
    print("do you wish to play again?")
    print("y - Yes")
    print("n - No")
    WantToPlayAns = input("Answer: ")
    if WantToPlayAns == "no":
        play = play -1
        print("See you again next time!:)")


play = 1
while play == 1:
    wantToPlay()