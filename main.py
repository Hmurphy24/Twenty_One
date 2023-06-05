import random

twenty_one_card_dictionary = {'Ace': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

twenty_one_score_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}


def twenty_one_rules():

    print()

    print('Welcome to 21! Try and get as close to 21 as possible!')

    print()

    print('If you go over 21 you lose! The same applies if the computer goes over 21, then it loses!')

    print('The deck will be shuffled an indicated amount of times and will be distributed between you and the computer.')

    print('When prompted, type either you want a card or not, the player with the highest number wins! (Given that you didn\'t bust!)')

    print()

    print('Good luck!')

    print()


def twenty_one_deck_maker():

    twenty_one_entire_card_deck = []

    twenty_one_suit_deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    twenty_one_deck_counter = 0

    while twenty_one_deck_counter < 4:

        for card in twenty_one_suit_deck:

            twenty_one_entire_card_deck.append(card)

        twenty_one_deck_counter += 1

    while True:

        twenty_one_times_shuffled = input('How many times do you want the deck to be shuffled? ')

        if twenty_one_times_shuffled.isdigit():

            twenty_one_shuffles = int(twenty_one_times_shuffled)

            break

        else:

            print('Type in an integer!')

            print()

    print('The deck will be shuffled {} time(s)!'.format(twenty_one_shuffles))

    while twenty_one_shuffles > 0:

        random.shuffle(twenty_one_entire_card_deck)

        twenty_one_shuffles -= 1

    return twenty_one_entire_card_deck


def twenty_one_gameplay(card_deck):

    twenty_one_user_hand = []

    twenty_one_computer_hand_hidden = []

    twenty_one_computer_hand_visible = []

    twenty_one_first_card = 0

    while twenty_one_first_card < 2:

        twenty_one_user_hand.append(card_deck[0])

        card_deck.remove(card_deck[0])

        twenty_one_computer_hand_hidden.append(card_deck[0])

        card_deck.remove(card_deck[0])

        twenty_one_first_card += 1

    twenty_one_computer_hand_visible.append(twenty_one_computer_hand_hidden[0])

    twenty_one_computer_hand_visible.append('X')

    print()

    print('Your Hand:')

    print(twenty_one_user_hand)

    print()

    print('Computer\'s Hand:')

    print(twenty_one_computer_hand_visible)

    print()

    twenty_one_user_hand_value = 0

    for card in twenty_one_user_hand:

        if card == 'Ace':

            while True:

                twenty_one_ace_value = input('Do you want your Ace to have a value of 1 or 11? ')

                if twenty_one_ace_value.isdigit():

                    if (twenty_one_ace_value == '1') or (twenty_one_ace_value == '11'):

                        twenty_one_user_hand_value = twenty_one_user_hand_value + int(twenty_one_ace_value)

                        break

                    else:

                        print('The value has to be 1 or 11!')

                        print()

                else:

                    print('Type in either "1" or "11".')

                    print()

        else:

            twenty_one_user_hand_value = twenty_one_user_hand_value + twenty_one_card_dictionary[card]

    twenty_one_computer_hand_value = 0

    for card in twenty_one_computer_hand_hidden:

        if card == 'Ace':

            if twenty_one_computer_hand_value <= 10:

                twenty_one_computer_hand_value = twenty_one_computer_hand_value + 11

            else:

                twenty_one_computer_hand_value = twenty_one_computer_hand_value + 1

        else:

            twenty_one_computer_hand_value = twenty_one_computer_hand_value + twenty_one_card_dictionary[card]

    twenty_one_user_stay_counter = 0

    twenty_one_computer_stay_counter = 0

    while True:

        if (twenty_one_user_stay_counter == 1) and (twenty_one_computer_stay_counter == 1):

            print('Okay, you and the computer both want to stay!')

            print()

            break

        if twenty_one_user_hand_value == 21:

            print('You got 21! Congrats!')

            print()

            break

        elif twenty_one_user_hand_value > 21:

            print('You went over 21! You busted!')

            print()

            break

        else:

            print('Your hand\'s current value is {}.'.format(twenty_one_user_hand_value))

            print()

            while True:

                twenty_one_user_input = input('Do you want to draw a card? ("Yes"/"No") ')

                if twenty_one_user_input.upper() == 'YES':

                    print('You drew a card!')

                    print()

                    twenty_one_card_draw = card_deck[0]

                    twenty_one_user_hand.append(twenty_one_card_draw)

                    card_deck.remove(twenty_one_card_draw)

                    if twenty_one_card_draw == 'Ace':

                        while True:

                            twenty_one_ace_value = input('Do you want your Ace to have a value of 1 or 11? ')

                            if twenty_one_ace_value.isdigit():

                                if (twenty_one_ace_value == '1') or (twenty_one_ace_value == '11'):

                                    twenty_one_user_hand_value = twenty_one_user_hand_value + int(twenty_one_ace_value)

                                    break

                                else:

                                    print('The value has to be 1 or 11!')

                                    print()

                            else:

                                print('Type in either "1" or "11".')

                                print()

                    else:

                        twenty_one_user_hand_value = twenty_one_user_hand_value + twenty_one_card_dictionary[twenty_one_card_draw]

                        break

                elif twenty_one_user_input.upper() == 'NO':

                    twenty_one_user_stay_counter = 1

                    print('Okay, you decided to stay.')

                    print()

                    break

                else:

                    print('Please enter either "Yes" or "No".')

                    print()

        if twenty_one_computer_hand_value == 21:

            print('The computer got 21!')

            print()

            break

        elif twenty_one_computer_hand_value > 21:

            print('The computer busted!')

            print()

            break

        elif 16 <= twenty_one_computer_hand_value <= 20:

            twenty_one_computer_stay_counter = 1

            print('The computer decided to stay!')

            print()

        else:

            print('The computer drew a card!')

            twenty_one_computer_hand_hidden.append(card_deck[0])

            twenty_one_computer_hand_value = twenty_one_computer_hand_value + twenty_one_card_dictionary[card_deck[0]]

            card_deck.remove(card_deck[0])

            twenty_one_computer_hand_visible.append('X')

            print()

        print('Your Hand:')

        print(twenty_one_user_hand)

        print()

        print('Computer\'s Hand:')

        print(twenty_one_computer_hand_visible)

        print()

        if (twenty_one_user_stay_counter == 1) and (twenty_one_computer_stay_counter == 1):

            print('Okay, you and the computer both want to stay!')

            print()

            break

    print('Ending Hands:')

    print()

    print('Your Hand:')

    print(twenty_one_user_hand)

    print('Hand value: {}'.format(twenty_one_user_hand_value))

    print()

    print('Computer\'s Hand:')

    print(twenty_one_computer_hand_hidden)

    print('Hand value: {}'.format(twenty_one_computer_hand_value))

    print()

    return twenty_one_user_hand_value, twenty_one_computer_hand_value


def twenty_one_replay(user_value, computer_value):

    if (user_value > 21) and (computer_value > 21):

        print('You and the computer both busted!')

        print()

        twenty_one_score_dictionary['Ties'] += 1

    elif user_value == computer_value:

        print('You tied with the computer!')

        print()

        twenty_one_score_dictionary['Ties'] += 1

    elif (user_value < 22) and (computer_value > 21):

        print('You win since the computer busted!')

        print()

        twenty_one_score_dictionary['Wins'] += 1

    elif (user_value < 22) and (computer_value < 22) and (user_value > computer_value):

        print('You won since you had a higher score than the computer!')

        print()

        twenty_one_score_dictionary['Wins'] += 1

    elif (user_value > 21) and (computer_value < 22):

        print('You lost since you busted!')

        print()

        twenty_one_score_dictionary['Losses'] += 1

    elif (user_value < 22) and (computer_value < 22) and (computer_value > user_value):

        print('You lost since the computer had a higher score than you!')

        print()

        twenty_one_score_dictionary['Losses'] += 1

    print('Here\'s the score:')

    print(twenty_one_score_dictionary)

    print()

    while True:

        twenty_one_replay_input = input('Would you like to play again? ("Yes"/"No") ')

        if twenty_one_replay_input.upper() == 'YES':

            print('Okay, let\'s go again!')

            print()

            break

        elif twenty_one_replay_input.upper() == 'NO':

            print('Okay, have a good day!')

            print()

            exit()

        else:

            print('Please type either "Yes" or "No"!')

            print()


twenty_one_rules()

while True:

    twenty_one_gameplay_deck = twenty_one_deck_maker()

    twenty_one_hand_values = twenty_one_gameplay(twenty_one_gameplay_deck)

    twenty_one_score_dictionary['Games Played'] += 1

    twenty_one_replay(twenty_one_hand_values[0], twenty_one_hand_values[1])
