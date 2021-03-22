import random

random.seed(0)

class Player1:


    def __init__(self):

        self.score = 0
        self.total_score = 0

    def Roll(self):

        print("Wei, it is your turn now.")
        value = input("r = roll")
        while value == "r":
            round_score = random.randint(1, 6)

            if round_score == 1:
                print(f"Wei, you rolled {round_score}. Now, it is your opponent's turn.")
                round_score = 0
                self.score = round_score + self.total_score
                Yi.Roll()

            self.score += round_score

            if self.score >= 100:
                print(f"You got {self.score}")
                print("Wei, you won!")
                break

            print(f"Wei, your round score is {round_score} and your score is: {self.score}")

            value = input("r = roll, h = hold")
            if value == "h":

                self.total_score = self.score
                print(f"Wei, your score is: {self.total_score}. Now, it is your opponent's turn.")
                Yi.Roll()

class Player2:

    def __init__(self):

        self.score = 0
        self.total_score = 0

    def Roll(self):

        print("Yi, it is your turn now.")
        value = input("r = roll")
        while value == "r":
            round_score = random.randint(1, 6)

            if round_score == 1:
                print(f"Yi, you rolled {round_score}. Now, it is your opponent's turn.")
                round_score = 0
                self.score = round_score + self.total_score
                Wei.Roll()

            self.score += round_score

            if self.score >= 100:
                print(f"You got {self.score}")
                print("Yi, you won!")
                break

            print(f"Yi, your round score is {round_score} and your score is: {self.score}")

            value = input("r = roll, h = hold")
            if value == "h":

                self.total_score = self.score
                print(f"Yi, your score is: {self.total_score}. Now, it is your opponent's turn.")
                Wei.Roll()

if __name__ == '__main__':

    Wei = Player1()
    Yi = Player2()
    print(Wei.Roll())