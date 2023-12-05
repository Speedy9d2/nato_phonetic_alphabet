import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = {row["letter"]: row["code"] for (index, row) in data.iterrows()}
print(new_data)

user_input = input("Enter a word ")
result = [new_data[word.upper()] for word in user_input]
print(result)
