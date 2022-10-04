import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from solver import WordleSolver as ws
import numpy as np

# Get wordlist and create game
wordlist = np.loadtxt("path to wordlist", dtype='str')
starting_words = np.array(["crane", "slate", "least", "dealt"])
game = ws(starting_words, wordlist)

# Start up automated bot
s = Service('path to chromedriver.exe') # include executable file in filename
browser = webdriver.Chrome(service=s)
url = 'https://www.nytimes.com/games/wordle/index.html'
browser.get(url)
time.sleep(10)

# click on exit button
exit_button = browser.find_element(By.CLASS_NAME, 'game-icon')
exit_button.click()
time.sleep(5)

# now type in the first word
interactable = browser.find_element(By.CLASS_NAME, 'Key-module_key__Rv-Vp')
browser.implicitly_wait(5)
first_word = game.first_word()
for i in first_word:
    interactable.send_keys(i)
    time.sleep(0.3)

time.sleep(1)
interactable.send_keys(Keys.ENTER)
time.sleep(10)

# read aria-status, print
for i in range(1,6):
    status_input = str(browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div['+str(i)+']/div').get_attribute('outerHTML'))
    time.sleep(5)
    print(ws.get_status(status_input))
browser.quit()
