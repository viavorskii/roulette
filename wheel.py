from outcome_builder import OutcomeBuilder
import random
from bin import Bin


class Wheel:
    BINS_DEFINITION = {
        '00': [OutcomeBuilder.OUTCOME_FIVE, OutcomeBuilder.OUTCOME_00],
        '0': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_0, OutcomeBuilder.OUTCOME_RED],
        '1': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_1, OutcomeBuilder.OUTCOME_RED],
        '2': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_2, OutcomeBuilder.OUTCOME_RED],
        '3': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_3, OutcomeBuilder.OUTCOME_GREEN],
        '4': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_4, OutcomeBuilder.OUTCOME_GREEN],
        '5': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_5, OutcomeBuilder.OUTCOME_GREEN],
        '6': [OutcomeBuilder.OUTCOME_LINE, OutcomeBuilder.OUTCOME_6, OutcomeBuilder.OUTCOME_GREEN],
    }

    def __init__(self, outcome_builder):
        self.outcome_builder = outcome_builder

    def run(self):
        key = random.choice(self.BINS_DEFINITION.keys())
        outcomes = []
        for outcome_name in self.BINS_DEFINITION[key]:
            outcomes.append(self.outcome_builder.get_outcome(outcome_name))

        return Bin(outcomes)