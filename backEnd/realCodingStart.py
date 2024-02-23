import detectIMGOnly
import computationClass
river_image = "river.jpg"
hand_image = "hand.jpg"

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

print("hand cards")
detectIMGOnly.cardsFromImage(hand_image)

computation = computationClass.Computation(detectIMGOnly.cardsFromImage(hand_image), detectIMGOnly.cardsFromImage(river_image))
computation.cleanData()
print(handNames[computation.compute_hand()])