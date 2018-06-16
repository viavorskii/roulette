class Table:
    def __init__(self, outcome_builder):
        self.bets = []
        self.outcome_builder = outcome_builder
        self.users = []

    def place_bet(self, bet):
        self.bets.append(bet)

    def place_player(self, user):
        self.users.append(user)

    def place_players(self, users):
        self.users.extend(users)

    def make_bets(self):
        for user in self.users:
            self.bets.append(user.generate_bet(self.outcome_builder))

    def get_won_bets(self, bin):
        bets = []
        for bet in self.bets:
            for outcome in bin.outcomes:
                if bet.outcome.outcome_type == outcome.outcome_type:
                    bets.append(bet)
                    break
        return bets

