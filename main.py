import random
from tkinter import *
import subprocess
from cows import Cow
from bulls import Bull


def is_duplicate(number: int) -> bool:
    return len(str(number)) != len(set(list(str(number))))


def generate_random() -> int:
    while True:
        number = random.randint(1000, 9999)
        if not is_duplicate(number):
            return number


if __name__ == '__main__':
    print("================================>          WELCOME TO COWS AND BULLS GAME          <====================================")
    secret_code = generate_random()
    user_guesses = []
    while True:
        user_guesses.append(int(input("Guess The Number : ")))
        cows = Cow(secret_code, user_guesses[-1])
        bulls = Bull(secret_code, user_guesses[-1])
        play = True
        if cows.cows_count == len(str(secret_code)):
            print("You have guessed it correct!!!\n")
            if len(user_guesses) != 1:
                print(f"your previous guesses are : {user_guesses[0:-1]}")
            play = input("Want to play again?\nType YES OR NO\n").lower()
            if play == 'yes':
                subprocess.run('python main.py')
            elif play == 'no':
                break
        else:
            print(f"cows : {cows}\nbulls : {bulls}")
            print("Try again")

