# Hangman

import random
from hphprint import stages

names = ("Hermione Granger", "Ronald weasley", "Fred Weaslye", "George Weasley",
"Ginevra Weasley", "Molly Weasley", "Arthur Weasley", "Percy Weasley", "Harry Potter",
"James Potter", "Dobby", "Kreacher", "Sirius Black", "Albus Dumbledore", "Fillius Flitwick",
"Rubeus Hagrid", "Minerva McGonagall", "Remus Lupin", "Sybill Trelawney", "Severus Snape",
"Gilderoy Lockhart", "Errol", "Fawkes", "Buckbeak", "Hedwig", "AKA Nearly Headless Nick",
"Salazar Slytherin", "Rowena Ravenclaw", "Helga Hufflepuff", "Godric Gryffindor", "Vincent Crabbe",
"Gregory Goyle", "Neville Longbottom", "Draco Malfoy", "Igor Karkaroff", "Peter Pettigrew",
"Lucius Malfoy", "Bellatrix Lestrange", "Barty Crouch Jr.", "Tom Marvolo Riddle - Lord Voldemort")

sepparator = "=" * 42
random_word = random.choice(names).lower()
hidden_word = []
attemp = 6

for i in random_word:
    hidden_word.append("_")

print(f"""{sepparator}
Welcome to the Harry Potter hangman game!
{sepparator}""")

print(stages[6])
print(f"""Here is your hidden word:\n {"".join(hidden_word)}, \n""")

while "_" in hidden_word:
    letter = input("Enter a possible letter(or space):\n").lower()
    if letter not in random_word:
        attemp -= 1
        print(stages[int(attemp)])
        if attemp == 0:
            print(f"Game over! Hidden word was: {random_word}")
            break
            
    else:
        for index in range(0, len(random_word)):
            if letter in random_word[index]:
                hidden_word[index] = letter

    print("".join(hidden_word))
    print(f"You have {attemp} attemps\n")

if "".join(hidden_word) == random_word:
    print(f"""
{20*"="}
    You win!
{20*"="}""")