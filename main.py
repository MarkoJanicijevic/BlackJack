from functions import *



print("Welcome to the BlackJack Game!")





def deal():
    user_cards.append(deal_random_card())

    user_number_cards = picture_to_number_list(user_cards)
    computer_number_cards = picture_to_number_list(computer_cards)
    user_sum = sum(user_number_cards)

    if 11 in user_number_cards and user_sum > 21:
        user_number_cards.remove(11)
        user_number_cards.append(1)
        user_sum = sum(user_number_cards)

    print(f"Your cards are {user_cards}, your current score is {user_sum}")
    print(f"Computer's card is {computer_cards}")


    if check_blackjack(user_sum):
        print(user_cards)
        print("It's a blackjack! You won!")
    else:
        if check_bust(user_sum):
            print(user_cards)
            print("It's a bust. You loose.")
        else:
            hit_stand = input("Hit or stand? \n").lower()
            if hit_stand == "hit":
                deal()
            else:
                comp_sum = sum(computer_number_cards)
                while comp_sum < 16:
                    computer_cards.append(deal_random_card())
                    computer_number_cards = picture_to_number_list(computer_cards)
                    comp_sum = sum(computer_number_cards)
                if check_bust(comp_sum):
                    print(f"Your cards are {user_cards}.")
                    print(f"Computer's cards are {computer_cards}. ")
                    print("Computer have it over 21. You won.")
                else:
                    if comp_sum > user_sum:
                        print(f"Your cards are {user_cards}.")
                        print(f"Computer's cards are {computer_cards}. ")
                        print("You lost, game over.")
                    elif comp_sum == user_sum:
                        print(f"Your cards are {user_cards}.")
                        print(f"Computer's cards are {computer_cards}. ")
                        print("It's a draw. ")
                    else:
                        print(f"Your cards are {user_cards}.")
                        print(f"Computer's cards are {computer_cards}. ")
                        print("You won, game over.")








game_is_on = True

while game_is_on:

    user_cards = [deal_random_card()]
    computer_cards = [deal_random_card()]

    deal()

    new_game = input("Do you want to play again? y/n \n")

    if new_game == "y":
        game_is_on = True
    else:
        game_is_on = False


