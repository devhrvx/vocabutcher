from dotenv import load_dotenv
import os
import openai

#API Call
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4o-mini-2024-07-18",
    messages = [
        {"role": "system", "content": "You generate word formatted as: Category Word"},
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
        print(f'The word does not conatain \'{char}\'')
        lives -= 1
    
    return lives

def word_check(guess, word, lives):
    if guess == word:
        print(f'Congratulations! You guessed \'{word}\' correctly')
        return True, lives
    
    else:
        print(f'{guess} is not the word')
        lives -= 1
    
    return False, lives

def game_handler():
    #This is to get the response
    generated_word = response['choices'][0]['message']['content']

    #This is to slice the word
    word_sliced = generated_word.split()
    category = word_sliced[0]
    word = word_sliced[1].lower()

    listed_word = lister(word)
    blanked = blanker(listed_word)
    lives = 5

    while lives > 0 and '_' in blanked:
        print('\nWord to guess:', ' '.join(blanked))
        print(f'Lives remaining: {lives}')

        guess = input('Guess the letter or the word: ').lower()

        if len(guess) == 1:
            lives = char_check(guess, blanked, listed_word, lives)
        else:
            correct, lives = word_check(guess, word, lives)
            if correct:
                break
        
    if '_' not in blanked:
        print(f'\nWell done! You guessed the word \'{word}\'!')
    elif lives == 0:
        print(f'\nGame over! The word was \'{word}\'.')

game_handler()