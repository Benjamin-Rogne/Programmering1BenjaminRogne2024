def wantToPlay(play):
    print("do you wish to play again?")
    print("y - Yes")
    print("n - No")
    WantToPlayAns = input("Answer: ")
    if WantToPlayAns == "no":
        play = play - 1
        print("See you again next time!:)")
    return play
    

while wantToPlay(1) == 1:
    print