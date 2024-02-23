import detectIMGOnly
import main

river_image = "river.jpg"
hand_image = "hand.jpg"

print("river cards")
detectIMGOnly.cardsFromImage(river_image)

print("hand cards")
detectIMGOnly.cardsFromImage(hand_image)

# main.getLists(detectIMGOnly.cardsFromImage(river_image), detectIMGOnly.cardsFromImage(hand_image))
# print(main.compute_hand())