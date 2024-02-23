import detectIMGOnly
import computationClass
river_image = "river.jpg"
hand_image = "hand.jpg"

print("river cards")
detectIMGOnly.cardsFromImage(river_image)

print("hand cards")
detectIMGOnly.cardsFromImage(hand_image)

computation = computationClass.Computation()
computation.cleanData()
print(computation.compute_hand())