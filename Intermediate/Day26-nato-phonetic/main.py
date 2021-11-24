import pandas as pd

# save the csv file to a dict
df = pd.read_csv("nato_phonetic_alphabet.csv")

# practicing dict comprehension instead of using to_dict()
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# create the interface of the game
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]

print(output_list)