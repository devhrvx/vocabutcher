from dotenv import load_dotenv
import os
import openai


#Functions
def list_ize(word):
    #list type a word
    listed = []
    for letter in word:
        listed.append(letter)
    
    return listed

def blanker(list):
    blanked = []
    for i in list:
        blanked.append('_')
    
    blanked_string = " ".join(blanked)
    return blanked_string

# def guess_letter(letter, list, blanked):
    #find if a letter exists on a list

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

#This is to get the response
generated_word = response['choices'][0]['message']['content']

#This is to slice the word
word_sliced = generated_word.split()

category = word_sliced[0]
word = word_sliced[1]

print(f'\nCategory: {category}\nWord: {word}')

listed_word = list_ize(word)
blanks = blanker(listed_word)
print('\n', listed_word, '\n', blanks)

# letter_input = str(input("Guess a letter:\t"))
# letter = letter_input[0]


