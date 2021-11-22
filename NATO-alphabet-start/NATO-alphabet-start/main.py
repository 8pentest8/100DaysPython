import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_data = input("Input your's name: ").upper()
alphabet_list = [alphabet_dict[letter] for letter in input_data]
print(alphabet_list)
