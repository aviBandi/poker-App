hand = ['6C', '9H']
community = ['2H', '10D', '10H', '6S', '7D']


class Computation:
    def __init__(self, hand, river):
        self.hand = hand
        self.river = river

    def map_card_values(self, card):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
                  'A': 14}
        return values[card[:-1]]

    def cleanData(self):
        global all_cards
        all_cards = self.hand + self.river
        all_cards.sort(key=lambda x: self.map_card_values(x))
        for i, each in enumerate(all_cards):
            if each[0] in ['J', 'Q', 'K', 'A']:
                all_cards[i] = str(self.map_card_values(each)) + each[1]
        print("-------------------")
        print(all_cards)
        print("-------------------")



object1 = Computation(hand, community)
object1.cleanData()