""" Welcome to my Wordle Game via the Python terminal output. In this game, the user gets 6 chances to guess a randomly-generated
5-letter word (aka the Wordle)! For each guess the user makes, the game breaks it down by letter. Specifically, if the 
user guesses a letter in the correct position of the actual word, that letter will become highlighted green. If the user 
guesses a letter that is in the actual word but they have guessed the incorrect position for that letter, the letter 
will be highlighted yellow. Lastly, if the user guesses a word with any letters that are not in the actual word, those 
letters will remain gray. For every letter that the user already guesses, the system adds them to the list of used letters 
and removes them from the list of all letters in order to print the used and unused letters after each guess. """

from rich.prompt import Prompt
from rich.console import Console
from random import choice
from wordsList import five_letter_words

# Here, I am using block emojis to help create the performance metric at the end of each Wordle game 
performance_blocks = {
    'correct_letter_and_place': '🟩',
    'correct_letter_wrong_place': '🟨',
    'incorrect_letter': '⬛'
}

# Creating the game title and instructions 
welcome_msg = f'\n[black on white] WELCOME TO OUR WORDLE GAME! [/]\n'
game_instructions = "You get six changes to guess the word. Start guessing below!\n"
guess_statement = "-------------------------------------\nEnter your guess: "

# In the Wordle game, the user gets 6 chances to guess the mystery word. Here, I am initializing that
guessing_chances = 6

# The next 3 defs are used to color each letter of each of the user's guesses to show them if the letter is in the word or not and if it is in the correct place or not

def correct_letter_and_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter_wrong_place(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on gray]{letter}[/]'

# The next def creates the progress with each guess and overall performance blocks for the user's game 

def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_letter_and_place(letter)
            wordle_pattern.append(performance_blocks['correct_letter_and_place'])
        elif letter in answer:
            guessed += correct_letter_wrong_place(letter)
            wordle_pattern.append(performance_blocks['correct_letter_wrong_place'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(performance_blocks['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []  # This creates a list of words that the user already guessed so the system can recognize and let the user know if they already guessed that word
    full_wordle_pattern = []
    all_words_guessed = []

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    used = []
    while not end_of_game:
        guess = Prompt.ask(guess_statement).upper()  # Gets the user's guess and converts into all uppercase 
        # The game only uses words with 5 letters in them, so if the word does not have 5 letters or if the word has been guessed already, the user gets an error
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            guess = Prompt.ask(guess_statement).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)
        console.print(*all_words_guessed, sep="\n")

        # Adding the used letters to the used letters list so users know what they guessed already 
        for each in guess:
            if each not in used:
                used.append(each)
        print("\nused letters:", ''.join(used))

        # Removing the letters used from the list of all letters to show the unused letters that users have not guessed yet
        for each in guess:
            if each in alphabet:
                alphabet.remove(each)
        print("unused letters: ", ''.join(alphabet))

        # If the user guesses correctly or runs out of allowed guesses, the game is over!
        if guess == chosen_word or len(already_guessed) == guessing_chances:
            end_of_game = True
    
    # Letting the user know if they lost or won the game 
    if len(already_guessed) == guessing_chances and guess != chosen_word:
        console.print("\n-------------------------------", f"\n[red]Sorry, you did not guess the WORDLE! Try again next time![/]")
        console.print(f"\n[green]The correct WORDLE was: '{chosen_word}'[/]")
    else:
        console.print("\n-------------------------------", f"\n[green]CONGRATS, you win! The WORDLE was '{chosen_word}'! \nYou guessed the WORDLE in {len(already_guessed)}/{guessing_chances} guesses![/]\n")
    console.print(f"\n[blue]Here is your performance for the game:",*full_wordle_pattern, sep="\n")


if __name__ == '__main__':
    console = Console()
    chosen_word = choice(five_letter_words)
    console.print(welcome_msg)
    console.print(game_instructions)
    game(console, chosen_word)
