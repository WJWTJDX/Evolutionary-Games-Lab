import random
from sys import exit
from numpy import matrix
import matplotlib.pyplot as plt


STRATEGIES = ["AC", "AD", "TfT", "NTfT"]

gamma = .99


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

    def __init__(self, gamma):
        self.gamma = gamma

    R = 3
    T = 5
    S = 1
    P = 2
    # Rows in order of 0:AC 1:AD 2:TFT 3:NTFT
    # Cols in order of 0:AC 1:AD 2:TFT 3:NTFT
    EXPECTED_PAYOFF_MATRIX = matrix([ [R/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma)],
                               [T/(1-gamma), P/(1-gamma), T + P*gamma/(1-gamma), S + T*gamma/(1-gamma)],
                               [R/(1-gamma), S + P*gamma/(1-gamma), R/(1-gamma), (S + P*gamma + T*gamma**2 + R*gamma**3)/(1-gamma**4)],
                               [T/(1-gamma), T + S*gamma/(1-gamma), (T + P*gamma + S*gamma**2 + R*gamma**3)/(1-gamma**4), (P+R*gamma)/(1-gamma**2)]] )

class StagHunt:
    R = 5
    T = 3
    S = 1
    P = 3
    # Rows in order of 0:AC 1:AD 2:TFT 3:NTFT
    # Cols in order of 0:AC 1:AD 2:TFT 3:NTFT
    EXPECTED_PAYOFF_MATRIX = matrix([ [R/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma)],
                               [T/(1-gamma), P/(1-gamma), T + P*gamma/(1-gamma), S + T*gamma/(1-gamma)],
                               [R/(1-gamma), S + P*gamma/(1-gamma), R/(1-gamma), (S + P*gamma + T*gamma**2 + R*gamma**3)/(1-gamma**4)],
                               [T/(1-gamma), T + S*gamma/(1-gamma), (T + P*gamma + S*gamma**2 + R*gamma**3)/(1-gamma**4), (P+R*gamma)/(1-gamma**2)]] )

    def __init__(self, gamma):
        self.gamma = gamma

class BattleOfTheSexes:
    R = 3
    T = 5
    S = 1
    P = 2
    #Rows in order of 0:H_AC, 1:H_AD, 2:H_TFT, 3:H_NTFT, 4:W_AC, 5:W_AD, 6:W_TFT, 7:W_NTFT
    #Cols in order of 0:H_AC, 1:H_AD, 2:H_TFT, 3:H_NTFT, 4:W_AC, 5:W_AD, 6:W_TFT, 7:W_NTFT
    EXPECTED_PAYOFF_MATRIX = matrix([ [P/(1-gamma), S/(1-gamma), P/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma)],
                                      [P/(1-gamma), R/(1-gamma), P + R*gamma/(1-gamma), R + P*gamma/(1-gamma), P/(1-gamma), T/(1-gamma), P + T*gamma/(1-gamma), T + P*gamma/(1-gamma)],
                                      [P/(1-gamma), S + R*gamma/(1-gamma), P/(1-gamma), (S+R*gamma+P*gamma**2+P*gamma**3)/(1-gamma**4), R/(1-gamma), S + T*gamma/(1-gamma), R/(1-gamma), (S+T*gamma+P*gamma**2+R*gamma**3)/(1-gamma**4)],
                                      [P/(1-gamma), R + S*gamma/(1-gamma), (P+R*gamma+S*gamma**2+P*gamma**3)/(1-gamma**4), (R+P*gamma)/(1-gamma**2), P/(1-gamma), T + S*gamma/(1-gamma), (P+T*gamma+S*gamma**2+R*gamma**3)/(1-gamma**4), (T+R*gamma)/(1-gamma**2)],
                                      [T/(1-gamma), P/(1-gamma), T/(1-gamma), P/(1-gamma), R/(1-gamma), P/(1-gamma), R/(1-gamma), P/(1-gamma)],
                                      [S/(1-gamma), R/(1-gamma), S + R*gamma/(1-gamma), R + S*gamma/(1-gamma), S/(1-gamma), P/(1-gamma), S + P*gamma/(1-gamma), P + S*gamma/(1-gamma)],
                                      [T/(1-gamma), P + R*gamma/(1-gamma), T/(1-gamma), (P+R*gamma+S*gamma**2+T*gamma**3)/(1-gamma**4), R/(1-gamma), P/(1-gamma), R/(1-gamma), (P+P*gamma+S*gamma**2+R*gamma**3)/(1-gamma**4)],
                                      [S/(1-gamma), R + P*gamma/(1-gamma), (S+R*gamma+P*gamma**2+T*gamma**3)/(1-gamma**4), (R+T*gamma)/(1-gamma**2), S/(1-gamma), P/(1-gamma), (S+P*gamma+P*gamma**2+R*gamma**3)/(1-gamma**4), (P+R*gamma)/(1-gamma**2)]])

    def __init__(self, gamma):
        self.gamma = gamma

class Replicator:

    #agentProportions must be in the order of [H_AC, H_AD, H_TFT, H_NTFT, WAC, WAD, WTFT, WNTFT]
    def __init__(self, gamma, agentProportions, game):
        if game == 0:
            self.game = PrisonersDilemma.__init__(gamma)
        elif game == 1:
            self.game = StagHunt.__init__(gamma)
        elif game == 2:
            self.game = BattleOfTheSexes.__init__(gamma)
        else:
            print("Not a valid game choice: ", game)
            exit()
        self.proportions = agentProportions

    def play(self):
        #Calculate the average payoff and utilities of each agent/Strategy
        avPayoff = 0
        agentUtilities = []

        for i in xrange(len(self.agentProportions)):
            utilityOfI = 0
            for j in xrange(len(self.agentProportions)):
                utilityOfI += self.agentProportions[j]*self.game.EXPECTED_PAYOFF_MATRIX.item(i,j)

            avPayoff += utilityOfI*self.agentProportions[i];
            agentUtilities[i] = utilityOfI

        #Calculate the change in proportion of each agent/Strategy
        changeInProp = []
        for i in xrange(len(self.agentProportions)):
            changeInProp[i] = self.agentProportions[i]*(agentUtilities[i] - avPayoff)

        #Update the proportions accordingly
        for i in xrange(len(self.agentProportions)):
            self.agentProportions[i] = self.agentProportions[i] + changeInProp[i]


#Set the initial proportions for the replicator dynamic
# PrisonerGame = Replicator.__init__(gamma, [.25, .25, .25, .25], 0)
# for i in 10000:
#     PrisonerGame.play()
#
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()