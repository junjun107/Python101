# player get two number from list
    # sum the two , as long as the sum is < 21 keep asking if player wants another card
# computer get one number from list
    # if yes, add another number to the list , sum
    # if no, the computer gets another card, if sum is <17, computer gets another card

# A starts to be 11 until player goes over 21
    # sum > 21 Bust
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_random_numbers = random.sample(cards, 2)
player_sum = sum(player_random_numbers)

computer_random_numbers = random.sample(cards, 1)
print(f"Your cards are {player_random_numbers} total is {player_sum}. Computer cards are: {computer_random_numbers}")

while player_sum < 21:
    player_choice = input("Do you want another card? ")
    new_random_number = random.choice(cards)

    if player_choice == 'y':
        player_random_numbers.append(new_random_number)
        player_sum = sum(player_random_numbers)
        print(f"Your new card is {new_random_number}, your have {player_random_numbers}, total is {player_sum} ")
    else:
        computer_random_numbers.append(new_random_number)
        computer_sum = sum(computer_random_numbers)
        if computer_sum < 17:
            computer_random_numbers.append(new_random_number)
            computer_sum = sum(computer_random_numbers)
        print(f"Computer cards are {computer_random_numbers}, total is {computer_sum}")
