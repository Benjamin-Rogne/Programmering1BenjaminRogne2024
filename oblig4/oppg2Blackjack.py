import random

#gjør klar chips og lister osv...
gameRound = 0
global bigScore
bigScore = 100
playerChips = 100
playerCardsList = []
dealerCardsList = []

#klasse for spillkort alle kortene deklareres nedover med navn type og tall/verdi
class playingCard:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

#2
twoS = playingCard("Two", "Spades", 2)
twoH = playingCard("Two", "Hearts", 2)
twoD = playingCard("Two", "Diamonds", 2)
twoC = playingCard("Two", "Clubs", 2)

#3
threeS = playingCard("Three", "Spades", 3)
threeH = playingCard("Three", "Hearts", 3)
threeD = playingCard("Three", "Diamonds", 3)
threeC = playingCard("Three", "Clubs", 3)

#4
fourS = playingCard("Four", "Spades", 4)
fourH = playingCard("Four", "Hearts", 4)
fourD = playingCard("Four", "Diamonds", 4)
fourC = playingCard("Four", "Clubs", 4)

#5
fiveS = playingCard("Five", "Spades", 5)
fiveH = playingCard("Five", "Hearts", 5)
fiveD = playingCard("Five", "Diamonds", 5)
fiveC = playingCard("Five", "Clubs", 5)

#6
sixS = playingCard("Six", "Spades", 6)
sixH = playingCard("Six", "Hearts", 6)
sixD = playingCard("Six", "Diamonds", 6)
sixC = playingCard("Six", "Clubs", 6)

#7
sevenS = playingCard("Seven", "Spades", 7)
sevenH = playingCard("Seven", "Hearts", 7)
sevenD = playingCard("Seven", "Diamonds", 7)
sevenC = playingCard("Seven", "Clubs", 7)

#8
eightS = playingCard("Eight", "Spades", 8)
eightH = playingCard("Eight", "Hearts", 8)
eightD = playingCard("Eight", "Diamonds", 8)
eightC = playingCard("Eight", "Clubs", 8)

#9
nineS = playingCard("Nine", "Spades", 9)
nineH = playingCard("Nine", "Hearts", 9)
nineD = playingCard("Nine", "Diamonds", 9)
nineC = playingCard("Nine", "Clubs", 9)

#10
tenS = playingCard("Ten", "Spades", 10)
tenH = playingCard("Ten", "Hearts", 10)
tenD = playingCard("Ten", "Diamonds", 10)
tenC = playingCard("Ten", "Clubs", 10)

#JACK
jS = playingCard("Jack", "Spades", 10)
jH = playingCard("Jack", "Hearts", 10)
jD = playingCard("Jack", "Diamonds", 10)
jC = playingCard("Jack", "Clubs", 10)

#QUEEN
qS = playingCard("Queen", "Spades", 10)
qH = playingCard("Queen", "Hearts", 10)
qD = playingCard("Queen", "Diamonds", 10)
qC = playingCard("Queen", "Clubs", 10)

#KING
kS = playingCard("King", "Spades", 10)
kH = playingCard("King", "Hearts", 10)
kD = playingCard("King", "Diamonds", 10)
kC = playingCard("King", "Clubs", 10)

#ACE
aS = playingCard("Ace", "Spades", 11)
aH = playingCard("Ace", "Hearts", 11)
aD = playingCard("Ace", "Diamonds", 11)
aC = playingCard("Ace", "Clubs", 11)

#liste over all kortene i kortstokken
cards = [twoS, twoH, twoD, twoC,
         threeS, threeH, threeD, threeC,
         fourS, fourH, fourD, fourC,
         fiveS, fiveH, fiveD, fiveC,
         sixS, sixH, sixD, sixC,
         sevenS, sevenH, sevenD, sevenC,
         eightS, eightH, eightD, eightC,
         nineS, nineH, nineD, nineC,
         tenS, tenH, tenD, tenC,
         jS, jH, jD, jC,
         qS, qH, qD, qC,
         kS, kH, kD, kC,
         aS, aH, aD, aC]

#leser av og summerer kortene som spilleren trekker
def playerCardRead(playerDraws):
    print("")
    print("your current cards are:")
    global totalPlayerCardValue
    for card in playerDraws:
        print(f"{card.name} of {card.suit}")
    totalPlayerCardValue = sum(card.value for card in playerDraws)
    acesCount = sum(1 for card in playerDraws if card.name == "Ace")
    while totalPlayerCardValue > 21 and acesCount > 0:
        totalPlayerCardValue -= 10
        acesCount -= 1
    print(f"with a total value of {totalPlayerCardValue}")
    if totalPlayerCardValue <= 20 :
        hitOrStand()
    return totalPlayerCardValue
    
#leser dealer trekk og summerer verdiene på kortene
def dealersCardRead(dealerDraws):
    global totalDealerCardValue
    print("")
    print("the dealers current cards are:")
    for card in dealerDraws:
        print(f"{card.name} of {card.suit}")
    totalDealerCardValue = sum(card.value for card in dealerDraws)
    countAces = sum(1 for card in dealerDraws if card.name == "Ace")
    while totalDealerCardValue > 21 and countAces > 0:
        totalDealerCardValue -= 10
        countAces -= 1
    print(f"with a total value of {totalDealerCardValue}")
    return totalDealerCardValue

#leser av delers første trekk og sier hva det er verdt
def dealersfirstCardRead(dealerDraws):
    print("")
    print("the dealers current known card is:")
    for cards in dealerDraws:
        print(f"{cards.name} of {cards.suit}")
    totalDealerCardValue = sum(cards.value for card in dealerDraws)
    print(f"with a total value of {totalDealerCardValue}")
    print("")

#trekker kort og fjerner kortet fra bunken
def drawCard(cardList):
    index = random.randrange(len(cardList))
    selectedCard = cardList.pop(index)
    return selectedCard

#denne funksjonen trekker fra chips dersom du taper
def playerLoseRound():
    global playerChips
    print(f"You lost {playerBet} chips")
    print("")
    playerChips = playerChips - playerBet
    if playerChips <= 0:
        playerLose()

#denne funkjonen skjer etter du har gått tom for chips
def playerLose():
    print("")
    print("    GAME OVER!")
    print("you ran out of chips")
    print("")
    print("this games higest score")
    score = highScore()
    print(f"  was {score} chips")
    print("")

#funksjon for hit eller stand 
def hitOrStand():
    ans = False
    stand = False
    while ans == False:
        print("")
        print("")
        print("Hit or Stand?")
        print("h - Hit")
        print("s - Stand")
        hitOrStandAns = input("Answer: ")
        print("")
        if hitOrStandAns == "h":
            playerDrawCard(cardList)
            playerCardRead(playerCards)
            ans = True
        elif hitOrStandAns == "s":
            ans = True
            stand = True
    return stand

#funksjon som spilles når du får blackjack  
def blackJack():
    global playerChips
    print("")
    print("     BLACKJACK")
    print("you doubled your reward")
    print("")
    playerChips = playerChips + (playerBet*2)
    return playerChips

#når du vinner på normalt vis legger denne funksjonen til chips du betta
def playerWin():
    global playerChips
    print("")
    print("      YOU WIN!")
    print(f"you earnd {playerBet} chips")
    playerChips = playerChips + playerBet

#denne funkjonen gjir beskjed om at runden var uavgjort og at ingen mister chips
def noWinners():
    print("")
    print("   It is a draw  ")
    print("you keep your chips")
    print("")
#dealer legger kortet til i lista si og fjerner det fra trekkebunken
def dealerDrawCard(cards):
    dealerCards.append(drawCard(cards))
    return dealerCards
#spiller legger kortet til i lista si og fjerner det fra trekkebunken
def playerDrawCard(cardList):
    playerCards.append(drawCard(cardList))
    return playerCards

#funksjon for utskrif av dealers kort og verdi er på kortene
def dealerDraw17(cardList, dealerCards):
        totalDealerCardValue = 0
        totalDealerCardValue = dealersCardRead(dealerCards)
        while totalDealerCardValue <= 17:
            dealerCards.append(drawCard(cardList))  # Trekker et nytt kort og legger til dealerens kort
            totalDealerCardValue = dealersCardRead(dealerCards)

#skal tracke høyeste score du har hatt dette gamet
def highScore():
    global bigScore
    if playerChips > bigScore:
        bigScore = playerChips
    return bigScore

#her er det en rekke funksjoner for de forskjellige utfallene av spillet
def winConditionCheck():
    if totalPlayerCardValue > 21:
        print("")
        print("You got busted")
        playerLoseRound()
        print("")
    elif totalPlayerCardValue == 21:
        blackJack()
    else:
        dealerDraw17(cardList, dealerCards)
        if totalDealerCardValue > 21:
            playerWin()
        elif totalPlayerCardValue > totalDealerCardValue:
            playerWin()
        elif totalPlayerCardValue < totalDealerCardValue:
            print("")
            print("  YOU LOSE!")
            playerLoseRound()
            print("")
        elif totalPlayerCardValue == totalDealerCardValue:
            noWinners()
        else:
            print("error")

#funksjon for å bette chips
def chipBet():
    global playerBet
    global playerChips
    bet = False
    while bet == False:
        print("")
        print(f"you have {playerChips} chips")
        print(f"how many do you wanna bet?")
        playerBet = int(input("Answer: "))
        print("")
        if playerBet > 0 and playerBet <= playerChips:
            bet = True
            return playerBet
        elif playerBet == 0:
            bet = False
            print("")
            print(f"you can not bet 0 Chips")
            print(f"Unvalid bet please try again")
            print("")
        elif playerBet > playerChips:
            bet = False
            print("")
            print(f"you can not bet more Chips than what you have")
            print(f"Unvalid bet please try again")
            print("")
        else:
            print("")
            print(f"please chose a hole number")
            print(f"Unvalid bet please try again")
            print("")


#spørr spiller etter hvert fullført spill med gjenværende chips om de vil spille mer
def wantToPlay(play):
    ans = False
    while ans == False:
        print("")
        print("do you want to play?")
        print("y - Yes")
        print("n - No")
        wantToPlayAns = input("Answer: ")
        if wantToPlayAns == "n":
            play = play - 1
            print("")
            print("Good bye see you again next time!")
            print("")
            print("this games higest score")
            score = highScore()
            print(f"was {score} chips")
            ans = True
        elif wantToPlayAns == "y":
            play = play
            ans = True
        else:
            print("")
            print("Unvalid answer please try again")
    return play

while wantToPlay(1) == 1:
    #kopierer lister for at bonken og de kortene spillerene trekker skal resette hver runde
    cardList = cards.copy()
    playerCards = playerCardsList.copy()
    dealerCards = dealerCardsList.copy()

    #teller hvor mange runder du har spillt starter på runde 1
    gameRound = gameRound + 1
    print("")
    print (f"Round {gameRound}")
    
    chipBet()
    #her trekkes kortene til dealer kun det første er synlig frem til etter spiller velger stand
    dealerDrawCard(cardList)
    dealersfirstCardRead(dealerCards)
    dealerDrawCard(cardList)
    
    #trekker de 2 første kortene for spiller derretter får man valget mellom hit og stand
    playerDrawCard(cardList)
    playerDrawCard(cardList)
    playerCardRead(playerCards)

    winConditionCheck()
    highScore()
    if playerChips == 0:
        print("   Good Bye")
        print("")
        break
        #dersom spiller ikke har flere chips vil spillet avslutte automatisk