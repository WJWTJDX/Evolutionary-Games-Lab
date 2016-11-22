import argparse
import csv
from src.games import Games

OUTPUT_FILE = 'results.csv'

class Imitator:
    LATTICE_SIZE = 30

    def __init__(self, game, gamma, init_props=None):
        self.game = Games.get_game(game, gamma)
        self.proportions = init_props
        self.lattice = self.construct_lattice()

        # self.print_lattice()

    def run(self, iterations=100):
        result = []
        cols = range(self.LATTICE_SIZE * self.LATTICE_SIZE)
        result.append(cols)

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

        with open(OUTPUT_FILE, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for row in result:
                writer.writerow(row)

    def best_neighbor(self, i, j):
        neighbors = self.neighbors(i,j)
        score = lambda x: x.score
        best = max(neighbors, key=score)
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
        l = []
        for i in range(self.LATTICE_SIZE):
            l.extend(self.lattice[i])

        for j in l:
            print(j, ",", end="")

        print()

    def lattice_array(self):
        l = []
        for i in range(self.LATTICE_SIZE):
            for j in range(self.LATTICE_SIZE):
                l.append(self.lattice[i][j].strategy)
        return l

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
    parser.add_argument('--iterations', '-t', type=int, default=100, help='number of generations to do')
    args = parser.parse_args()

    imitator = Imitator(args.game, args.gamma)
    imitator.run(args.iterations)
