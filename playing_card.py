# 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
# 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
# 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
# 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'
# playing card unicode: https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
import random
def playing_card():
    suit = '\u2660', '\u2665', '\u2666', '\u2663'
    #print(suit)
    #rank = 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    rank = list('A123456789') + ['10'] + list('JQK')
    # print(rank)
    deck = []  #save information is list
    for i in suit :
        for j in rank :
            deck.append(j + i) #that is add information
    return deck


d = playing_card()
print(d) 
random.shuffle(d)
print(d)
p = random.sample(d, 7) #that is select card random 7 cards
print(p)