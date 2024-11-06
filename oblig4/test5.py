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
aS = playingCard("Ace", "Spades", 11 or 1)
aH = playingCard("Ace", "Hearts", 11 or 1)
aD = playingCard("Ace", "Diamonds", 11 or 1)
aC = playingCard("Ace", "Clubs", 11 or 1)

print (f"you derew a {aC.name} of {aC.suit} and got a value of {aC.value}")

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
print(cards)