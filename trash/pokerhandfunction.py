def findPokerHand(hand):
    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        if rank == "A": rank = 14
        elif rank == "K": rank = 13
        elif rank == "Q": rank = 12
        elif rank == "J": rank = 11

        ranks.append(int(rank))
        suits.append(suit)

        sortedRanks = sorted(ranks)

    if suits.count(suits[0])==5:
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10)
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)
        else:
            possibleRanks.append(6)

    if all(sortedRanks[i] == sortedRanks[i-1]+1 for i in range(1,len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueValues = list(set(sortedRanks))

    if len(handUniqueValues) == 2:
        for val in handUniqueValues:
            if sortedRanks.count(val) == 4:
                possibleRanks.append(8)
            elif sortedRanks.count(val) == 3:
                possibleRanks.append(7)

    if len(handUniqueValues) == 3:
        for val in handUniqueValues:
            if sortedRanks.count(val) == 3:
                possibleRanks.append(4)
            elif sortedRanks.count(val) == 2:
                possibleRanks.append(3)

    if len(handUniqueValues) == 4:
        possibleRanks.append(2)

    if not possibleRanks:
        possibleRanks.append(1)

    pokerHandRanks = {10:"Royal Flush",9:"Straight Flush",8:"Four of a kind",
                      7:"Full House",6:"Flush",5:"Straight",4:"Three of a kind",
                      3:"Two Pair",2:"Pair",1:"High Card"}
    return pokerHandRanks[max(possibleRanks)]


if __name__ == '__main__':
    findPokerHand(["AH","KH","QH","JH","10H"]) # royal flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # straight flush
