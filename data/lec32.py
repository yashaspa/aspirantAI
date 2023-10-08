class Card:

    rankval = {
            'A':14,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            # ...
            'J':11,
            'Q':12,
            'K':13}
    '''
    '''
    def __init__(self, r, s):
        self.rank = r
        self.suit = s


    def __repr__(self):
        return self.rank + " of " + self.suit

    def __lt__(self, other):
        '''support the < operator on Cards'''
        myval = Card.rankval[self.rank]
        otherval = Card.rankval[other.rank]
        return myval < otherval

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ['A','2','3', '4', '5',
                    '6', '7', '8', '9', '10',
                    'J', 'Q', 'K']:
            for suit in ['Spades', 'Clubs',
                    'Diamonds', 'Hearts']:
                c = Card(rank, suit)
                self.cards.append(c)




def main():
    '''
    '''
    c1 = Card('3', 'Spades')
    c2 = Card('4', 'Hearts')

    if c1 < c2:
        print('c1 is less than c2.')

    print(c1)
    print(c2)

if __name__ == '__main__':
    main()
