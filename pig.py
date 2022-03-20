import random
import argparse


class Dice:
    def __init__(self, n=6):
        self.sides = n
        self.roll()

    def roll(self):
        self.value = int(random.random() * self.sides + 1)

class Game:
    def __init__(self):
        self.die = Dice()
        self.p1 = Player('Player 1')
        self.p2 = Player('Player 2')

    def play(self):
        while (self.p1.score <= 100 and self.p2.score <= 100):
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()
        if (self.p1.score > self.p2.score):
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')

class Player:
    def __init__(self, title):
        self.name = title
        self.score = 0
        self.die = Dice(6)

    def move(self):
        round_score = 0
        again = 'r'
        # establish a while loop for the player's turn
        while again == 'r':
            self.die.roll()
            roll = self.die.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score + roll
                print("{}'s round score is {}".format(self.name, round_score))
                again = input('Do you want to Roll = r or Hold = h  ')
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))

if __name__ == "__main__":
    print('welcome to game of Pig!')
    pig = Game()
    pig.play()
    print()
    print('Rerun to play again')