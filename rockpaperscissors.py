#!/usr/bin/env python3
import random
from random import randint

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class Random_Player(Player):
    def move(self):
        return random.choice(moves)


class Human_Player(Player):
    def move(self):
        while True:
            response = input("Rock, Paper, Scissors?: ").lower()
            if (response in moves):
                return response
            print("Try again.")


class Reflect_Player(Player):
    def learn(self, my_move, their_move):
        self.their_last_move = their_move

    def __init__(self):
        self.their_last_move = " "

    def move(self):
        if self.their_last_move == " ":
            return random.choice(moves)
        else:
            return self.their_last_move


class Cycle_Player(Player):
    def learn(self, my_move, their_move):
        self.my_last_move = my_move

    def __init__(self):
        self.my_last_move = " "

    def move(self):
        while True:
            if self.my_last_move == " ":
                return random.choice(moves)
            elif self.my_last_move == "rock":
                return "paper"
            elif self.my_last_move == "paper":
                return "scissors"
            elif self.my_last_move == "scissors":
                return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} \nPlayer 2: {move2}")
        if beats(move1, move2):
            print("Round won by: Player 1")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Round won by: Player 2")
            self.p2_score += 1
        else:
            print("Tie!")
        print(f"Score: Player 1- {self.p1_score}, Player 2- {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock, Paper, Scissors Shoot!")
        for round in range(10):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("Player 1 wins!")
        elif self.p1_score < self.p2_score:
            print("Player 2 wins")
        else:
            print("Tie!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(Cycle_Player(), Human_Player())
    game.play_game()
