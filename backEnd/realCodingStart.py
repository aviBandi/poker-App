import detectIMGOnly
import computationClass


def computeWinner(player1, player2):
    if player1.compute_hand() > player2.compute_hand():
        print("Player 1 wins")
        print("Player 1 wins with a", handNames[player1.compute_hand()], "over a", handNames[player2.compute_hand()])
    elif player1.compute_hand() < player2.compute_hand():
        print("Player 2 wins")
        print("Player 2 wins with a", handNames[player2.compute_hand()], "over a", handNames[player1.compute_hand()])
    else:
        print("Tie")
        print("Both players have a", handNames[player1.compute_hand()])

river_image = "river.jpg"
hand1_image = "hand1.jpg"
hand2_image = "hand2.jpg"

handNames = {8: "Four of a Kind",
             7: "Full House",
             6: "Flush",
             5: "Straight",
             4: "Three of a Kind",
             3: "Two Pair",
             2: "Pair",
             1: "High Card"}

print("river cards")
detectIMGOnly.cardsFromImage(river_image)

print("hand one cards")
detectIMGOnly.cardsFromImage(hand1_image)

print("hand two cards")
detectIMGOnly.cardsFromImage(hand2_image)


print("------------------------------")
print("Player one data")
player1 = computationClass.Computation(detectIMGOnly.cardsFromImage(hand1_image), detectIMGOnly.cardsFromImage(river_image))
player1.cleanData()
print(handNames[player1.compute_hand()])
print("------------------------------")

print("Player two data")
print("------------------------------")
player2 = computationClass.Computation(detectIMGOnly.cardsFromImage(hand2_image), detectIMGOnly.cardsFromImage(river_image))
player2.cleanData()
print(handNames[player2.compute_hand()])
print("------------------------------")

computeWinner(player1, player2)