""" This code is for the game of Wordle! In this game, the user gets 6 chances to guess a randomly-generated
5-letter word (aka, the Wordle)! For each guess the user makes, the game breaks it down by letter. Specifically, 
if the user guesses a letter in the correct position of the actual word, that letter will become highlighted green.
If the user guesses a letter that is in the actual word but they have guessed the incorrect position for that 
letter, the letter will be highlighted yellow. Lastly, if the user guesses a word with any letters that are not 
in the actual word, those letters will become gray. For every letter that the user already guesses, the system 
makes them greyed-out in the list of alphabet letters on the bottom of the screens (the indicators), which indicate
which letters the user has guessed already and which they have not used yet. Have fun playing! """

import pygame
import sys 
import random 
from wordsList import five_letter_words

pygame.init()

# First, I create the PyGame window and set the background image as the Wordle boxes image that I created and imported here
width, height = 600,750
game_window = pygame.display.set_mode((width, height))
background = pygame.image.load("wordle bg.png")
background_screen = background.get_rect(center=(300,375))
pygame.display.set_caption("PLAY WORDLE!")

# Here are all of the colors needed for the styling of this Wordle Game 
darkGray = (18,18,19)
green = (106,170,100)
yellow = (201,180,88)
gray = (120,124,126)
outline = (211,214,218)
filled_outline = (18,18,19) 
red = (230,94,94)

# The alphabet will be used to display the letters on the screen (called 'indicators' in the Wordle Game), indicating if the letter is used or unused 
alphabet = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

""" Note: For the purpose of easily checking if the game is working, the initial correct Wordle is 'Plant'. 
However, after 'plant' is played, if the user presses 'Enter' key to play again, they will get a random word.
To get a random word on the first try, comment out that line of code and uncomment the one after, or vice versa."""
correct_wordle = "plant"
# correct_wordle = random.choice(five_letter_words)

guesses_font = pygame.font.Font("FreeSansBold.otf", 50)
alph_font = pygame.font.Font("FreeSansBold.otf", 25)

game_window.fill(darkGray)
game_window.blit(background, background_screen)
pygame.display.update()

letter_spacing_X = 76
letter_spacing_Y = 92 
letter_size = 60 

# Here, I am initializing the variable that counts how many guesses the user makes
num_guesses = 0

# This list helps us draw each letter from each guess on the screen 
user_guesses = [[]] * 6 

current_guess = []
current_guess_string = ""
current_letter_bg_x = 120  # Setting the start x positioning for first letter typed

# Reminder: indicators are indicative of the used and unused letters in the alphabet according to user guesses
indicators = []

# The game result can be either W(win), L(loss), or remain empty which represents that the game is still ongoing
game_result = ""

# The Letter class deals with drawing and styling the letters for when the user is typing their guesses
class Letter:
    # The __init__ function styles and positions the letters 
    def __init__(self, text, bg_position):
        self.bg_color = darkGray
        self.text_color = "white"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, letter_size, letter_size)
        self.text = text
        self.text_position = (self.bg_x+25, self.bg_position[1]+34)
        self.text_surface = guesses_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    # The draw() function draws and places the letters on the screen as the user types 
    def draw(self):
        pygame.draw.rect(game_window, self.bg_color, self.bg_rect)
        if self.bg_color == darkGray:
            pygame.draw.rect(game_window, filled_outline, self.bg_rect, 3)
        self.text_surface = guesses_font.render(self.text, True, self.text_color)
        game_window.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    # The delete() function removes letters from the user's typing guess as triggered by the use of the "Delete" key
    def delete(self):
        pygame.draw.rect(game_window, darkGray, self.bg_rect)
        pygame.draw.rect(game_window, outline, self.bg_rect, 3)
        pygame.display.update()

# The indicator class deals with the alphabet indicators of whether or not the user has guessed the letter already or not (indicating if the letter is used or unused)
class Indicator:
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter to be used by the indicators
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 45, 55)
        self.bg_color = outline

    def draw(self):
        # Draws the indicator rectangle and its text on the screen at the specified position 
        pygame.draw.rect(game_window, self.bg_color, self.rect)
        self.text_surface = alph_font.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+20))
        game_window.blit(self.text_surface, self.text_rect)
        pygame.display.update()

# Now, we draw the alphabet letter indicators on the screen. First, set the x and y positions 
indicator_x, indicator_y = 60, 560

# Creating the 3 rows of alphabet letters according to standard US english keyboard
for i in range(3):
    for letter in alphabet[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 50
    indicator_y += 60
    if i == 0:  # 0 represents the middle row of alphabet letters on the Wordle Game screen
        indicator_x = 80
    elif i == 1:  # 1 represents the bottom row of alphabet letters on the Wordle Game screen
        indicator_x = 125

# The check_guess function goes through each letter of the user's guess and checks if it should be green, yellow, or gray
def check_guess(guess_to_check):
    global current_guess, current_guess_string, num_guesses, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in correct_wordle:
            # If the letter in the user's guess is in the actual word and in the correct position, it should be green
            if lowercase_letter == correct_wordle[i]:
                guess_to_check[i].bg_color = green
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = green
                        indicator.draw()
                if not game_decided:
                    game_result = "W"
            # If the letter in the user's guess is in the actual word, but not in the correct position, it should be yellow
            else:
                guess_to_check[i].bg_color = yellow
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = yellow
                        indicator.draw()
                game_result = ""
                game_decided = True
        # If the letter in the user's guess is not in the actual wordle at all, it should be gray
        else:
            guess_to_check[i].bg_color = gray
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = gray
                    indicator.draw()
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    
    # After each guess, we need to increase number of guesses by 1, reset the current guess letters, and the start X position for guessing
    num_guesses += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 120  # determines the X start of the first letter of the next user guess

    # In the game of Wordle, the user gets 6 chances to guess the word. If they don't guess in 6, they lose the game
    if num_guesses == 6 and game_result == "":
        game_result = "L"


# The play_again() function is for when the Wordle game is ended (win or loss), and the user can opt to play another round
def play_again():
    # If the user guesses the correct wordle within 6 chances, they win! And, they are prompted to play the game again 
    if game_result == "W":
        pygame.draw.rect(game_window, darkGray, (10, 550, 1000, 800))
        win_lose_font = pygame.font.Font("FreeSansBold.otf", 25)
        win_text = win_lose_font.render(f"Congrats, you win! You guessed in {num_guesses}/6 guesses!", True, green)
        win_rect = win_text.get_rect(center=(width/2, 650))
        play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
        play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "white")
        play_again_rect = play_again_text.get_rect(center=(width/2, 700))
        word_was_text = play_again_font.render(f"The wordle was {correct_wordle.upper()}!", True, "white")
        word_was_rect = word_was_text.get_rect(center=(width/2, 600))
        
        game_window.blit(word_was_text, word_was_rect)
        game_window.blit(win_text, win_rect)
        game_window.blit(play_again_text, play_again_rect)
        pygame.display.update()
    # If the user did not guess the correct wordle within 6 guesses, they lose. But, they are still prompted to play again
    else:  # represents if game_result == "L"
        pygame.draw.rect(game_window, darkGray, (10, 550, 1000, 800))
        win_lose_font = pygame.font.Font("FreeSansBold.otf", 25)
        win_text = win_lose_font.render(f"Sorry, you lost! You did not guess it in 6 guesses!", True, red)
        win_rect = win_text.get_rect(center=(width/2, 650))
        play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
        play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "white")
        play_again_rect = play_again_text.get_rect(center=(width/2, 700))
        word_was_text = play_again_font.render(f"The wordle was {correct_wordle.upper()}!", True, "white")
        word_was_rect = word_was_text.get_rect(center=(width/2, 600))
        
        game_window.blit(word_was_text, word_was_rect)
        game_window.blit(win_text, win_rect)
        game_window.blit(play_again_text, play_again_rect)
        pygame.display.update()
    
# The reset() function resets all of the global variables to their default states so the game can be started over from the beginning
def reset():
    global num_guesses, correct_wordle, user_guesses, current_guess, current_guess_string, game_result
    game_window.fill(darkGray)
    game_window.blit(background, background_screen)
    num_guesses = 0
    correct_wordle = random.choice(five_letter_words).lower()
    user_guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = outline
        indicator.draw()

def create_new_letter():
    # Creates a new letter as the user types and adds it to the user's guess
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, num_guesses*78+letter_spacing_Y))
    current_letter_bg_x += letter_spacing_X
    user_guesses[num_guesses].append(new_letter)
    current_guess.append(new_letter)
    # Drawing the letters so the user can view them on the screen
    for guess in user_guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # Deletes the most recently typed letter from the user's guess 
    global current_guess_string, current_letter_bg_x
    user_guesses[num_guesses][-1].delete()
    user_guesses[num_guesses].pop()  # Removes the letter from the list of letters that make up the user's guess
    current_guess_string = current_guess_string[:-1]  # Slicing the string to get from index 0 to -1 (non inclusive), meaning it excludes the last letter
    current_guess.pop()
    current_letter_bg_x -= letter_spacing_X

# This is the main game loop 
while True:
    # If the game ends (ie. win or loss), the user will be prompted to play again, or they can exit the game
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # First, when the game is over (won or lost), user can press "Enter" to play again, so return key triggers a reset here
                if game_result != "":  
                    reset()
                # Otherwise if the user has pressed "Enter", it means they are submitting a word guess, so we call the check_guess() function
                else:  
                    if len(current_guess_string) == 5: 
                        check_guess(current_guess)
            # If the user presses the "Delete" key while typing, the system will call the delete_letter() function 
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            # If the user presses any letter key from the alphabet, the system calls the create_new_letter() function to draw that letter 
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
