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

## Installation 

### Included Files
* terminalWordle.py - This is the file containing the code to run the Wordle game directly in the Python Terminal Output
* playWordle.py - This is the file containing the code to run the Wordle game with the PyGame GUI, which closely resembles the actually look and feel of the real NYT Wordle game
* wordsList.py - This file contains a long list of 5-letter words (required for both terminalWordle.py and playWordle.py to run). Each of the programs randomly chooses a word from this list each time the user plays the game so that they are prompted with a new random 5-letter word to guess on each round of playing.
* wordle bg.png - This is the background image that I created to resemble the actual Wordle interface. It is only required by the playWordle.py file in order to develop the UI background for the game.
* FreeSansBold.otf - This is a font text file that is used for styling in the playWordle.py file. 

### Demo Version (Runs in the Python Terminal Output)

For this version, all you will need to do is download the terminalWordle.py and wordsList.py files. Once downloaded, you can simply run the terminalWordle.py file and start guessing 5-letter words within the terminal.

### Full Version (Complete with a PyGame GUI)

For this version, you will need to download the playWordle.py, wordsList.py, wordle bg.png, and FreeSansBold.otf files (Be sure to install the pygame module as well)! Once downloaded, you can run the playWordle.py file which will trigger PyGame to run. Once the GUI pops up on your screen, you can simply start guessing 5-letter words. 
