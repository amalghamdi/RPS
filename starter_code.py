#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.next_move = moves.index(my_move)
        self.next_move += 1


def roundsOfPlay():
    while True:
        rounds = input("How many rounds you wants to play?")
        if not rounds.isdigit():
            print("Enter numbers only")
            continue
        return int(rounds)


class RockPlayer(Player):
    def move(self):
        return moves[0]


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            your_move = input("rock, paper, scissors?").lower()
            if your_move in moves:
                return your_move
            else:
                print("Try again")


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move


class CyclePlayer(Player):
    def __init__(self):
        self.next_move = 0

    def move(self):
        return moves[self.next_move]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("----Tie!!----")
        elif beats(move1, move2):
            print("----** Player one wins! **----")
            self.p1.score += 1
        else:
            print("----** Player Two wins! **----")
            self.p2.score += 1
        self.result()

    def play_game(self, rounds=3):
        print("Game start!")
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
            print("----------------------------")
        print("Game over!")

    def result(self):
        print(f'player one scored: {self.p1.score}')
        print(f'player two scored: {self.p2.score}')
        if self.p1.score > self.p2.score:
            print('Player one wis!')
        elif self.p2.score > self.p1.score:
            print('Player two wins!')
        else:
            print('Tie!')


if __name__ == '__main__':
    rounds = roundsOfPlay()
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game(int(rounds))
