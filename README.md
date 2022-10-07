# WordleSolver

This repository contains programs to solve [Wordle](https://www.nytimes.com/games/wordle/index.html) puzzles.  bf_solver.py is a manual input program using enhancedwordlist.txt as a database of words.  wordle_solver.py and wordle_logic.py work together to automatically solve the wordle puzzle using the same database.  solver will interact with the [Wordle](https://www.nytimes.com/games/wordle/index.html) website to gather feedback and input guesses based on that feedback.  A initial wordlist is hardcoded to four recommended words to start with.  logic is the brute force algorithm that narrows down the possible words based on what letters are correct, present and absent.  

wordle_solver uses [Selenium](https://selenium-python.readthedocs.io/) and [Selenium.dev](https://www.selenium.dev/) and [ChromeDriver](https://chromedriver.chromium.org/downloads) for automated website interaction. Drivers also exist for other popular browsers.

Currently, plans are to develop more interesting algorithms to solve wordle puzzles.  Feel free to go ahead and use these as a baseline for your own wordle solvers.
