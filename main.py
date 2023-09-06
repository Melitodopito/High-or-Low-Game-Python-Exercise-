import art
import random
from game_data import data
import os


def game():

  def generate_random(data):
    return data[random.randrange(0, len(data))]

  def show_comparisons():
    print(art.logo)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")

  Score = 0
  Game_Over = False
  a = generate_random(data)
  b = generate_random(data)
  show_comparisons()
  while not Game_Over:
    if a['follower_count'] > b['follower_count']:
      winner = "a"
    else:
      winner = "b"

    answer = input("Who has more followers ? Type \"A\" or \"B\": ")

    if answer.lower() == winner:
      Score += 1
      os.system("clear")
      print(f"\nYou're right! Current score: {Score}")
      a = b
      b = generate_random(data)
      show_comparisons()
    else:
      Game_Over = True
      print(f"Sorry, that's wrong. Final score: {Score}")


game()
