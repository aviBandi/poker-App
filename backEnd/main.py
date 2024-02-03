
# Need to use a string method first to have a string of the card value and suit. Then need to do a card[:1] to get the first digit letter
def map_card_value(value):
    if value.isdigit():
        return int(value)
    elif value == 'A':
        return 14
    elif value == 'K':
        return 13
    elif value == 'Q':
        return 12
    elif value == 'J':
        return 11
    else:
        raise ValueError("Invalid card value")


# def check_straight_flush(hand, community):
#     all_cards = hand + community
#     all_cards.sort(key=lambda x: map_card_value(x[0]))
#     for i in range(len(all_cards) - 4):
#         if all_cards[i][1] == all_cards[i+4][1]:
#             straight_flush = True
#             for j in range(i, i+4):
#                 if map_card_value(all_cards[j][0]) != map_card_value(all_cards[j+1][0]) - 1:
#                     straight_flush = False
#                     break
#             if straight_flush:
#                 return True
#     return False


#
# def check_four_of_a_kind(hand, community):
#     all_cards = hand + community
#     all_cards.sort(key=lambda x: map_card_value(x[0]))
#     for i in range(len(all_cards) - 3):
#         if map_card_value(all_cards[i][0]) == map_card_value(all_cards[i+3][0]):
#             return True
#     return False
#
# def check_full_house(hand, community):
#     all_cards = hand + community
#     all_cards.sort(key=lambda x: map_card_value(x[0]))
#     three_of_a_kind = False
#     pair = False
#     for i in range(len(all_cards) - 2):
#         if map_card_value(all_cards[i][0]) == map_card_value(all_cards[i+2][0]):
#             three_of_a_kind = True
#             break
#     for i in range(len(all_cards) - 1):
#         if map_card_value(all_cards[i][0]) == map_card_value(all_cards[i+1][0]) and map_card_value(all_cards[i][0]) != map_card_value(all_cards[i+2][0]):
#             pair = True
#             break
#     if three_of_a_kind and pair:
#         return True
#     return False
#
# # The rest of the code remains the same...
#
# def check_flush(hand, community):
#     all_cards = hand + community
#     suits = [card[1] for card in all_cards]
#     for suit in suits:
#         if suits.count(suit) >= 5:
#             return True
#     return False
#
# def check_straight(hand, community):
#     all_cards = hand + community
#     all_cards.sort()
#     for i in range(len(all_cards) - 4):
#         straight = True
#         for j in range(i, i+4):
#             if all_cards[j][0] != all_cards[j+1][0] - 1:
#                 straight = False
#                 break
#         if straight:
#             return True
#     return False
#
# def check_three_of_a_kind(hand, community):
#     all_cards = hand + community
#     all_cards.sort()
#     for i in range(len(all_cards) - 2):
#         if all_cards[i][0] == all_cards[i+2][0]:
#             return True
#     return False
#
# def check_two_pair(hand, community):
#     all_cards = hand + community
#     all_cards.sort()
#     pairs = 0
#     for i in range(len(all_cards) - 1):
#         if all_cards[i][0] == all_cards[i+1][0]:
#             pairs += 1
#     if pairs >= 2:
#         return True
#     return False
#
# def check_one_pair(hand, community):
#     all_cards = hand + community
#     all_cards.sort()
#     for i in range(len(all_cards) - 1):
#         if all_cards[i][0] == all_cards[i+1][0]:
#             return True
#     return False
#
# def evaluate_hand(hand, community):
#     if check_straight_flush(hand, community):
#         return "Straight Flush"
#     elif check_four_of_a_kind(hand, community):
#         return "Four of a Kind"
#     elif check_full_house(hand, community):
#         return "Full House"
#     elif check_flush(hand, community):
#         return "Flush"
#     elif check_straight(hand, community):
#         return "Straight"
#     elif check_three_of_a_kind(hand, community):
#         return "Three of a Kind"
#     elif check_two_pair(hand, community):
#         return "Two Pair"
#     elif check_one_pair(hand, community):
#         return "One Pair"
#     else:
#         return "High Card"
#
def main():
    community_cards = []
    for i in range(5):
        card = input(f"Enter community card {i+1} (e.g., '10H' for 10 of Hearts): ").upper()
        # community_cards.append((int(card[:-1]), card[-1]))
        community_cards.append(card)

    player_hand = []
    for i in range(2):
        card = input(f"Enter your hand card {i+1} (e.g., '10H' for 10 of Hearts): ").upper()
        player_hand.append(card)
        # player_hand.append((int(card[:-1]), card[-1]))

    # hand_rank = evaluate_hand(player_hand, community_cards)
    # print(f"\nYour hand is: {hand_rank}")
    print(community_cards)
    print(player_hand)
if __name__ == "__main__":
    main()
