from operator import contains
import numpy as np

# Get wordlist
wordlist = np.loadtxt("enhancedwordlist.txt", dtype='str')
starting_words = np.array(["crane", "slate", "least", "dealt"])

class WordleSolver:

    # Initilize
    def __init__(self, start, wordlist):
        self.wordlist = wordlist
        self.starting_words = start
        self.not_letters_array = np.array([])
        self.has_letters_array = np.array([])
        self.not_possible_words = np.array([])
        self.polished_possible_words = np.array([])
        self.built_word = ["#","#","#","#","#"]
        self.guesses = np.array([])

    def gametracker(self):
        for i_holder in range(0,6):
            if i_holder == 0:
                print("Starting Word:", self.starting_words[np.random.randint(0,self.starting_words.size)])
                print(self.feedback(), "\n")
                print(self.select_next_word(), "\n")
            else:
                print(self.feedback(), "\n")
                print(self.select_next_word(), "\n")

    def feedback(self):
        # User input
        guess_temp = str(input("Your input: ")).lower()
        correct_letters_temp = str(input("Which letters are in the correct spots, followed by their position (0 to 4), separate different letters by space: ")).lower().split()
        not_letters_temp = str(input("Letters not in word, separated by a space: ")).lower().split()
        has_letters_temp = str(input("Letters confirmed in word but position unknown: ")).lower().split()

        # Add guess
        self.guesses = np.append(self.guesses, guess_temp)
        print("Guesses so far: \n", self.guesses, "\n")

        # Build word based off of correct letters and positions
        for item in correct_letters_temp:
            self.built_word.insert(int(item[1]), item[0])
            self.built_word.pop(int(item[1])+1)

        # Add letters that are in not_letters_temp to not_letters_array
        for letter in not_letters_temp:
            self.not_letters_array = np.append(self.not_letters_array, letter)

        # Add letters that are in has_letters_temp to has letters array
        for letter in has_letters_temp:
            self.has_letters_array = np.append(self.has_letters_array, letter)
        
        # print out built word as a string
        print("Built Word:")
        return "".join(self.built_word)

    def select_next_word(self):
        ## Selects the next word ##
        
        # initialize array containing possible words to select
        possible_words_temp = np.array([])
        polished_possible_words_temp = np.array([])
        polished_possible_words_add_temp = np.array([])
        polished_possible_words_delete_temp = np.array([])

        # go through built word and put words from word list that match location of letters
        for let_pos in range(0,5):
            if self.built_word == ['#','#','#','#','#']:
                possible_words_temp = self.wordlist
                break
            let = self.built_word[let_pos]
            if let == "#":
                pass
            else:
                for word in self.wordlist:
                    if word[let_pos] != let:
                        self.not_possible_words = np.append(self.not_possible_words, word)
                    else:
                        possible_words_temp = np.append(possible_words_temp, word)
        
        # go through words and compare to list of letters not in the word, add to not_possible array
        for notlet_pos in range(0,self.not_letters_array.size):
            notlet = self.not_letters_array[notlet_pos]
            for posword in possible_words_temp:
                if notlet in posword:
                    self.not_possible_words = np.append(self.not_possible_words, posword)
        
        # remove duplicates (and sort)
        self.not_possible_words = np.unique(self.not_possible_words)
        possible_words_temp = np.unique(possible_words_temp)

        # compare not possible and possible arrays, create polished array
        polished_possible_words_temp = np.setdiff1d(possible_words_temp,self.not_possible_words)

        # remove duplicates(and sort)
        polished_possible_words_temp = np.unique(polished_possible_words_temp)

        # go through words and determine if they contain a letter not a position x, remove words that don't qualify
        if self.has_letters_array.size > 0:
            for letter in self.has_letters_array:
                for word in polished_possible_words_temp:
                    if letter in word:
                        polished_possible_words_add_temp = np.append(polished_possible_words_add_temp, word)
                    else:
                        polished_possible_words_delete_temp = np.append(polished_possible_words_delete_temp, word)
            self.polished_possible_words = np.setdiff1d(polished_possible_words_add_temp,polished_possible_words_delete_temp)
        else:
            self.polished_possible_words = polished_possible_words_temp
        
        # remove previous guesses from polished list
        self.polished_possible_words = np.setdiff1d(self.polished_possible_words, self.guesses)

        # return a random word
        print("Doesn't have letters: \n", self.not_letters_array,"\n")
        print("Has letters: \n", self.has_letters_array,"\n")
        print("Next guess:")
        return self.polished_possible_words[np.random.randint(0,self.polished_possible_words.size)]


# game = WordleSolver(starting_words, wordlist)
# game.gametracker()
