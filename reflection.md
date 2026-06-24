# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked like a very generic webapp with a title, description of what the game is, and a entry box for the guess. The game looked very straight forward, but had an issue that practically made it unplayable being the backwards hints that it was outputting. This made it basically impossible to get the right answer unless you somehow guessed it without the use of the hints.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. Able to enter guess out of given range.
2. The hints were backwards, pointing me in the wrong direction.
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior  | Console Output / Error |
|-------|-------------------|------------------|------------------------|
| 1000  | Out of range      | "Go higher" hint | "none"
|  70   | "Go lower" hint   | "Go higher" hint | "none"
|  30   | "GO higher" hint  | "Go lower" hint  | "none"

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used claude ai for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One of the changes that the AI suggested that was correct was changing the logic of the game to correctly hint the player in the right direction. I verified the result by identifying the changes being made and ensuring that the logic made sense and that the direction the hint was given was correct and not in the wrong direction.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One of the changes that the AI suggested that was incorrect was to change the data type of the guess. This made it to where my numbers that I was entering into the text box was not able to be compared to the correct number due to a type error. I did not catch this initially but whenever I ran the program and attempted to play the game I ran into a type error and I then went back and asked claude for where the issue was and why it happened working with it to fix the type error.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I verified whether my bug was really fixed by running the same tests that failed before implementing the changes to ensure that the same cases now worked. I also threw other edge to the program that I did not do before to really make sure that the program ran as intended.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
I asked claude to create a pytest based off of the issues that we fixed together. I ran into an issue with this though as even though the pytest initally passed, whenever I manually tested the game I ran into issues that pytest did not catch. This showed that the code still had errors that the pytest did not catch showing the importance of also manually checking your code.
- Did AI help you design or understand any tests? How?
AI helped me design the pytest that I ran with the fixes that we implemented. The way I did this was asking claude to created pytest case tests to run into the program to tackle the issues that we attempted to fix together.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Think of a Streamlit app as a movie that starts from the beginning every time you interact with it.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit from this project that I will reuse in the future is using pytests as well as manually testing the code to ensure that all of it works properly.
- What is one thing you would do differently next time you work with AI on a coding task?
I will definitely monitor the AI even closer to ensure that no errors like the one that I faced happens when making changes to the code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed how I think about AI generated code by showing me first hand how AI can definitely mess up and that it is not perfect by any means and requires careful monitoring to ensure that it works. This made me believe that AI will definitely not take peoples jobs and that it is something that is not flawless.
