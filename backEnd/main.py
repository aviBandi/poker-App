hand = ["5C", "7S"]
community = ["5S", "10D", "2S", "10H", "5D"]

def map_card_value(card):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card[:-1]]
# sort the list in numerical order and make all face cards into a numerical value
def cleanData():
    global all_cards
    all_cards = hand + community
    all_cards.sort(key=lambda x: map_card_value(x))
    for i, each in enumerate(all_cards):
        if each[0] in ['J', 'Q', 'K', 'A']:
            all_cards[i] = str(map_card_value(each)) + each[1]

cleanData()
print(all_cards)
# Straight Flush Done
def check_straight_flush():
    for i in range(len(all_cards)-4):
        # Checks for a straight
        print(all_cards[i][:-1], all_cards[i + 4][:-1])
        if int(all_cards[i][:-1])+4 == int(all_cards[i+4][:-1]):
            # Checks for flush in the cards with straight
            if all_cards[i][-1] == all_cards[i+1][-1] == all_cards[i+2][-1] == all_cards[i+3][-1] == all_cards[i+4][-1]:
                return True
    return False

# THIS 100 PERCENT WORKS
def check_flush():
    suits = [card[-1] for card in all_cards]

    for i in range(len(suits)-4):
        print(suits[i], end=" ")
        if suits.count(suits[i]) == 5:
            return True
    else:
        return False

# Straight is done
def check_straight():
    for i in range(len(all_cards)-4):
        if int(all_cards[i][:-1])+4 == int(all_cards[i+4][:-1]):
            return True
    return False
# Four of a kind done
def four_of_a_kind():
    numList = [int(x[:-1]) for x in all_cards]
    print(numList)
    for i in range(len(numList)-2):
        if numList.count(numList[i]) == 4:
            return True
    return False


# Three of a kind done
def three_of_a_kind():
    numList = [int(x[:-1]) for x in all_cards]
    print(numList)
    for i in range(len(numList)-2):
        if numList.count(numList[i]) == 3:
            return True
    return False
# High card works now
def high_card():
    cardNums = [int(x[:-1]) for x in all_cards]
    return max(cardNums)

# Accounts for pear but not multiple pair in one hand
def check_pair():
    numList = [int(x[:-1]) for x in all_cards]
    # possiblePairs = set()
    print(numList)
    for i in range(len(numList)-1):
        if numList.count(numList[i]) == 2:
            # possiblePairs.add(numList[i])
            return True
    # if len(possiblePairs) != 0:
    #     return (True, max(possiblePairs))
    return False
# Check Two pair function now works
def check_two_pair():
    numList = [int(x[:-1]) for x in all_cards]
    print(numList)
    possiblePairs = set()
    for i in range(len(numList)-1):
        if numList.count(numList[i]) == 2:
            possiblePairs.add(numList[i])
    if len(possiblePairs) == 2:
        return True
    return False

# I think it works now
def check_full_house():
    numList = [int(x[:-1]) for x in all_cards]
    print(numList)
    possiblePairs = set()
    for i in range(len(numList)-1):
        print(numList[i], end=" ")
        if numList.count(numList[i]) == 3:
            possiblePairs.add(numList[i])
        if numList.count(numList[i]) == 2:
            possiblePairs.add(numList[i])
    print(possiblePairs)
    if len(possiblePairs) == 2:
        return True
    return False


print(check_full_house())