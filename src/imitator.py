import argparse
from src.games import PrisonersDilemma, StagHunt, BattleOfTheSexes


class Imitator:
    LATTICE_SIZE = 30

    def __init__(self, game, gamma, init_props=None):
        if game == 0:
            self.game = PrisonersDilemma(gamma)
        elif game == 1:
            self.game = StagHunt(gamma)
        elif game == 2:
            self.game = BattleOfTheSexes(gamma)

        self.gamma = gamma
        self.proportions = init_props
        self.lattice = self.construct_lattice()

        self.print_lattice()

    def construct_lattice(self):
        # for now, just default to quadrants
        half = self.LATTICE_SIZE / 2

        result = []
        for i in range(self.LATTICE_SIZE):
            row = []
            for j in range(self.LATTICE_SIZE):
                if i >= half > j:
                    row.append(Agent("AC"))
                elif i >= half and j >= half:
                    row.append(Agent("TfT"))
                elif j >= half > i:
                    row.append(Agent("NTfT"))
                else:
                    row.append(Agent("AD"))
            result.append(row)

        return result

    def print_lattice(self):
        for i in range(self.LATTICE_SIZE):
            print(self.lattice[i])


class Agent:

    def __init__(self, initial_strategy):
        self.strategy = initial_strategy
        # score for most recent round
        self.score = 0

    def __repr__(self):
        return self.strategy

    def __str__(self):
        return self.strategy

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('game', help='the game index to play')
    parser.add_argument('gamma', type=float, nargs='?', default=0.95, help='the gamma value')
    args = parser.parse_args()

    imitator = Imitator(args.game, args.gamma)
