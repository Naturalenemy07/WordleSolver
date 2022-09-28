from operator import contains
import numpy as np

# Get wordlist
wordlist = np.loadtxt("enhancedwordlist.txt", dtype='str')
# wordlist = np.unique(wordlist_pre)
# np.savetxt('enhancedwordlist.txt', wordlist, fmt="%s")

# Initilize
starting_words = np.array(["crane", "slate", "least", "dealt"])
first_word = starting_words[np.random.randint(0,starting_words.size)]
not_letters_array = np.array([])
has_letters_array = np.array([])
built_word = ["#","#","#","#","#"]

def feedback():
    ##takes feedback from user (hopefully to be automated later) and returns built word ##
    global not_letters_array, built_word, has_letters_array

    # Print first word
    print("First word:",first_word)

    # User input
    correct_letters_temp = str(input("Which letters are in the correct spots, followed by their position (0 to 4), seperate different letters by space: ")).split()
    not_letters_temp = str(input("Letters not in word, seperated by a space: ")).split()
    has_letters_temp = str(input("Letters confirmed in word but position unknown: ")).split()

    # Build word based off of correct letters and positions
    for item in correct_letters_temp:
        built_word.insert(int(item[1]), item[0])
        built_word.pop(int(item[1])+1)

    # Add letters that are in not_letters_temp to not_letters_array
    for letter in not_letters_temp:
        not_letters_array = np.append(not_letters_array, letter)

    # Add letters that are in has_letters_temp to has letters array
    for letter in has_letters_temp:
        has_letters_array = np.append(has_letters_array, letter)
    
    # print out built word as a string
    print("".join(built_word))
    return 0

def select_next_word():
    ## Selects the next word ##
    global built_word, wordlist, not_letters_array
    
    # initialize array containing possible words to select
    possible_words = np.array([])
    not_possible_words = np.array([])
    polished_possible_words = np.array([])
    polished_possible_words_add = np.array([])
    polished_possible_words_delete = np.array([])
    super_polished_possible_words = np.array([])

    # go through built word and put words from word list that match location of letters
    for let_pos in range(0,5):
        if built_word == ['#','#','#','#','#']:
            possible_words = wordlist
            break
        let = built_word[let_pos]
        if let == "#":
            pass
        else:
            for word in wordlist:
                if word[let_pos] != let:
                    not_possible_words = np.append(not_possible_words, word)
                else:
                    possible_words = np.append(possible_words, word)
    
    # go through words and compare to list of letters not in the word, add to not_possible array
    for notlet_pos in range(0,not_letters_array.size):
        notlet = not_letters_array[notlet_pos]
        for posword in possible_words:
            if notlet in posword:
                not_possible_words = np.append(not_possible_words, posword)
    
    # remove duplicates (and sort)
    not_possible_words = np.unique(not_possible_words)
    possible_words = np.unique(possible_words)

    # compare not possible and possible arrays, create polished array
    polished_possible_words = np.setdiff1d(possible_words,not_possible_words)

    # remove duplicates(and sort)
    polished_possible_words = np.unique(polished_possible_words)

    # go through words and determine if they contain a letter not a position x, remove words that don't qualify.
    if has_letters_array.size > 0:
        for letter in has_letters_array:
            print(letter)
            for word in polished_possible_words:
                print(word)
                if letter in word:
                    print("adding:",word)
                    polished_possible_words_add = np.append(polished_possible_words_add, word)
                else:
                    polished_possible_words_delete = np.append(polished_possible_words_delete, word)
    else:
        super_polished_possible_words = polished_possible_words

    # create super polished by removing words that don't contain all possible letters
    super_polished_possible_words = np.setdiff1d(polished_possible_words_add,polished_possible_words_delete)

    # return a random word
    print("Next word\n",super_polished_possible_words[np.random.randint(0,super_polished_possible_words.size)])

feedback()
select_next_word()
