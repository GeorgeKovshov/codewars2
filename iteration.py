usernames = ("Rainer", "Alfons", "Flatsheep")
iter1 = usernames.__iter__()
print(iter1.__next__())
print(iter1.__next__())

iter2 = iter(usernames)
print(next(iter2))

usernames2 = ["Rainer", "Alfons", "Flatsheep"]
looper = iter(usernames2)
print()
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break

class Portfolio:
    def __init__(self):
        self.holdings = {}  # Key = ticker, Value = number of shares

    def buy (self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(selfself, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())

p = Portfolio()
p.buy('Alpha', 15)
p.buy('Beta', 23)
p.buy('Gamma', 9)
p.buy('Gamma', 20)

print(p.holdings.get("Gamma"))

import itertools

ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [card for card in itertools.product(ranks, suits)]

for (index, card) in enumerate(deck):
    print(1 + index, card)

hands = [hand for hand in itertools.combinations(deck, 5)]

print(f"The number of 5-card poker hands is {len(hands)}.")


