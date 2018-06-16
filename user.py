from random import randint
from bet import Bet


class User:
    MIN_BET = 1
    MAX_BET = 100

    def __init__(self, i):
        self.id = i

    def generate_bet(self, outcome_builder):
        amount = randint(self.MIN_BET, self.MAX_BET)
        outcome = outcome_builder.get_random_outcome()

        return Bet(outcome, amount, self)