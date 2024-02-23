from ultralytics import YOLO
import cv2

classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']
model = YOLO("playingCards.pt")

def cardsFromImage(imageSource):
    hand = []
    results = model(imageSource, show=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])

            hand.append(classNames[cls])

        hand = list(set(hand))
        print(hand)
        return hand

# results = model("river.jpg", show=True)
# for r in results:
#     boxes = r.boxes
#     for box in boxes:
#         cls = int(box.cls[0])
#
#         hand.append(classNames[cls])
#
#     hand = list(set(hand))
#     print(hand)
#
# cv2.waitKey(0)