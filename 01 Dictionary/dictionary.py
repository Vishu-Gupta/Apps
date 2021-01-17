"""Program for a basic dictionary"""
import json
from difflib import get_close_matches
data = json.load(open('data.json', 'r')) # loads the json file as a dictionary
ERROR_MSG = "Word Doesn't exist. Please recheck the word"
def translate(search_word):
    """Method to search for the word in Data and return list of meanings"""
    search_word = search_word.lower()
    if search_word in data.keys(): 
        return data[search_word]  # first search for the lower case version of the word
    elif search_word.title() in data.keys():
        return data[search_word.title()]  # then search for the Title version of the word
    elif search_word.upper() in data.keys():
        return data[search_word.upper()]  # then search for the upper letter version of the word
    else:
        matching_word = find_match(search_word)
        if matching_word == ERROR_MSG:
            return ERROR_MSG
        else:
            return data[matching_word]

def find_match(word):
    """Method to find the closest match"""
    match_list = get_close_matches(word, data.keys(), cutoff=0.8)
    if len(match_list) == 0:
        return ERROR_MSG
    else:
        user_confirm = input(f"Did you mean {match_list[0]} Enter Y for Yes\n")
        if user_confirm in ['Y', 'y']:
            return match_list[0]
        else:
            return ERROR_MSG

search_word = input('Enter the word : ')
output = translate(search_word)

if type(output) == str:
    print(output)
else:
    for meaning in output:
        print(meaning)