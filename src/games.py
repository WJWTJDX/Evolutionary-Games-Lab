import random
from sys import exit
from numpy import matrix
from numpy import array
from numpy import arange
import matplotlib.pyplot as plt

STRATEGIES = ["AC", "AD", "TfT", "NTfT"]


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

    def __init__(self, gamma):
        self.gamma = gamma
        self.EXPECTED_PAYOFF_MATRIX = self.generate_expected_payoff()

    def generate_expected_payoff(self):
        R = self.R
        T = self.T
        S = self.S
        P = self.P
        gamma = self.gamma
        # Rows in order of 0:AC 1:AD 2:TFT 3:NTFT
        # Cols in order of 0:AC 1:AD 2:TFT 3:NTFT
        return matrix([[R / (1 - gamma), S / (1 - gamma), R / (1 - gamma), S / (1 - gamma)],
                     [T / (1 - gamma), P / (1 - gamma), T + P * gamma / (1 - gamma), S + T * gamma / (1 - gamma)],
                     [R / (1 - gamma), S + P * gamma / (1 - gamma), R / (1 - gamma), (S + P * gamma + T * gamma ** 2 + R * gamma ** 3) / (1 - gamma ** 4)],
                     [T / (1 - gamma), T + S * gamma / (1 - gamma), (T + P * gamma + S * gamma ** 2 + R * gamma ** 3) / (1 - gamma ** 4), (P + R * gamma) / (1 - gamma ** 2)]])


class StagHunt(PrisonersDilemma):
    R = 5
    T = 3
    S = 1
    P = 3

    def __init__(self, gamma):
        super.__init__(gamma)


class BattleOfTheSexes:
    R = 3
    T = 5
    S = 1
    P = 2

    def __init__(self, gamma):
        self.gamma = gamma
        self.EXPECTED_PAYOFF_MATRIX = self.generate_expected_payoff()

    def generate_expected_payoff(self):
        R = self.R
        T = self.T
        S = self.S
        P = self.P
        gamma = self.gamma
        # Rows in order of 0:H_AC, 1:H_AD, 2:H_TFT, 3:H_NTFT, 4:W_AC, 5:W_AD, 6:W_TFT, 7:W_NTFT
        # Cols in order of 0:H_AC, 1:H_AD, 2:H_TFT, 3:H_NTFT, 4:W_AC, 5:W_AD, 6:W_TFT, 7:W_NTFT
        return matrix([ [P/(1-gamma), S/(1-gamma), P/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma), R/(1-gamma), S/(1-gamma)],
                        [P/(1-gamma), R/(1-gamma), P + R*gamma/(1-gamma), R + P*gamma/(1-gamma), P/(1-gamma), T/(1-gamma), P + T*gamma/(1-gamma), T + P*gamma/(1-gamma)],
                        [P/(1-gamma), S + R*gamma/(1-gamma), P/(1-gamma), (S+R*gamma+P*gamma**2+P*gamma**3)/(1-gamma**4), R/(1-gamma), S + T*gamma/(1-gamma), R/(1-gamma), (S+T*gamma+P*gamma**2+R*gamma**3)/(1-gamma**4)],
                        [P/(1-gamma), R + S*gamma/(1-gamma), (P+R*gamma+S*gamma**2+P*gamma**3)/(1-gamma**4), (R+P*gamma)/(1-gamma**2), P/(1-gamma), T + S*gamma/(1-gamma), (P+T*gamma+S*gamma**2+R*gamma**3)/(1-gamma**4), (T+R*gamma)/(1-gamma**2)],
                        [T/(1-gamma), P/(1-gamma), T/(1-gamma), P/(1-gamma), R/(1-gamma), P/(1-gamma), R/(1-gamma), P/(1-gamma)],
                        [S/(1-gamma), R/(1-gamma), S + R*gamma/(1-gamma), R + S*gamma/(1-gamma), S/(1-gamma), P/(1-gamma), S + P*gamma/(1-gamma), P + S*gamma/(1-gamma)],
                        [T/(1-gamma), P + R*gamma/(1-gamma), T/(1-gamma), (P+R*gamma+S*gamma**2+T*gamma**3)/(1-gamma**4), R/(1-gamma), P/(1-gamma), R/(1-gamma), (P+P*gamma+S*gamma**2+R*gamma**3)/(1-gamma**4)],
                        [S/(1-gamma), R + P*gamma/(1-gamma), (S+R*gamma+P*gamma**2+T*gamma**3)/(1-gamma**4), (R+T*gamma)/(1-gamma**2), S/(1-gamma), P/(1-gamma), (S+P*gamma+P*gamma**2+R*gamma**3)/(1-gamma**4), (P+R*gamma)/(1-gamma**2)]])

class Replicator:

    # agentProportions must be in the order of [H_AC, H_AD, H_TFT, H_NTFT, WAC, WAD, WTFT, WNTFT]
    def __init__(self, gamma, agentProportions, game):
        if game == 0:
            self.game = PrisonersDilemma(gamma)
        elif game == 1:
            self.game = StagHunt(gamma)
        elif game == 2:
            self.game = BattleOfTheSexes(gamma)
        else:
            print("Not a valid game choice: ", game)
            exit()
        self.agentProportions = agentProportions

    def play(self):
        # Calculate the average payoff and utilities of each agent/Strategy
        avPayoff = 0
        agentUtilities = [0]*len(self.agentProportions)
        utilitySum = 0

        for i in range(len(self.agentProportions)):
            utilityOfI = 0
            for j in range(len(self.agentProportions)):
                utilityOfI += self.agentProportions[j]*self.game.EXPECTED_PAYOFF_MATRIX.item(i,j)

            avPayoff += utilityOfI*self.agentProportions[i]
            agentUtilities[i] = utilityOfI
            utilitySum += utilityOfI
        # print("Agent Utilities: ", agentUtilities)
        # print("Average Payoff: ", avPayoff)

        # Normalize the utilities to be on a 0-1 scale
        for i in range(len(agentUtilities)):
            agentUtilities[i] = agentUtilities[i]/utilitySum

        # print("Agent Utilities: ", agentUtilities)
        avPayoff = avPayoff/utilitySum
        # print("Average Payoff: ", avPayoff)

        # Calculate the change in proportion of each agent/Strategy
        changeInProp = [0]*len(self.agentProportions)
        for i in range(len(self.agentProportions)):
            changeInProp[i] = self.agentProportions[i]*(agentUtilities[i] - avPayoff)
        # print("Change in proportions: ", changeInProp)


        # Update the proportions accordingly
        for i in range(len(self.agentProportions)):
            self.agentProportions[i] = self.agentProportions[i] + changeInProp[i]

        # print("Updated Proportions: ", self.agentProportions)
        return self.agentProportions

# Set the initial proportions for the replicator dynamic
PrisonerGame = Replicator(.99, [.25, .25, .25, .25], 0)
iterations = 150
AC = [PrisonerGame.agentProportions[0]]*iterations
AD = [PrisonerGame.agentProportions[1]]*iterations
TfT = [PrisonerGame.agentProportions[2]]*iterations
NTfT = [PrisonerGame.agentProportions[3]]*iterations
Time = arange(0, iterations, 1)
for i in range(iterations - 1):
    props = PrisonerGame.play()
    AC[i+1] = props[0]
    AD[i+1] = props[1]
    TfT[i+1] = props[2]
    NTfT[i+1] = props[3]
ac = array(AC)
ad = array(AD)
tft = array(TfT)
ntft = array(NTfT)
#Plot the results
plt.plot(Time, ac, label="AC")
plt.plot(Time, ad, label="AD")
plt.plot(Time, tft, label="TFT")
plt.plot(Time, ntft, label="NTFT")
plt.ylabel('Proportion of Agents')
plt.xlabel('Time')
plt.legend(loc=2, borderaxespad=0.)

plt.show()