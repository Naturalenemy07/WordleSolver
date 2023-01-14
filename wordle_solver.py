import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from wordle_logic import WordleSolver as ws
from checkdriver import Checker
import numpy as np

# Get wordlist and create game
pathToCDexe = 'path\to\chromedriver.exe'
pathToCD = 'path\to\chromedriver_win32'
wordlist = np.loadtxt("path\to\enhancedwordlist.txt", dtype='str')
starting_words = np.array(["reach", "dealt", "salet", "crane", "audio"])
game = ws(starting_words, wordlist)

# Update Chromedriver as needed
ckr = Checker(pathToCD)

# Start up automated bot
s = Service(pathToCDexe)
browser = webdriver.Chrome(service=s)
url = 'https://www.nytimes.com/games/wordle/index.html'
browser.get(url)
time.sleep(5)

# click on exit button on popup
exit_button = browser.find_element(By.CLASS_NAME, 'game-icon')
exit_button.click()
time.sleep(2)

# find interactable element
interactable = browser.find_element(By.CLASS_NAME, 'Key-module_key__kchQI')
browser.implicitly_wait(10)

def type_in_word(word):
    # hard coded to type in 5 letters similar to human, press enter
    for i in word:
            interactable.send_keys(i)
            time.sleep(0.2)
    time.sleep(1)
    interactable.send_keys(Keys.ENTER)
    time.sleep(3)
    return 0

def check_status(row):
    # interacts with wordle html and finds status of each letter with by passing to WordleSolver.get_status
    word_status_list = []
    for let_pos in range(1,6):
        try:
            status_input = str(browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div['+str(row)+']/div['+str(let_pos)+']/div').get_attribute('outerHTML'))
        except:
            status_input = str(browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div['+str(row)+']/div['+str(let_pos)+']/div').get_attribute('outerHTML'))
        browser.implicitly_wait(10)
        word_status_list.append(game.return_aria_label(status_input))
    return word_status_list

for row in range(1, 7):
# hard coded to repeat 6 times, can break out of loop if detects game success
    if row == 1:
    # Inputs first word
        first_word = game.first_word()
        time.sleep(2)
        type_in_word(first_word)
    else:
    # inputs guessed word with output from check status
        next_word = game.feedback_select(word_status)
        time.sleep(2)
        type_in_word(next_word)
    
    #  check status, get numpy array containing status of each letter
    word_status = check_status(row)

    # Checks to see status, if status_int is 5, that means all letters are correct
    if game.game_end(word_status):
        print("Solved!")
        browser.quit()
        quit()
