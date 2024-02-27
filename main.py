import cardDetection
import computationClass


# def computeWinner(player1, player2):
#     if player1.compute_hand() > player2.compute_hand():
#         print("Player 1 wins")
#         print("Player 1 wins with a", handNames[player1.compute_hand()], "over a", handNames[player2.compute_hand()])
#     elif player1.compute_hand() < player2.compute_hand():
#         print("Player 2 wins")
#         print("Player 2 wins with a", handNames[player2.compute_hand()], "over a", handNames[player1.compute_hand()])
#     else:
#         print("Tie")
#         print("Both players have a", handNames[player1.compute_hand()])
#     # High card functionality
#     if player1.compute_hand() == 1 and player2.compute_hand() == 1:
#         if player1.high_card() > player2.high_card():
#             print("Player 1 wins with a a high card of", player1.high_card(), "over Player 2 with a high card of", player2.high_card())
#         elif player2.high_card() > player1.high_card():
#             print("Player 2 wins with a high card of", player2.high_card(), "over Player 1 with a high card of", player1.high_card())
#         else:
#             print("PLayer 1 and Player 2 tie with a high card of", player2.high_card())

def computeWinner(*players):
    highestHand = 0
    winners = []
    for player in players:
        if player.compute_hand() > highestHand:
            highestHand = player.compute_hand()
            winners = [player]
        elif player.compute_hand() == highestHand:
            winners.append(player)
    if len(winners) == 1:
        print("Player", winners[0].player_number, "wins with a", handNames[highestHand])
    else:
        print("Tie between players", end=" ")
        for i in range(len(winners)):
            if i == len(winners) - 1:
                print("and", winners[i], end=" ")
            else:
                print(winners[i], end=", ")
        print("with a", handNames[highestHand])





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
cardDetection.cardsFromImage(river_image)

print("hand one cards")
cardDetection.cardsFromImage(hand1_image)

print("hand two cards")
cardDetection.cardsFromImage(hand2_image)


print("------------------------------")
print("Player one data")
player1 = computationClass.Computation(cardDetection.cardsFromImage(hand1_image), cardDetection.cardsFromImage(river_image), 1)
player1.cleanData()
print(handNames[player1.compute_hand()])
print("------------------------------")

print("Player two data")
print("------------------------------")
player2 = computationClass.Computation(cardDetection.cardsFromImage(hand2_image), cardDetection.cardsFromImage(river_image), 1)
player2.cleanData()
print(handNames[player2.compute_hand()])
print("------------------------------")

computeWinner(player1, player2)