from wheel import Wheel
from table import Table
from user import User
from outcome_builder import OutcomeBuilder


class Roulette:
    def __init__(self, table, wheel, users):
        self.table = table
        self.wheel = wheel
        self.users = users

    def run(self):
        table.place_players(self.users)
        table.make_bets()
        bin = self.wheel.run()
        bets = table.get_won_bets(bin)

        self.print_results(bets, bin)

    @staticmethod
    def print_results(bets, bin):
        print ('won types:\n')
        for won_outcome in bin.outcomes:
            print (won_outcome.outcome_type + '\n')

        print ('\nwon bets:\n')
        for bet in bets:
            print(str(bet.user.id) + ' ' + bet.outcome.outcome_type + '\n')


outcome_builder = OutcomeBuilder()
wheel = Wheel(outcome_builder)
table = Table(outcome_builder)
users = []
for i in range(1, 10):
    users.append(User(i))

roulette = Roulette(table, wheel, users)
roulette.run()
