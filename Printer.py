from pyfiglet import figlet_format
from termcolor import colored

class Printer:
  def  __init__(self):
    pass

  def print_header(self):
    header = figlet_format("Guess the Quote!")
    header = colored(header, color="red")
    print(header)
  
  def print_quote(self, quote):
    print(f"Who said this....?\n\n{quote}\n")

  def print_guesses(self, guesses):
    print(f"You have {guesses} guesses remaining.")
  
  def print_clue(self, clue):
    print(f"\nNope, that's not right. Here's a clue....\n{clue}\n")
  
  def player_win(self, author):
    print(f"That's right! It was {author}")

  def player_lose(self, author):
    print(f"Nope, you lose! It was {author} who said it")

  def goodbye(self):
    print("Okay, bye!")

