# Wordle
A version of the New York Times word-guessing game, Wordle, developed entirely in Python. 

## What is Wordle?

Wordle is a web-based word guessing game created by software engineer, Josh Wardle. The game is run by The New York Times. Players have six attempts to guess a five-letter word, and they are given feedback for each guess in the form of colored letter tiles indicating when they have guessed letters that match or occupy the correct position of the actual word. 

In this project, I designed and programmed my own version of Wordle entirely in Python. My development of this Wordle version includes a demo version of the game which ran simply but thouroughly within the Python terminal output, as well as the final fully functioning Wordle game designed with a PyGame GUI, replicating a simple version of the actual New York Times Wordle interface. 

## How the Program Works:

* User gets 6 chances to guess a randomly-generated 5-letter word 
* The program indicates correctly and incorrectly-guessed letters for each user guess in coordination with the actual generated word (green for correct letter in the correct position of the word, yellow for correct letter but in the incorrect position of the word, and gray if the letter is not in the actual word in any letter position). 
* The game interface displays the alphabet on the lower section of the screen, greying out letters that have already been guessed by the user.
* If the user guesses the randomly-generated word within 6 chances, they win the game! If they fail to guess the word correctly in 6 chances, they lose.  
