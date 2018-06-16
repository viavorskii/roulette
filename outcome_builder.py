from outcome import Outcome
import random


class OutcomeBuilder:
    OUTCOME_00 = '00'
    OUTCOME_0 = '0'
    OUTCOME_1 = '1'
    OUTCOME_2 = '2'
    OUTCOME_3 = '3'
    OUTCOME_4 = '4'
    OUTCOME_5 = '5'
    OUTCOME_6 = '6'
    OUTCOME_RED = 'red'
    OUTCOME_GREEN = 'green'
    OUTCOME_LINE = 'line'
    OUTCOME_FIVE = 'five'

    AVAILABALE_OUTCOMES = {
        OUTCOME_00: 40,
        OUTCOME_0: 40,
        OUTCOME_1: 40,
        OUTCOME_2: 40,
        OUTCOME_3: 40,
        OUTCOME_4: 40,
        OUTCOME_5: 40,
        OUTCOME_6: 40,
        OUTCOME_RED: 10,
        OUTCOME_GREEN: 10,
        OUTCOME_LINE: 20,
        OUTCOME_FIVE: 10
    }

    def __init__(self):
        self.outcomes = {}

    def get_outcome(self, name):
        if name in self.outcomes:
            return self.outcomes[name]
        elif name in self.AVAILABALE_OUTCOMES:
            self.outcomes[name] = Outcome(name, self.AVAILABALE_OUTCOMES[name])
            return self.outcomes[name]
        else:
            raise Exception(name + ' outcome is not found')

    def get_random_outcome(self):
        return self.get_outcome(
            random.choice(
                self.AVAILABALE_OUTCOMES.keys()
            )
        )

