import random

random.seed(0)

class Play_Game:

    def __init__(self):
        self.score = 0
        self.hold_score = 0
        self.player1_status = True
        self.player2_status = False

    def Roll_Dice(self):
        round_score = random.randint(1, 6)
        return round_score

    def Run_Total(self):
        self.score += round_score
        return self.score

    def Hold(self):
        self.hold_score = self.score
        return self.hold_score

if __name__ == '__main__':

    Player1 = Play_Game()
    Player2 = Play_Game()

print("Game Started!")
print("Player1's turn.")
while Player1.player1_status is True:

    action = input("r = roll, h = hold")
    if action == 'r':
        round_score = Player1.Roll_Dice()
        if round_score == 1:
            Player1.player1_status = False
            Player2.player2_status = True
            print("Player1, you rolled 1.")
            round_score = 0
            Player1.score = round_score + Player1.hold_score
            print(f"Round score is 1. Roll back to {Player1.score}")

    if action == 'h':
        Player1.player1_status = False
        Player2.player2_status = True
        Player1.Hold()
        print(f"Player1, You hold the score: {Player1.hold_score}")

    if action != 'h':
        Player1.Run_Total()
        print(f"Player1, your round score is: {round_score} and your score is : {Player1.score}")

    if Player1.score >= 100:
        print("Player1, you won!")
        break

    while Player2.player2_status is True:
        print("Player2's turn.")
        action = input("r = roll")
        if action == 'r':
            round_score = Player2.Roll_Dice()
            if round_score == 1:
                Player2.player2_status = False
                Player1.player1_status = True
                print("Player2, you rolled 1.")
                round_score = 0
                Player2.score = round_score + Player2.hold_score

        if action == 'h':
            Player2.player2_status = False
            Player1.player1_status = True
            Player2.Hold()
            print(f"Player2, You hold the score: {Player2.hold_score}")

        if action != 'h':
            Player2.Run_Total()
            print(f"Player2, your round score is: {round_score} and your score is : {Player2.score}")

        if Player2.score >= 100:
            print("Player2, you won!")
            break