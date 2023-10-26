import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = pandas.DataFrame(nato_phonetic_alphabet)

phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


def generate_phonetic():
    word = input("Enter the word.").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Enter a WORD, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
