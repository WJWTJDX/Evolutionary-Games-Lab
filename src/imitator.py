import argparse
import csv
from src.games import Games

EXTENSION = '.csv'
DATA_DIR = '../data/'


class Imitator:
    LATTICE_SIZE = 30

    def __init__(self, game, gamma, lattice_pattern="quadrants"):
        self.game = Games.get_game(game, gamma)
        self.pattern = lattice_pattern
        self.lattice = self.construct_lattice(lattice_pattern)

    # == Imitation Dynamics Functions ==

    def run(self, iterations=100):
        print(self.game.name, "--" + self.pattern)

        result = []
        cols = range(self.LATTICE_SIZE * self.LATTICE_SIZE)
        result.append(cols)
        result.append(self.lattice_array())

        for t in range(iterations):
            # get scores
            for i in range(self.LATTICE_SIZE):
                for j in range(self.LATTICE_SIZE):
                    self.get_score(i,j)
            # imitate the best of your neighbors
            for i in range(self.LATTICE_SIZE):
                for j in range(self.LATTICE_SIZE):
                    agent = self.get_agent(i, j)
                    best = self.best_neighbor(i, j)
                    if best.score > agent.score:
                        agent.strategy = best.strategy

            result.append(self.lattice_array())

            done = self.converged
            print(done, t+1)
            if done:
                break

        with open(self.output_file, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for row in result:
                writer.writerow(row)

    def best_neighbor(self, i, j):
        neighbors = self.neighbors(i,j)
        best = max(neighbors, key=lambda x: x.score)
        return best

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
        result = [self.get_agent(i - 1, j - 1), self.get_agent(i - 1, j), self.get_agent(i - 1, j + 1),
                  self.get_agent(i, j - 1), self.get_agent(i, j + 1),
                  self.get_agent(i + 1, j - 1), self.get_agent(i + 1, j), self.get_agent(i + 1, j + 1)]
        return result
    
    def get_agent(self, i, j):
        if i > 0:
            i %= self.LATTICE_SIZE
        if j > 0:
            j %= self.LATTICE_SIZE
        return self.lattice[i][j]

    def battle(self, agent1, agent2):
        score = self.game.EXPECTED_PAYOFF_MATRIX[agent1.id, agent2.id]
        return score

    # == Properties ==

    # returns true if all of the agents are of the same type
    @property
    def converged(self):
        first = self.get_agent(0, 0).strategy
        for i in range(self.LATTICE_SIZE):
            for j in range(self.LATTICE_SIZE):
                current = self.get_agent(i, j).strategy
                if current != first:
                    return False
        return True

    @property
    def output_file(self):
        path = DATA_DIR + self.game.abbreviation + '_' + self.pattern_abbreviation(self.pattern) + EXTENSION
        print(path)
        return path

    # == Lattice Functions ==

    def construct_lattice(self, lattice_pattern):
        pattern = self.pattern_abbreviation(lattice_pattern)
        result = []
        if pattern == "quads":
            result = self.quad_pattern()
        elif pattern == "inv":
            result = self.invasion_pattern("AC")
        elif pattern == "tri":
            result = self.triangles_pattern()
        return result

    def quad_pattern(self):
        result = []
        half = self.LATTICE_SIZE / 2
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

    def invasion_pattern(self, defender):
        others = self.game.STRATEGIES[:]
        others.remove(defender)
        result = []
        for i in range(self.LATTICE_SIZE):
            row = []
            for j in range(self.LATTICE_SIZE):
                if 6 <= i <= 11 and 12 <= j <= 17:
                    row.append(Agent(others[0]))
                elif 18 <= i <= 23 and 12 <= j <= 17:
                    row.append(Agent(others[1]))
                elif 12 <= i <= 17 and 18 <= j <= 23:
                    row.append(Agent(others[2]))
                else:
                    row.append(Agent(defender))
            result.append(row)
        return result

    def triangles_pattern(self):
        result = []
        half = self.LATTICE_SIZE / 2
        for i in range(self.LATTICE_SIZE):
            row = []
            for j in range(self.LATTICE_SIZE):
                if i >= half > j:
                    if i + j >= self.LATTICE_SIZE:
                        row.append(Agent("H_AC"))
                    else:
                        row.append(Agent("W_AC"))
                elif i >= half and j >= half:
                    if i + j >= half*3:
                        row.append(Agent("H_TfT"))
                    else:
                        row.append(Agent("W_TfT"))
                elif j >= half > i:
                    if i + j >= self.LATTICE_SIZE:
                        row.append(Agent("H_NTfT"))
                    else:
                        row.append(Agent("W_NTfT"))
                else:
                    if i + j >= half:
                        row.append(Agent("H_AD"))
                    else:
                        row.append(Agent("W_AD"))
            result.append(row)
        return result

    def lattice_array(self):
        l = []
        for i in range(self.LATTICE_SIZE):
            for j in range(self.LATTICE_SIZE):
                l.append(self.lattice[i][j].strategy)
        return l

    def print_lattice(self, grid=None):
        if grid is None:
            grid = self.lattice
        for row in grid:
            print(row)

    # == Helper Methods ==

    @staticmethod
    def pattern_abbreviation(pattern):
        abbreviations = {"quadrants": "quads", "quad": "quads", "quads": "quads",
                         "invasion": "inv", "inv": "inv",
                         "triangles": "tri", "tri": "tri", "triangle": "tri"}
        pattern = pattern.lower()
        return abbreviations[pattern]


class Agent:
    ID_MAP = {"AC": 0, "AD": 1, "TfT": 2, "NTfT": 3,
              "H_AC": 0, "H_AD": 1, "H_TfT": 2, "H_NTfT": 3, "W_AC": 4, "W_AD": 5, "W_TfT": 6, "W_NTfT": 7}

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
    parser.add_argument('--iterations', '-t', type=int, default=100, help='number of generations to do')
    parser.add_argument('--pattern', '-lp', default="quads", help='the lattice pattern to use')
    args = parser.parse_args()

    imitator = Imitator(args.game, args.gamma, lattice_pattern=args.pattern)
    imitator.run(args.iterations)
