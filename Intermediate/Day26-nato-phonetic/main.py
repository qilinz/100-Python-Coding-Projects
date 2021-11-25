import pandas as pd

# save the csv file to a dict
df = pd.read_csv("nato_phonetic_alphabet.csv")

# practicing dict comprehension instead of using to_dict()
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# create the interface of the game
def nato():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato()
    else:
        print(output_list)


nato()
