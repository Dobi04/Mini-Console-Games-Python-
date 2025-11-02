import random



def picking(words):
    len_words = len(words)
    index = random.randint(0, len_words-1)

    picked_word = words[index]
    hiden_word = ["_"] * len(picked_word)
    return picked_word, hiden_word

def is_WIN(hiden_word):
    for char in hiden_word:
        if char == "_":
            return False
    return True

def print_WIN():
    print("***************************")
    print("----------YOU WON----------")
    print("***************************")

def print_LOSE():
    print("****************************")
    print("----------YOU LOST----------")
    print("****************************")

def take_a_guess(gess, picked_word, hiden_word, wrong_gesses):
    index = picked_word.find(gess)
    for ind, character in enumerate(picked_word):
        if character == gess:
            hiden_word[ind] = gess

    is_correct_gess = True if index != -1 else False
    if index == -1:
        print("There is no such letter in this picked word. ")
        wrong_gesses.append(gess)

    return hiden_word, is_correct_gess, wrong_gesses


words = [
    "elephant", "giraffe", "penguin", "dolphin", "crocodile",  # Animals
    "brazil", "canada", "germany", "japan", "sweden",          # Countries
    "keyboard", "backpack", "umbrella", "airplane", "sandwich", # Objects
    "mystery", "journey", "sunshine", "whisper", "freedom"      # Common words
]
picked_word, hiden_word = picking(words)
wrong_gesses=[]

def hangman_art(hiden_word):
    hangman_art = { 0: (" __________",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),
                    1: (" __________",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),
                    2: (" __________",
                    "  |     |   ",
                    "  |   (*_*) ",
                    "  |         ",
                    "  |         ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),
                    3: (" __________",
                    "  |     |   ",
                    "  |   (*_*) ",
                    "  |     |   ",
                    "  |         ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),
                    4: (" __________",
                    "  |     |   ",
                    "  |   (*_*) ",
                    "  |    /|\\ ",
                    "  |         ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),
                    5: (" __________",
                    "  |     |   ",
                    "  |   (*_*) ",
                    "  |    /|\\ ",
                    "  |    /    ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),
                    6: (" __________",
                    "  |     |   ",
                    "  |   (*_*) ",
                    "  |    /|\\ ",
                    "  |    / \\ ",
                    "  |         ",
                    f"__|_________       {hiden_word}"),}
    return hangman_art

i=0
while True:
    i+=1  
    hangman = hangman_art(hiden_word)
    for line in hangman.get(i):
        print(line)

    print(f"Wrong gesses: {wrong_gesses}")
    gess = input("Enter a gess: ").lower()
    hiden_word, is_correct_gess, wrong_gesses = take_a_guess(gess, picked_word, hiden_word, wrong_gesses)

    hangman = hangman_art(hiden_word)

    if is_correct_gess == True:
        i-=1

    if is_WIN(hiden_word) == True:
        for line in hangman.get(i):
            print(line)
        print_WIN()
        break


    if i == 5:
        for line in hangman.get(6):
            print(line)
        print(wrong_gesses)
        print_LOSE()
        break
 