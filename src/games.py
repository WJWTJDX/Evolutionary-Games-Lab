import random


# Template Game class
class Game:
    ACTIONS = ["C", "D"]
    payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (1, 5),
                     ("D", "C"): (5, 1), ("D", "D"): (2, 2)}

    def opposite_action(self, action):
        if action == self.ACTIONS[0]:
            return self.ACTIONS[1]
        elif action == self.ACTIONS[1]:
            return self.ACTIONS[0]
        else:
            print("uhoh! unexpected action:", action)
            return None

    # def __init__(self, trials=100, gamma=1.0, log=False):
    #     self.trials = trials
    #     self.gamma = gamma
    #     self.log = log
    #
    # def run(self, p1, p2):
    #     sums = [0, 0]
    #     trials = 0
    #     for i in range(self.trials):
    #         actions, results = self.play(p1, p2)
    #         if self.log:
    #             print(actions)
    #
    #         # notify players of other player's action
    #         p1.update_prev(actions[1])
    #         p2.update_prev(actions[0])
    #
    #         # update totals
    #         sums[0] += results[0]
    #         sums[1] += results[1]
    #
    #         # biased coin flip for continuing
    #         trials += 1
    #         if not self.should_continue():
    #             break
    #
    #     if self.log:
    #         print("totals: ", str(sums))
    #         print("trials: ", trials)
    #     return sums
    #
    # def play(self, p1, p2):
    #     actions = (p1.action(), p2.action())
    #     results = self.payoff_matrix[actions]
    #     return actions, results
    #
    # def should_continue(self):
    #     return random.random() < self.gamma


# Base Template for the different types of agents
class Agent:

    def __init__(self, strategy):
        # the previous play of the other player
        self.previous = None
        self.strategy = strategy

    # gets the player's next action
    def action(self):
        return self.strategy.get_action(self.previous)

    # updates the action of what the other player just did
    def update_prev(self, results):
        self.previous = results


# Template for the different strategies
class Strategy:

    def __init__(self, game):
        self.game = game

    # is passed in the other player's previous action, then makes their decision based on that
    def get_action(self, previous):
        # override this function
        pass


class AlwaysCooperate(Strategy):

    def get_action(self, previous):
        return self.game.ACTIONS[0]


class AlwaysDefect(Strategy):

    def get_action(self, previous):
        return self.game.ACTIONS[1]


class TitForTat(Strategy):

    def get_action(self, previous):
        if previous is None:
            return self.game.ACTIONS[0]
        else:
            return previous


class NotTitForTat(Strategy):

    def get_action(self, previous):
        if previous is None:
            return self.game.ACTIONS[1]
        else:
            return self.game.opposite_action(previous)
