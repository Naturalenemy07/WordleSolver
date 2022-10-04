import numpy as np

class WordleSolver:

    # Initilize
    def __init__(self, start, wordlist):
        self.wordlist = wordlist
        self.starting_words = start
        self.not_letters_array = np.array([])
        self.has_letters_array = np.array([])
        self.has_letters_pos_array = np.array([])
        self.not_possible_words = np.array([])
        self.polished_possible_words = np.array([])
        self.built_word = ["#","#","#","#","#"]
        self.guesses = np.array([])   

    def first_word(self):
        first_word = str(self.starting_words[np.random.randint(0,self.starting_words.size)])
        return first_word

    def feedback(self):
        # User input
        guess_temp = str(input("Your input: ")).lower()
        correct_letters_temp = str(input("Which letters are in the correct spots, followed by their position (0 to 4), separate different letters by space: ")).lower().split()
        not_letters_temp = str(input("Letters not in word, separated by a space: ")).lower().split()
        has_letters_pos_temp = str(input("Letters in word, include position not at, seperate position by space: ")).lower().split()

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

        # function that stores the letter and guess position it confirmed is not at
        for item in has_letters_pos_temp:
            self.has_letters_pos_array = np.append(self.has_letters_pos_array, item)
            self.has_letters_array = np.append(self.has_letters_array, item[0])

        # print out built word as a string
        print("\nBuilt Word: ", "".join(self.built_word), "\n")
        return 0


    def select_next_word(self):
        ## Selects the next word ##
        
        # initialize array containing possible words to select
        possible_words_temp = np.array([])
        polished_possible_words_temp = np.array([])
        polished_possible_words_add_temp = np.array([])
        polished_possible_words_delete_temp = np.array([])
        to_delete_array_temp = np.array([])

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

        # go through words and determine if they contain letter
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

        # go through polished possible words and add words that line up with letters position to to_delete_array, remove words from polished list
        if self.has_letters_pos_array.size > 0:
            for let_pos in self.has_letters_pos_array:
                let_temp = let_pos[0]
                pos_temp = int(let_pos[1])
                for word in self.polished_possible_words:
                    if word[pos_temp] == let_temp:
                        to_delete_array_temp = np.append(to_delete_array_temp, word)
            self.polished_possible_words = np.setdiff1d(self.polished_possible_words, to_delete_array_temp)
        else:
            pass
                            
        
        # remove previous guesses from polished list
        self.polished_possible_words = np.setdiff1d(self.polished_possible_words, self.guesses)

        # return a random word
        print("Doesn't have letters: \n", self.not_letters_array,"\n")
        print("Has letters, but not at these positions: \n",self.has_letters_pos_array, "\n")
        print("Next guess:", self.polished_possible_words[np.random.randint(0,self.polished_possible_words.size)], "\n")
        return 0

    def get_status(input):
        # take html input from wordle and return status of the letter
        html_text = input
        starting_int = int(html_text.find('aria-label="')+len('aria-label="'))
        ending_int = int(html_text.find('" aria-live='))
        aria_label = html_text[starting_int: ending_int]
        return aria_label
        
