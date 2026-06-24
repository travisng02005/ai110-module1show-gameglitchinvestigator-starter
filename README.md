# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The games purpose is to guess the number depending on the level of difficulty using the hints given to arrive to the correct answer within a given amount of guesses.
- [ ] Detail which bugs you found.
The bugs I found was the reset game button not working, the hints pointing the player into the wrong direction, and lastly the game allowing the player to enter guesses outside of the range given.
- [ ] Explain what fixes you applied.
The fixes I applied was ensuring that using the reset game button resets that website state, flipping the hints so that they are now pointing to the right direction, and lastly limiting the range that the player can enter a number by not allowing numbers outside of the given range.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters 30
2. Game returns "Go higher!"
3. User enters a guess of 97 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Travis\Documents\VSCode\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 5 items                                                                                                                                                                                        

tests\test_game_logic.py .....                                                                                                                                                                     [100%]

=========================================================================================== 5 passed in 0.02s ===========================================================================================
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
