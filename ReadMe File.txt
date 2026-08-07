Math Quiz Program

Author: Waseem Patel
Language: Python 3 using Tkinter

Purpose

This program helps students practise mathematics through Easy, Medium and Hard quizzes. Each quiz has 30 questions, three lives, a five-minute timer, a score, results page and leaderboard.

Before Running the Program

1. Make sure Python 3 and IDLE are installed.

2. Install the Pillow image library by entering this in Command Prompt:

py -m pip install pillow

3. Keep the Python file and the images folder together in the same project folder.

4. Do not rename the question images or images/heart.png.

How to Use the Program

1. Open the final Python file in IDLE.

2. Select Run > Run Module, or press F5.

3. The main menu will display Sign Up, Log in, Leaderboard and Exit.

4. Select Sign Up.

5. Enter a username and password between 5 and 30 characters long.

6. Select Confirm. A message will show that the account has been saved.

7. The program will return to the main menu.

8. Select Log in and enter the same username and password.

9. Select Confirm to open the difficulty screen.

10. Choose Easy, Medium or Hard, then select Confirm to begin.

11. Read the question and look at its image.

12. Type only the answer in the answer box. Do not type the unit shown beside it.

13. Numbers, decimals, negative values and fractions may be used where required.

14. Select Submit Answer, or press Enter.

15. A correct answer increases the score. A wrong answer removes one of the three lives.

16. If the answer is blank or contains invalid characters, follow the message shown and try again.

17. The program automatically moves to the next question after a correct or wrong answer.

The quiz ends when all 30 questions are completed, all three lives are lost or the five-minute timer reaches zero. The results page then displays the username, score, and time used, and whether the user won or lost. Select Main Menu to return to the beginning.

If you want to leave anytime throughout the quiz, select the red Exit button, and it will take you back to the difficulty screen.

Leaderboard Use / Access

1. Select Leaderboard from the main menu.

2. Choose Easy, Medium or Hard from the difficulty box.

3. The leaderboard displays each username's best score and time for that difficulty. Higher scores appear first. If scores are equal, the faster time appears first.

4. Select Exit to return to the main menu.

Saved Files

The program uses two text files:

1. LoginInfo.txt stores usernames and passwords created through Sign Up. So they can be used when logging in.

2. Leaderboard.txt stores quiz scores and times.

These files are separate, so removing a user from LoginInfo.txt will not remove their previous leaderboard score. Use a test password that is not used for an important personal account.

Common Problems to avoid when running the program:

Images do not load: Make sure the images folder is beside the Python file and that its files have not been renamed.

PIL cannot be found: Run py -m pip install pillow, then reopen IDLE.

Login is rejected: Make sure the account has been created and the username and password are typed exactly the same way.

Lastly, select the "Exit" button on the main menu to close the program.