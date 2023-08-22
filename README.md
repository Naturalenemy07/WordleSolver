# WordleSolver

### As of June 2023, Chrome for Testing is released, see [CfT](https://developer.chrome.com/blog/chrome-for-testing/) and [GoogleChromeLabs CfT](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints). I will update the README and code to reflect usage of CfT, at this time school is starting and I have limited time, but will update it as soon as possible.

This repository contains programs to solve [Wordle](https://www.nytimes.com/games/wordle/index.html) puzzles.  bf_solver is a manual input program using enhancedwordlist as a database of words.  wordle_solver and wordle_logic work together to automatically solve the wordle puzzle using the same database.  wordle_solver will interact with the [Wordle](https://www.nytimes.com/games/wordle/index.html) website to gather feedback and input guesses based on that feedback.  A initial wordlist is hardcoded to four recommended words to start with.  wordle_logic contains the brute force algorithm that narrows down the possible words based on what letters are correct, present and absent.  

wordle_solver uses [Selenium](https://www.selenium.dev/) and [ChromeDriver](https://chromedriver.chromium.org/downloads) for automated website interaction. Drivers also exist for other popular browsers, see [Selenium Browser Drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) for the list.

Currently, plans are to develop more interesting algorithms to solve wordle puzzles.  Feel free to go ahead and use these as a baseline for your own wordle solvers.

You will need to download [Selenium](https://www.selenium.dev/) and [ChromeDriver](https://chromedriver.chromium.org/downloads) prior to use.  wordle_solver will check for Chromedriver updates and update accordingly using [webdriver-auto-update](https://pypi.org/project/webdriver-auto-update/).



### Packages
selenium  
webdriver_auto_update  
numpy  
time
