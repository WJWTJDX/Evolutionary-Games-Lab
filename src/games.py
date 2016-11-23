from sys import exit
from numpy import matrix


class PrisonersDilemma:

    R = 3
    T = 5
    S = 1
    P = 2
    STRATEGIES = ["AC", "AD", "TfT", "NTfT"]

    def __init__(self, gamma):
        self.abbreviation = "PD"
        self.name = "Prisoners Dilemma"
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


class StagHunt:
    R = 5
    T = 3
    S = 1
    P = 3
    STRATEGIES = ["AC", "AD", "TfT", "NTfT"]

    def __init__(self, gamma):
        self.abbreviation = "SH"
        self.name = "Stag Hunt"
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
                       [R / (1 - gamma), S + P * gamma / (1 - gamma), R / (1 - gamma),
                        (S + P * gamma + T * gamma ** 2 + R * gamma ** 3) / (1 - gamma ** 4)],
                       [T / (1 - gamma), T + S * gamma / (1 - gamma),
                        (T + P * gamma + S * gamma ** 2 + R * gamma ** 3) / (1 - gamma ** 4),
                        (P + R * gamma) / (1 - gamma ** 2)]])


class BattleOfTheSexes:
    R = 3
    T = 5
    S = 1
    P = 2
    STRATEGIES = ["H_AC", "H_AD", "H_TfT", "H_NTfT", "W_AC", "W_AD", "W_TfT", "W_NTfT"]

    def __init__(self, gamma):
        self.abbreviation = "BOTS"
        self.name = "Battle of the Sexes"
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


class Games:

    @staticmethod
    def get_game(game, gamma):
        if game == 0:
            return PrisonersDilemma(gamma)
        elif game == 1:
            return StagHunt(gamma)
        elif game == 2:
            return BattleOfTheSexes(gamma)
        else:
            print("Not a valid game choice: ", game)
            exit()
