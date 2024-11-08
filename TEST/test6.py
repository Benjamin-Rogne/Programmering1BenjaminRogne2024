class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.name} of {self.suit} (Value: {self.value})"

# Create cards with Ace initially set to 11
drawn_cards = [
    Card("Ace", "Hearts", 11),
    Card("King", "Spades", 10),
    Card("King", "Spades", 1),
    Card("King", "Spades", 10),
]

def calculate_blackjack_total(cards):
    total = sum(card.value for card in cards)
    aces_count = sum(1 for card in cards if card.name == "Ace")
    
    # Adjust total if it's over 21 and we have Aces counted as 11
    while total > 21 and aces_count > 0:
        total -= 10  # Changing one Ace from 11 to 1 reduces total by 10
        aces_count -= 1

    return total

# Calculate and print the best total
total_value = calculate_blackjack_total(drawn_cards)
print(f"Total value of drawn cards: {total_value}")



def playerCardRead(playerDraws):
    print("your current cards are:")
    for cards in playerDraws:
        print(f"{cards.name} of {cards.suit}")
    totalPlayerCardValue = sum(cards.value for card in playerDraws)
    acesCount = sum(1 for card in playerDraws if cards.name == "Ace")
    while totalPlayerCardValue > 21 and acesCount > 0:
        totalPlayerCardValue -= 10
        acesCount -= 1
    print(f"with a total value of {totalPlayerCardValue}")
    #playerRead(totalPlayerCardValue)
