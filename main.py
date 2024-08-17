from dotenv import load_dotenv
import os
import openai
import time as t

#API Call
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4o-mini-2024-07-18",
    messages = [
        # Moderate the difficulty of the system here!!! (P.S. This is so difficult)
        {"role": "system", "content": "You generate hard word formatted as: Category Word"},
        {"role": "user", "content": "Give a word and its category"}
    ]
)

def lister(word):
    listed_word = []
    for i in word:
        listed_word.append(i)
    
    return listed_word

def blanker(listed_word):
    blanked = []
    for i in listed_word:
        blanked.append('_')
    
    return blanked

def display_blanks(blanked):
    for i in blanked:
        print(i, end=' ')

def char_check(char, blanked, listed_word, lives):
    matched = False
    for index, letter in enumerate(listed_word):
        if letter == char:
            blanked[index] = char
            matched = True
    
    if not matched:
        limb_lose = 'You will lose a limb for that.'
        print(f'\nThe word does not contain \'{char}\'')
        t.sleep(.4)
        for i in limb_lose:
            print(i, end='', flush=True)
            t.sleep(.07)
        lives -= 1
    
    return lives

def word_check(guess, word, lives):
    if guess == word:
        print(f'Congratulations! You guessed \'{word}\' correctly')
        print("""
        
       █  ██   ██  █
        █         █
         █████████

""")
        return True, lives
    
    else:
        print(f'{guess} is not the word')
        lives -= 1
    
    return False, lives

def difficulty(letter):
    if letter[0].lower() == 'a':

        return 7
    elif letter[0].lower() == 'b':
        return 6
    else:
        return 5
    
def limb_handler(lives):
    if lives == 7:
        return """
         O
        /|\\
         |
         |
        / \\
        """
    elif lives == 6:
        return """
         O
        /|\\
         |
        / \\
        """
    elif lives == 5:
        return """
         O
        /|\\
        / \\
        """
    elif lives == 4:
        return """
         O
        /|
        / \\
        """
    elif lives == 3:
        return """
         O
         |
        / \\
        """
    elif lives == 2:
        return """
         O
         |
        / 
        """
    elif lives == 1:
        return """
         O
         |
        """
    else:
        return """
         O
        """

def game_handler():
    #This is to get the response from the API call
    generated_word = response['choices'][0]['message']['content']

    #difficulty input
    print('\nChoose difficulty:\n\t[a] Easy\n\t[b] Normal\n\t[c] Hard')
    difficulty_char = input()
    #This is to slice the word
    word_sliced = generated_word.split()
    category = word_sliced[0]
    word = word_sliced[1].lower()

    listed_word = lister(word)
    blanked = blanker(listed_word)
    lives = difficulty(difficulty_char)

    while lives > 0 and '_' in blanked:
        t.sleep(.5)
        print('\n\nCategory: ', category)
        print('Word to guess:', ' '.join(blanked))
        print(f'Lives remaining: {lives}')
        print(limb_handler(lives))

        guess = input('Guess the letter or the word: ').lower()

        if len(guess) == 1:
            lives = char_check(guess, blanked, listed_word, lives)
        else:
            correct, lives = word_check(guess, word, lives)
            if correct:
                break
        
    if lives == 0:
        t.sleep(.6)
        print(f'\n\nGame over! The word was \'{word}\'.')
        t.sleep(.3)
        print('Bruh.')
        t.sleep(.3)
        print("""
         ██   ██
    
        ████████
       █        █
        ████████
""")

game_handler()