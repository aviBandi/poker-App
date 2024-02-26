class Computation:
    def __init__(self, hand, river):
        self.hand = hand
        self.river = river
        self.all_cards = []

    def map_card_values(self, card):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
                  'A': 14}
        return values[card[:-1]]

    def cleanData(self):

        self.all_cards = self.hand + self.river
        self.all_cards.sort(key=lambda x: self.map_card_values(x))
        for i, each in enumerate(self.all_cards):
            if each[0] in ['J', 'Q', 'K', 'A']:
                self.all_cards[i] = str(self.map_card_values(each)) + each[1]


        print("-------------------")
        print(self.all_cards)
        print("-------------------")
    # ------------------------------------------
    # ------------------------------------------
    # ------------------------------------------
    # NEED TO CREATE A STRAIGHT FLUSH THAT WORKS
    # ------------------------------------------
    # ------------------------------------------
    # ------------------------------------------
    def check_flush(self):
        suits = [card[-1] for card in self.all_cards]
        print("--------------------------")
        for i in range(len(suits) - 4):
            if suits.count(suits[i]) >= 5:
                return True
        else:
            return False

    def check_straight(self):
        # for i in range(len(all_cards)-4):
        #     if int(all_cards[i][:-1])+4 == int(all_cards[i+4][:-1]):
        #         return True
        # return False
        myNums = [int(x[:-1]) for x in self.all_cards]
        for i in range(len(self.all_cards) - 4):
            if int(self.all_cards[i][:-1]) + 1 in myNums and int(self.all_cards[i][:-1]) + 2 in myNums and int(
                    self.all_cards[i][:-1]) + 3 in myNums and int(self.all_cards[i][:-1]) + 4 in myNums:
                return True
        return False

    def check_full_house(self):
        three_of_a_kind = False
        two_of_a_kind = False
        numList = [int(x[:-1]) for x in self.all_cards]
        uniqueNumList = list(set(numList))
        for i in range(len(uniqueNumList)):
            if numList.count(uniqueNumList[i]) == 3:
                three_of_a_kind = True
            if numList.count(uniqueNumList[i]) == 2:
                two_of_a_kind = True
        if three_of_a_kind == True and two_of_a_kind == True:
            return True
        return False

    def four_of_a_kind(self):
        numList = [int(x[:-1]) for x in self.all_cards]
        for i in range(len(numList) - 2):
            if numList.count(numList[i]) == 4:
                return True
        return False

    def three_of_a_kind(self):
        numList = [int(x[:-1]) for x in self.all_cards]
        for i in range(len(numList) - 2):
            if numList.count(numList[i]) == 3:
                return True
        return False

    def check_two_pair(self):
        numList = [int(x[:-1]) for x in self.all_cards]
        possiblePairs = set()
        for i in range(len(numList) - 1):
            if numList.count(numList[i]) == 2:
                possiblePairs.add(numList[i])
        if len(possiblePairs) == 2:
            return True
        return False

    def high_card(self):
        cardNums = [int(x[:-1]) for x in self.all_cards]
        return max(cardNums)

    def compute_hand(self):
        # if check_straight_flush():
        #     return 9
        if self.four_of_a_kind():
            return 8
        elif self.check_full_house():
            return 7
        elif self.check_flush():
            return 6
        elif self.check_straight():
            return 5
        elif self.three_of_a_kind():
            return 4
        elif self.check_two_pair():
            return 3
        elif self.check_pair():
            return 2
        return 1



if __name__ == "__main__":
    hand = ['6C', '9H']
    community = ['2H', '10D', '10H', '6S', '7D']
    object1 = Computation(hand, community)
    object1.cleanData()
    print(object1.compute_hand())