# hand = ["7S", "6S"]
# community = ["5S", "5D", "5H", "2D", "5C"]
hand = ['6C', '9H']
community = ['2H', '10D', '10H', '6S', '7D']

# def getLists(river,playerHand):
#     global hand
#     global community
#     hand = playerHand
#     community = river
#     print("hand: ", hand)
#     print("community: ", community)
# testing lo
class Computation:
    def __init__(self, river, hand):
        self.river = river
        self.hand = hand
    def map_card_value(self, card):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
                  'A': 14}
        return values[card[:-1]]





#
# def map_card_value(card):
#     values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#     return values[card[:-1]]
# # sort the list in numerical order and make all face cards into a numerical value
# def cleanData():
#     global all_cards
#     all_cards = hand + community
#     all_cards.sort(key=lambda x: map_card_value(x))
#     for i, each in enumerate(all_cards):
#         if each[0] in ['J', 'Q', 'K', 'A']:
#             all_cards[i] = str(map_card_value(each)) + each[1]
#
# cleanData()
# print("-------------------")
# print(all_cards)
# print("-------------------")
# # # Straight Flush NOT Done need to map the index of the straight values to the cards
# # def check_straight_flush():
# #     myNums = [int(x[:-1]) for x in all_cards]
# #     for i in range(len(all_cards)-4):
# #         # Checks for a straight
# #         if int(all_cards[i][:-1])+1 in myNums and int(all_cards[i][:-1])+2 in myNums and int(all_cards[i][:-1])+3 in myNums and int(all_cards[i][:-1])+4 in myNums:
# #             # Checks for flush in the cards with straight
# #             if all_cards[i][-1] == all_cards[i+1][-1] == all_cards[i+2][-1] == all_cards[i+3][-1] == all_cards[i+4][-1]:
# #                 return True
# #     return False
#
# # THIS 100 PERCENT WORKS
# def check_flush():
#     suits = [card[-1] for card in all_cards]
#     print("-------------------")
#     for i in range(len(suits)-4):
#         if suits.count(suits[i]) >= 5:
#             return True
#     else:
#         return False
#
# # Straight is done
# def check_straight():
#     # for i in range(len(all_cards)-4):
#     #     if int(all_cards[i][:-1])+4 == int(all_cards[i+4][:-1]):
#     #         return True
#     # return False
#     myNums = [int(x[:-1]) for x in all_cards]
#     for i in range(len(all_cards)-4):
#         if int(all_cards[i][:-1])+1 in myNums and int(all_cards[i][:-1])+2 in myNums and int(all_cards[i][:-1])+3 in myNums and int(all_cards[i][:-1])+4 in myNums:
#             return True
#     return False
# # Four of a kind done
# def four_of_a_kind():
#     numList = [int(x[:-1]) for x in all_cards]
#     for i in range(len(numList)-2):
#         if numList.count(numList[i]) == 4:
#             return True
#     return False
#
#
# # Three of a kind done
# def three_of_a_kind():
#     numList = [int(x[:-1]) for x in all_cards]
#     for i in range(len(numList)-2):
#         if numList.count(numList[i]) == 3:
#             return True
#     return False
# # High card works now
# def high_card():
#     cardNums = [int(x[:-1]) for x in all_cards]
#     return max(cardNums)
#
# # Accounts for pear but not multiple pair in one hand
# def check_pair():
#     numList = [int(x[:-1]) for x in all_cards]
#     # possiblePairs = set()
#     for i in range(len(numList)-1):
#         if numList.count(numList[i]) == 2:
#             # possiblePairs.add(numList[i])
#             return True
#     # if len(possiblePairs) != 0:
#     #     return (True, max(possiblePairs))
#     return False
# # Check Two pair function now works
# def check_two_pair():
#     numList = [int(x[:-1]) for x in all_cards]
#     possiblePairs = set()
#     for i in range(len(numList)-1):
#         if numList.count(numList[i]) == 2:
#             possiblePairs.add(numList[i])
#     if len(possiblePairs) == 2:
#         return True
#     return False
#
# # I think it works now
# def check_full_house():
#     numList = [int(x[:-1]) for x in all_cards]
#     possiblePairs = set()
#     for i in range(len(numList)-1):
#         if numList.count(numList[i]) == 3:
#             possiblePairs.add(numList[i])
#         if numList.count(numList[i]) == 2:
#             possiblePairs.add(numList[i])
#     if len(possiblePairs) == 2:
#         return True
#     return False
#
# def compute_hand():
#     # if check_straight_flush():
#     #     return 9
#     if four_of_a_kind():
#         return 8
#     elif check_full_house():
#         return 7
#     elif check_flush():
#         return 6
#     elif check_straight():
#         return 5
#     elif three_of_a_kind():
#         return 4
#     elif check_two_pair():
#         return 3
#     elif check_pair():
#         return 2
#     # NEED TO FIGURE OUT A WAY TO IMPLEMENT THIS WITH HIGH CARD LATER.
#     return 1
#
#
# print(compute_hand())