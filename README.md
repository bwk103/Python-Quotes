# Guess The Quote

## Challenge

Taken from Colt Steele's [The Modern Python 3 Bootcamp](https://www.udemy.com/the-modern-python3-bootcamp/learn/v4/overview), my challenge was to build a quotes guessing game, run on the command line, using Python3 and BeautifulSoup. 

The game scrapes [Quotes to Scrape](http://quotes.toscrape.com/) for a collection of quotes, selects one at random and displays it to the player.  The player is then given four chances to guess the name of the person who said the quote. If the player is wrong, they are given a clue about the person's identity.

## Approach

The suggested approach in building this application was to do so using only a few, long methods.  However, given my experience in OOP, I instead decided upon extracting the functionality of the application into three separate classes:

- a Scraper class to make the http request to the site, to extract the data and to format it into a list;

- a Game class to control the logistics of the game itself i.e. starting the game and considering guesses; and

- a Printer class to display messages to the player via the command line.  

## Technology Used

In building this application I made use of the following technologies and modules:

- [Python 3](https://www.python.org/);
- [Requests](http://docs.python-requests.org/en/master/) to make the HTTP request to site;
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrap and format the returned data;
- [Pyfiglet](https://github.com/pwaller/pyfiglet) and [Termcolor](https://pypi.org/project/termcolor/) to make the welcome screen beautiful.

## Installation

### Prerequisites 

The application uses Python 3.  If you have not previously installed Python 3 onto your machine, follow the instructions [here](https://www.python.org/downloads/) to do so.

### Playing the Game

Download the repository by navigating to an appropriate location on the command line and running:

`git clone https://github.com/bwk103/Python-Quotes.git`

Install the required modules by running the following command on the command line:

`python3 -m pip install requests bs4 pyfiglet termcolor`

Run the application by running the following command:

`python3 Game.py`

## Credits

- Colt Steele for the project idea.

- Quotes to Scrape for the many inspiring quotes. 






