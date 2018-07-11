from Scraper import Scraper
from Printer import Printer
from random import choice

class Game:

  def __init__(self, guesses=4, scraper=Scraper(), printer=Printer()):
    self.guesses = guesses
    self.scraper = scraper
    self.printer = printer
    self.scraper.get_quotes()
    self.quote = None
  
  def start_game(self):
    self.quote = choice(self.scraper.get_quote_list()) 
    self.printer.print_header()
    self.printer.print_quote(self.quote[0])
    self.printer.print_guesses(self.guesses)
    self._make_guess()

  def _make_guess(self):
    guess = input("")
    self._check_answer(guess)

  def _check_answer(self, guess):
    answer = self.quote[1]
    if guess == answer:
      self.printer.player_win(answer)
      self._play_again()
    else:
      self.guesses -=1
      self._check_round()
  
  def _check_round(self):
    if self.guesses == 3:
      self._first_clue()
    elif self.guesses == 2:
      self._second_clue()
    elif self.guesses == 1:
      self._final_clue()
    else:
      self.printer.player_lose(self.quote[1])
      self._play_again()

  def _first_clue(self):
    link = "http://quotes.toscrape.com" + self.quote[2]
    clue = self.scraper.get_bio(link)
    self._next_round(clue)

  def _second_clue(self):
    char = self.quote[1][0]
    clue = f"The first letter of this person's first name is {char}."
    self._next_round(clue)

  def _final_clue(self):
    lastname = self.quote[1].split(" ")[-1]
    char = lastname[0]
    clue = f"The first letter in this person's surname is {char}."
    self._next_round(clue)

  def _next_round(self, clue):
    self.printer.print_clue(clue)
    self.printer.print_guesses(self.guesses)
    self._make_guess()

  def _play_again(self):
    replay = input("Do you want to play again? y/n ")
    if replay == "y":
      self.start_game()
    else:
      self.printer.goodbye()
      exit

game = Game()
game.start_game()