import random


def deal_card(card_list):
  random_cards = random.choice(card_list)
  return random_cards

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#  deal cards

user_cards = []
computer_cards = []

deal_number = 2

for deals in range(0, deal_number):
  user_cards.append(deal_card(cards))
  computer_cards.append(deal_card(cards))

print("Your cards are: ", user_cards)
print("Computer's first card is: ", computer_cards[0])