import numpy as np

class WordleSolver:

    # Initilize
    def __init__(self, start, wordlist):
        self.wordlist = wordlist
        self.possible_words = wordlist
        self.starting_words = start
        self.absent_letters_array = np.array([])
        self.correct_letters_array = np.array([])
        self.present_letters_array = np.array([])
        self.built_word = ["#","#","#","#","#"]

    def first_word(self):
        first_word = str(self.starting_words[np.random.randint(0,self.starting_words.size)])
        return first_word

    def feedback_select(self, status):
        correct_letters_temp = []
        absent_letters_temp = []
        present_letters_temp = []

        # Input as a list, add to appropriate lists
        guess_temp = ""
        for stat in range(0,5):
            guess_temp += status[stat][0].lower()
            if "correct" in status[stat]:
                # ["a0" "b1" "c2"] letter followed by correct position
                correct_letters_temp.append(str(status[stat][0]+str(stat)))
            elif "absent" in status[stat]:
                # ["a" "b" "c"]
                absent_letters_temp.append(str(status[stat][0]))
            elif "present" in status[stat]:
                # ["a0" "b1" "c2"] letter followed by position not in
                present_letters_temp.append(str(status[stat][0]+str(stat)))

        # Build word based off of correct letters and positions
        for item in correct_letters_temp:
            self.built_word.insert(int(item[1]), item[0])
            self.built_word.pop(int(item[1])+1)

        # Add new letters that are in absent_letters_temp to absent_letters_array
        for letter in absent_letters_temp:
            self.absent_letters_array = np.append(self.absent_letters_array, letter)

        # function that stores the letter and guess position it confirmed is not at
        for item in present_letters_temp:
            self.present_letters_array = np.append(self.present_letters_array, item)

        ###########################
        ## Selects the next word ##
        ###########################

        words_to_delete = np.array([])

        # go through "possible words array", add words to "words to delete" that contain letters in "absent letters"
        for letter in absent_letters_temp:
            for word in self.possible_words:
                if letter in self.built_word:
                    pass
                elif letter in word:
                    words_to_delete = np.append(words_to_delete, word)

        # go through "possible words array", add words to "words to delete" words that contain letter at position in "present letters"
        for letter_position in present_letters_temp:
            for word in self.possible_words:
                # if 
                if letter_position[0] not in word:
                    words_to_delete = np.append(words_to_delete, word)
                elif word[int(letter_position[1])] == letter_position[0]:
                    words_to_delete = np.append(words_to_delete, word)
                
        # add previous guess to "words_to_delete"
        words_to_delete = np.append(words_to_delete, guess_temp)

        # Next compare built word to words in possible words
        for let_pos in range(0,5):
            if self.built_word == ['#','#','#','#','#']:
                break
            let = self.built_word[let_pos]
            if let == "#":
                pass
            else:
                for word in self.possible_words:
                    if word[let_pos] != let:
                        words_to_delete = np.append(words_to_delete, word)
        
        # remove words that do not match position of built word
        self.possible_words = np.setdiff1d(self.possible_words, words_to_delete)

        return self.possible_words[np.random.randint(0,self.possible_words.size)]

    def return_aria_label(self, input):
        html_text = input
        starting_int = int(html_text.find('aria-label="')+len('aria-label="'))
        ending_int = int(html_text.find('" aria-live='))
        aria_label = html_text[starting_int: ending_int]
        return aria_label

    def game_end(self, input):
        status_int = 0
        for stat in input:
            if "correct" in stat:
                status_int += 1
        if status_int == 5:
            return True
        else:
            return False
