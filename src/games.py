import random


STRATEGIES = ["AC", "AD", "TfT", "NTfT"]


# Template Game class
class Game:
    # ACTIONS = ["C", "D"]
    # payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (1, 5),
    #                  ("D", "C"): (5, 1), ("D", "D"): (2, 2)}
    #
    # def opposite_action(self, action):
    #     if action == self.ACTIONS[0]:
    #         return self.ACTIONS[1]
    #     elif action == self.ACTIONS[1]:
    #         return self.ACTIONS[0]
    #     else:
    #         print("uhoh! unexpected action:", action)
    #         return None

    ##### INCLUDE:
    # EXPECTED_PAYOFF_MATRIX
    # R,P,S,T values
    # H/W for battle of the sexes

    def __init__(self, gamma):
        self.gamma = gamma


# A basic agent has a strategy
class Agent:

    def __init__(self, initial_strategy):
        self.strategy = initial_strategy
        # score for most recent round
        self.score = 0
        # for battle of sexes: gender-strategy
