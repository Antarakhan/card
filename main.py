from module.Chips import Chips
from module.Deck import Deck
from module.Hand import Hand
playing = True


def take_bet(chips):
    while True:
        try:
            bet = int(input("How many chips would you like to bet?"))
            chips.bet = bet
        except ValueError:
            print('Please enter a number')
        else:
            if chips.bet > chips.total:
                print("Not enough. You only have {} chips remaining".format(chips.total))
            else:
                break


def hit(deck, hand):
    dealedCard = deck.deal_one()
    hand.add_card(dealedCard)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    userSelection = input("Hit or stand? Enter h or s")

    while True:
        if userSelection == 'h':
            hit(deck, hand)
            playing = True
        elif userSelection == 's':
            playing = False
        else:
            print("Please enter h or s only")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')  # or a loop


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(chips):
    print("BUST DEALER!")
    chips.lose_bet()


def dealer_wins(chips):
    print("DEALER WINS!")
    chips.win_bet()


def push():
    print('Dealer and player tie! PUSH')


print("Blackjack game")

# Create & shuffle the deck, deal two cards to each player
deck = Deck()
deck.shuffle_deck()

# Set up the Player's chips
player = Hand()
dealer = Hand()

for card in range(2):
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())

# Prompt the Player for their bet
player_chips = Chips()
take_bet(player_chips)

show_some(player, dealer)

while playing:
    hit_or_stand(deck, player)
    show_some(player, dealer)

    # If Player hand exceeds 21, then busted and break loop
    if player.value > 21:
        player_busts(player_chips)
        break

# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
if player.value <= 21:
    while dealer.value < player.value:
        hit(deck, dealer)

    show_all(player, dealer)

    # Run different winning scenarios
    if dealer.value > 21:
        dealer_busts(player_chips)

    elif dealer.value > player.value:
        dealer_wins(player_chips)
    elif dealer.value < player.value:
        player_wins(player_chips)
    else:
        push()


