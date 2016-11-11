import random


# Template Game class
class Game:
    payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (1, 5),
                     ("D", "C"): (5, 1), ("D", "D"): (2, 2)}

    def __init__(self, trials=100, gamma=1.0, log=False):
        self.trials = trials
        self.gamma = gamma
        self.log = log

    def run(self, p1, p2):
        sums = [0, 0]
        trials = 0
        for i in range(self.trials):
            actions, results = self.play(p1, p2)
            if self.log:
                print(actions)

            # notify players of other player's action
            p1.update(actions[1])
            p2.update(actions[0])

            # update totals
            sums[0] += results[0]
            sums[1] += results[1]

            # biased coin flip for continuing
            trials += 1
            if not self.should_continue():
                break

        if self.log:
            print("totals: ", str(sums))
            print("trials: ", trials)
        return sums

    def play(self, p1, p2):
        actions = (p1.action(), p2.action())
        results = self.payoff_matrix[actions]
        return actions, results

    def should_continue(self):
        return random.random() < self.gamma


# Base Template for the different types of agents
class Agent:

    def __init__(self):
        # the previous play of the other player
        self.previous = None

    # gets the player's next action
    def action(self):
        return "C"

    # updates the action of what the other player just did
    def update(self, results):
        self.previous = results
