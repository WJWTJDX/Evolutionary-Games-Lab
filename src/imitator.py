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

    def run(self, iterations=100):
        for t in range(iterations):
            # per generation
            for i in range(self.LATTICE_SIZE):
                for j in range(self.LATTICE_SIZE):
                    self.get_score(i,j)
        self.print_scores()

    def get_score(self, i, j):
        agent = self.lattice[i][j]

        # get 8-connected neighbors score
        total = 0
        for n in self.neighbors(i, j):
            total += self.battle(agent, n)

        # update agent's score
        agent.score = total
        return total

    def neighbors(self, i, j):
        result = [self.lattice[i - 1][j - 1], self.lattice[i - 1][j], self.lattice[i - 1][(j + 1) % self.LATTICE_SIZE],
                  self.lattice[i][j - 1], self.lattice[i][(j + 1) % self.LATTICE_SIZE],
                  self.lattice[(i + 1) % self.LATTICE_SIZE][j - 1], self.lattice[(i + 1) % self.LATTICE_SIZE][j],
                  self.lattice[(i + 1) % self.LATTICE_SIZE][(j + 1) % self.LATTICE_SIZE]]
        return result

    def battle(self, agent1, agent2):
        score = self.game.EXPECTED_PAYOFF_MATRIX[agent1.id, agent2.id]
        return score

    # Lattice Functions
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

    def print_scores(self):
        for i in range(self.LATTICE_SIZE):
            print([int(x.score) for x in self.lattice[i]])

class Agent:
    ID_MAP = {"AC": 0, "AD": 1, "TfT": 2, "NTfT": 3}

    def __init__(self, initial_strategy):
        self.strategy = initial_strategy
        # score for most recent round
        self.score = 0

    def __repr__(self):
        return self.strategy

    def __str__(self):
        return self.strategy

    @property
    def id(self):
        return self.ID_MAP[self.strategy]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('game', type=int, help='the game index to play')
    parser.add_argument('gamma', type=float, nargs='?', default=0.95, help='the gamma value')
    parser.add_argument('--iterations', '--t', type=int, default=100, help='number of generations to do')
    args = parser.parse_args()

    imitator = Imitator(args.game, args.gamma)
    print()
    imitator.run(1)
