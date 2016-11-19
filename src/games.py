import random
from numpy import matrix


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

class PrisonersDilemma:
    R = 3
    T = 5
    S = 1
    P = 2

    gamma = None

    EXPECTED_PAYOFF_MATRIX = matrix([ [R/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma)],
                               [T/(1-gamma), P/(1-gamma), T + P*gamma/(1-gamma), S + T*gamma/(1-gamma)],
                               [R/(1-gamma), S + P*gamma/(1-gamma), R/(1-gamma), (S + P*gamma + T*gamma**2 + R*gamma**3)/(1-gamma**4)],
                               [T/(1-gamma), T + S*gamma/(1-gamma), (T + P*gamma + S*gamma**2 + R*gamma**3)/(1-gamma**4), (P+R*gamma)/(1-gamma**2)]] )