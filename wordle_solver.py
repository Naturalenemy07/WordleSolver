import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from wordle_logic import WordleSolver as ws
# from checkdriver import Checker
import numpy as np

# Get wordlist and create game
# pathToCDexe = 'C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\chromedriver_win32\\chromedriver.exe'
# pathToCD = 'C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\chromedriver_win32'
wordlist = np.loadtxt('C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\wordlesolver\\enhancedwordlist.txt', dtype='str')
starting_words = np.array(["reach", "dealt", "salet", "crane", "audio", "lousy"])
game = ws(starting_words, wordlist)

# Update Chromedriver as needed
# ckr = Checker(pathToCD)

# Start up automated bot
# s = Service(pathToCDexe)
browser = webdriver.Firefox()
actions = ActionChains(browser) 
# browser = webdriver.Chrome(service=s)
url = 'https://www.nytimes.com/games/wordle/index.html'
browser.get(url)
time.sleep(5)

# click on button to play
# play_button = browser.find_element(By.CLASS_NAME, 'Welcome-module_button__ZG0Zh') # This is the subscribe button
inits = 0
try:
    play_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/button[2]')
    play_button.click()
    time.sleep(5)
except:
    # This is a popup for terms and conditions
    popups = browser.find_element(By.CLASS_NAME, ("purr-blocker-card__button"))
    popups.click()
    time.sleep(5)

    welcome_box = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]')
    print("welcome box\n",welcome_box)

    play_button = browser.find_element(By.CSS_SELECTOR, '[data-testid="Play"]')
    play_button.click()

# click on exit button on popup
exit_button = browser.find_element(By.CLASS_NAME, 'game-icon')
exit_button.click()
time.sleep(2)

# find interactable element (this sometimes changes...)
interactable = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/main/div[2]/div[3]/button[1]') #Enter button
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
            status_input = str(browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/main/div[1]/div/div['+str(row)+']/div['+str(let_pos)+']/div').get_attribute('outerHTML'))
        except:
            raise Exception
        # try:
        #     status_input = str(browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div['+str(row)+']/div['+str(let_pos)+']/div').get_attribute('outerHTML'))
        # except:
        #     status_input = str(browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div['+str(row)+']/div['+str(let_pos)+']/div').get_attribute('outerHTML'))
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
        print(f"Next guess: {next_word}\n")
        time.sleep(2)
        type_in_word(next_word)
    
    #  check status, get numpy array containing status of each letter
    word_status = check_status(row)

    # Checks to see status, if status_int is 5, that means all letters are correct
    if game.game_end(word_status):
        print(f"Solved! Correct word is: {next_word}")
        browser.quit()
        quit()
