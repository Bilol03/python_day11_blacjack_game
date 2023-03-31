import random
from os import system
from art import logo
end_game = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
    random_cards = random.choice(cards)
    return random_cards




# // Calculating Scores

def calculate_score(user_score, comp_score):

    length_user = len(user_score)
    length_comp = len(comp_score)
    score1 = sum(user_score)
    score2 = sum(comp_score)
    print("Your cards are: ", user_score, "current score: ", score1)
    print("Computer's first card is: ", comp_score[0])
    while score1 <= 21:
        add_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if add_card == "y":
            user_score.append(deal_card())
            if user_score[len(user_score) - 1] == 11:
                user_score[len(user_score) - 1] = 1
            score1 = sum(user_score)
            print(f"""Your cards: {user_score}, current score: {score1}
Computer's first card: {comp_score[0]}""")
        else:
            break
    if length_comp == 2 and score2 == 21:
        return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

Computer has blackJack. You win!!
        """
    if length_user == 2 and score1 == 21:
        return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

You have blackJack. You win!
        """
    
    if score1 > 21:
        for i in user_score:
            if i == 11:
                user_score.remove(i)
                i == 1
                user_score.append(i)
            else:
                return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

You went over you lose!
        """
        score1 = sum(user_score)
        print(score1)
        if score1 > 21:
            return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

You went over you lose!
        """
        

    if score2 < 17:
        while score2 < 17:
            comp_score.append(deal_card())
            score2 = sum(comp_score)
        if score2 > 21:
            return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

Computer went over you win!
        """
    if score1 > score2:
        return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

You win!
        """
    elif score1 == score2:
        return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

Draw
        """
    else:
        return f"""Your final hand is: {user_score}, final score: {score1}
Computer's final hand is: {comp_score}, final score: {score2}

Computer wins!
        """



while not end_game:
    user_cards = []
    computer_cards = []

    deal_number = 2

    for deals in range(0, deal_number):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    ask_end_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_end_game == "n":
        end_game = True
    else:
        system("clear")
        print(logo)
        res = calculate_score(user_cards, computer_cards)
        print(res)

