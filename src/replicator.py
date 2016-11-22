import argparse
from games import Games
import matplotlib.pyplot as plt
from numpy import array
from numpy import arange


class Replicator:

    # agentProportions must be in the order of [H_AC, H_AD, H_TFT, H_NTFT, WAC, WAD, WTFT, WNTFT]
    def __init__(self, game, gamma, agentProportions):
        self.game = Games.get_game(game, gamma)
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('game', type=int, help=
    '''The game index to play:
        0: Prisoner's Dilemma
        1: Stag Hunt
        2: Battle of the Sexes''')
    parser.add_argument('initial_proportions', type=float, nargs='*', default=[0.25, 0.25, 0.25, 0.25], help=
    '''The initial proportions of the population.
    Should be in the order of [AC, AD, TFT, NTFT] or [H_AC, H_AD, H_TFT, H_NTFT, WAC, WAD, WTFT, WNTFT]''')
    parser.add_argument('--gamma', '-g', type=float, nargs='?', default=0.95, help='the gamma value')
    parser.add_argument('--iterations', '--t', type=int, default=100, help='number of generations to do')
    args = parser.parse_args()

    # Set the initial proportions for the replicator dynamic
    game = Replicator(args.game, args.gamma, args.initial_proportions)
    iterations = args.iterations
    Time = arange(0, iterations, 1)
    if len(args.initial_proportions) == 4:
        AC = [game.agentProportions[0]] * iterations
        AD = [game.agentProportions[1]] * iterations
        TfT = [game.agentProportions[2]] * iterations
        NTfT = [game.agentProportions[3]] * iterations
        for i in range(iterations - 1):
            props = game.play()
            AC[i + 1] = props[0]
            AD[i + 1] = props[1]
            TfT[i + 1] = props[2]
            NTfT[i + 1] = props[3]
        ac = array(AC)
        ad = array(AD)
        tft = array(TfT)
        ntft = array(NTfT)
        # Plot the results
        plt.plot(Time, ac, label="AC")
        plt.plot(Time, ad, label="AD")
        plt.plot(Time, tft, label="TFT")
        plt.plot(Time, ntft, label="NTFT")
    else:
        HAC = [game.agentProportions[0]] * iterations
        HAD = [game.agentProportions[1]] * iterations
        HTfT = [game.agentProportions[2]] * iterations
        HNTfT = [game.agentProportions[3]] * iterations
        WAC = [game.agentProportions[4]] * iterations
        WAD = [game.agentProportions[5]] * iterations
        WTFT = [game.agentProportions[6]] * iterations
        WNTFT = [game.agentProportions[7]] * iterations
        for i in range(iterations - 1):
            props = game.play()
            HAC[i + 1] = props[0]
            HAD[i + 1] = props[1]
            HTfT[i + 1] = props[2]
            HNTfT[i + 1] = props[3]
            WAC[i+1] = props[4]
            WAD[i+1] = props[5]
            WTFT[i+1] = props[6]
            WNTFT[i+1] = props[7]
        ac = array(HAC)
        # print ac
        ad = array(HAD)
        # print ad
        tft = array(HTfT)
        ntft = array(HNTfT)
        wac = array(WAC)
        # print wac
        wad = array(WAD)
        # print wad
        wtft = array(WTFT)
        wntft = array(WNTFT)
        # Plot the results
        plt.plot(Time, ac, label="H_AC")
        plt.plot(Time, ad, label="H_AD")
        plt.plot(Time, tft, label="H_TFT")
        plt.plot(Time, ntft, label="H_NTFT")
        plt.plot(Time, wac, label="W_AC", linestyle="--")
        plt.plot(Time, wad, label="W_AD", linestyle="--")
        plt.plot(Time, wtft, label="W_TFT", linestyle="--")
        plt.plot(Time, wntft, label="W_NTFT", linestyle="--")
    plt.ylabel('Proportion of Agents')
    plt.xlabel('Time')
    axes = plt.gca()
    axes.set_ylim([0, 1])
    plt.legend(loc=0, borderaxespad=0.)

    plt.show()