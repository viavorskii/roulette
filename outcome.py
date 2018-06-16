class Outcome:
    def __init__(self, outcome_type, coefficient):
        self.outcome_type = outcome_type
        self.coefficient = coefficient

    def get_won_amount(self, amount):
        return self.coefficient * amount

    def __str__(self):
        return self.outcome_type

    def __repr__(self):
        return "{class_:s}({outcome_type!r}, {coefficient!r})".format(
            class_=type(self).__name__, **vars(self))

