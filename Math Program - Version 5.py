'''
# Author: Waseem Patel
# Date: 09/06/2026
# Purpose: To create a Math quiz / game to help students have fun doing math in an interactive way
'''

# Import tkinter and ttk for GUI creation.
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import random

# These are the dimensions, possible colours, fonts, etc of the entire GUI
window_width = 900
window_height = 585
text_colour = "black"
button_colour = "#CFF2FF"
button_hover_colour = "#f2f2f2"
title_font = ("Arial", 28, "bold")
button_font = ("Arial", 22)
button_width = 255
button_height = 68
centre_x = window_width // 2
button_x = centre_x - button_width // 2


userFile="LoginInfo.txt"

class MathQuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Math Quiz")
        self.root.geometry("900x585")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root, bg = "#87CEEB", highlightbackground = "black", highlightthickness = 2)
        self.main_frame.pack(fill="both", expand=True)
        self.current_username = ""
        self.timer_job = None
        self.show_main_menu()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_menu_button(self, text, y_position, command):
        button = tk.Button(self.main_frame, text = text, font = ("Georgia", 25, "bold") , bg = button_colour, fg = text_colour, activebackground = button_hover_colour, activeforeground = text_colour, relief = "solid", borderwidth = 1, command = command)

        button.place(x = button_x, y = y_position, width = button_width, height = button_height)
        return button

# This is the displays the title of the GUI
    def show_main_menu(self):
        self.clear_screen()

        # This creates the main label on the GUI, welcoming the user
        title_label = tk.Label(self.main_frame, text = "Welcome to the Math Quiz", font = ("Georgia", 28, "bold"), bg= "#87CEEB", fg = text_colour)

        title_label.place(x = 0, y = 20, width = window_width, height = 45)

        self.create_menu_button("Sign Up", 120, self.open_sign_up)
        self.create_menu_button("Log in", 230, self.open_log_in)
        self.create_menu_button("Leaderboard", 338, self.open_leaderboard)
        self.create_menu_button("Exit", 442, self.exit_program)

    # This function displays the sign up section for the user to use
    def open_sign_up(self):
        self.clear_screen()

        # This creates the labels for the GUI, so the user can navigate on what to do
        title_label = tk.Label(self.main_frame, text = "<Sign Up Below>", font = title_font, bg = "#87CEEB", fg = text_colour, height = 50)
        username_label = tk.Label(self.main_frame, text = "Username:", fg = "#000000", font = title_font, bg = "#87CEEB")
        password_label = tk.Label(self.main_frame, text = "Password:", fg = "#000000", font = title_font, bg = "#87CEEB")
        self.username_entry = tk.Entry(self.main_frame, font = ("Arial", 18), relief = "solid", borderwidth = 1)
        self.password_entry = tk.Entry(self.main_frame,font = ("Arial", 18), relief = "solid", borderwidth = 1, show = "*")
        button_signup = tk.Button(self.main_frame, text = "Confirm", fg = "#000000", font = title_font, bg = "#87CEEB", relief = "solid", borderwidth = 1, command = self.save_signup)

        # This places each of the buttons in its specific area on the GUI
        button_signup.place(x = 375, y = 400, width = 250, height = 50)
        self.password_entry.place(x = 350, y = 300, width = 330, height = 50)
        self.username_entry.place(x = 350, y = 200, width = 330, height = 50)
        password_label.place(x = 100, y = 300, width = 200, height = 50)
        username_label.place(x = 100, y = 200, width = 200, height = 50)
        title_label.place(x = 0, y = 40, width = window_width, height = 50)

        self.create_back_button()    

    # This function saves the sign up details that the user inserts 
    def save_signup(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # This section creates minimums and maximums for the number of characters allowed when signing up
        if len(username) > 30:
            messagebox.showerror("Error", "Username must be 30 characters or less.")
            return

        if len(username) < 5:
            messagebox.showerror("Error", "Username must be more than 5 characters.")
            return

        if len(password) > 30:
            messagebox.showerror("Error", "Password must be 30 characters or less.")
            return

        if len(password) < 5:
            messagebox.showerror("Error", "Password must be more than 5 characters.")
            return

        file = open("LoginInfo.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()

        messagebox.showinfo("Success", "Account saved.")
        self.show_main_menu()

    # This function creates the log in section for the user to use
    def open_log_in(self):
        self.clear_screen()

        # This section creates the labels of the GUI, so the user can navigate it with ease
        title_label = tk.Label(self.main_frame,text = "<Log In Below>", font = title_font, bg = "#87CEEB", fg = text_colour, height = 50)
        login_username_label = tk.Label(self.main_frame, text = "Username:", fg = "#000000", font = title_font, bg = "#87CEEB")
        login_password_label = tk.Label(self.main_frame, text = "Password:", fg = "#000000", font = title_font, bg = "#87CEEB")
        self.username_entry_login = tk.Entry(self.main_frame, font = ("Arial", 18), relief = "solid", borderwidth = 1)
        self.password_entry_login = tk.Entry(self.main_frame, font = ("Arial", 18), relief = "solid", borderwidth = 1, show = "*")
        button_login = tk.Button(self.main_frame, text = "Confirm", fg = "#000000", font = title_font, bg = "#87CEEB", relief = "solid", borderwidth = 1, command = self.check_login)
        
        # This section places the button, label, and typing box it in designated area
        button_login.place(x = 375, y = 400, width = 250, height = 50)
        self.password_entry_login.place(x = 350, y = 300, width = 330, height = 50)
        self.username_entry_login.place(x = 350, y = 200, width = 330, height = 50)
        login_password_label.place(x = 100, y = 300, width = 200, height = 50)
        login_username_label.place(x = 100, y = 200, width = 200, height = 50)
        title_label.place(x = 0, y = 40, width = window_width, height = 50)

        self.create_back_button()

    # This function checks whether the log in information inserted is the same as the sign up information
    def check_login(self):
        username = self.username_entry_login.get().strip()
        password = self.password_entry_login.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # This section creates minimums and maximums for the number of characters allowed when logging in
        if len(username) > 30:
            messagebox.showerror("Error", "Username must be 30 characters or less.")
            return

        if len(username) < 5:
            messagebox.showerror("Error", "Username must be more than 5 characters.")
            return

        if len(password) > 30:
            messagebox.showerror("Error", "Password must be 30 characters or less.")
            return

        if len(password) < 5:
            messagebox.showerror("Error", "Password must be more than 5 characters.")
            return

        try:
            file = open("LoginInfo.txt", "r")
            saved_users = file.readlines()
            file.close()
        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts have been created yet.")
            return

        for user in saved_users:
            user = user.strip()

            if user == "":
                continue

            details = user.split(",")

            if len(details) == 2:
                saved_username = details[0]
                saved_password = details[1]

                if username == saved_username and password == saved_password:
                    self.current_username = username
                    messagebox.showinfo("Success", "Log in successful.")
                    self.difficulty_selection()
                    return

        messagebox.showerror("Error", "Incorrect username or password.")

    # This function is for the difficulties, allowing the user to choose between the three difficulties
    def difficulty_selection(self):
        self.clear_screen()

        title_label = tk.Label(self.main_frame, text = "<Choose Your Difficulty>", font = title_font, bg = "#87CEEB", fg = text_colour, height = 50)

        title_label.place(x = 0, y = 40, width = window_width, height = 50)

        self.login_back_button()

        self.difficulty_box = tk.Listbox(self.main_frame, font = ("Arial", 28, "bold"), bg = "white", fg = "black", relief = "solid", borderwidth = 1)

        self.difficulty_box.place(x = 320, y = 200, width = 250, height = 140)

        # These are the three difficulties the user can choose from
        self.difficulty_box.insert(1, ">Easy\n")
        self.difficulty_box.insert(2, ">Medium\n")
        self.difficulty_box.insert(3, ">Hard\n")
        self.difficulty_box.select_set(0)
        self.difficulty_box.focus_set()

        button_confirm = tk.Button(self.main_frame, text = "Confirm", fg = "#000000", font = title_font, bg = "#87CEEB", relief = "solid", borderwidth = 1, command = self.check_difficulty)
        
        button_confirm.place(x = 320, y = 400, width = 250, height = 50)

    # This function checks which difficulty the user selected
    def check_difficulty(self):
        selected_option = self.difficulty_box.curselection()

        if len(selected_option) == 0:
            messagebox.showerror("Error", "Please select a difficulty.")
            return

        chosen_difficulty = self.difficulty_box.get(selected_option[0])

        if "Easy" in chosen_difficulty:
            self.math_quiz()
        else:
            messagebox.showinfo("Unavailable", "This difficulty has not been created yet.")

    def math_quiz(self):
        self.clear_screen()
            # This function displays the Easy math quiz question
    def math_quiz(self):
        self.clear_screen()

        # These variables are set when the quiz begins
        self.score = 0
        self.time_left = 300
        self.question_answered = False
        self.quiz_active = True
        self.timer_job = None

        question_title = tk.Label(
            self.main_frame,
            text = "Question 1",
            font = ("Arial", 25, "bold"),
            bg = "#87CEEB",
            fg = "black"
        )

        question_title.place(x = 0, y = 15, width = 900, height = 45)

        # This creates the large box around the quiz
        quiz_frame = tk.Frame(
            self.main_frame,
            relief = "solid",
            borderwidth = 1
        )

        quiz_frame.place(x = 55, y = 70, width = 790, height = 470)

        # This displays the difficulty
        difficulty_label = tk.Label(
            quiz_frame,
            text = "Difficulty: Easy",
            font = ("Arial", 15, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        difficulty_label.place(x = 15, y = 35, width = 210, height = 45)

        # This displays the logged-in username
        username_label = tk.Label(
            quiz_frame,
            text = "Username: " + self.current_username,
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        username_label.place(x = 15, y = 100, width = 210, height = 45)

        # This displays the five-minute timer
        self.timer_label = tk.Label(
            quiz_frame,
            text = "Time Remaining: 5:00",
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        self.timer_label.place(x = 15, y = 165, width = 210, height = 45)

        # This displays the user's score
        self.score_label = tk.Label(
            quiz_frame,
            text = "Score: 0",
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        self.score_label.place(x = 15, y = 230, width = 210, height = 45)

        # This displays the formula for the question
        formula_label = tk.Label(
            quiz_frame,
            text = "Formula:\n1/2 x base x height",
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        formula_label.place(x = 15, y = 295, width = 210, height = 70)

        # This displays the question
        question_label = tk.Label(
            quiz_frame,
            text = "A triangle has a base of 13cm and a height of 10cm.\nWhat is the area of the triangle?",
            font = ("Arial", 20, "bold"),
            wraplength = 480,
            justify = "center"
        )

        question_label.place(x = 265, y = 100, width = 485, height = 120)

        answer_label = tk.Label(
            quiz_frame,
            text = "Type your answer:",
            font = ("Arial", 17, "bold")
        )

        answer_label.place(x = 275, y = 250, width = 210, height = 45)

        # This Entry box allows the user to type only the number
        self.answer_entry = tk.Entry(
            quiz_frame,
            font = ("Arial", 18),
            justify = "center",
            relief = "solid",
            borderwidth = 2
        )

        self.answer_entry.place(x = 490, y = 250, width = 150, height = 45)

        # This displays the unit beside the answer box
        unit_label = tk.Label(
            quiz_frame,
            text = "cm²",
            font = ("Arial", 18, "bold")
        )

        unit_label.place(x = 645, y = 250, width = 70, height = 45)

        # This button checks the user's answer
        self.submit_button = tk.Button(
            quiz_frame,
            text = "Submit Answer",
            font = ("Arial", 16, "bold"),
            relief = "solid",
            borderwidth = 2,
            command = self.check_typed_answer
        )

        self.submit_button.place(x = 390, y = 330, width = 220, height = 55)

        # This button exits the quiz
        exit_button = tk.Button(
            quiz_frame,
            text = "Exit",
            font = ("Arial", 17, "bold"),
            relief = "solid",
            borderwidth = 2,
            command = self.exit_quiz
        )

        exit_button.place(x = 620, y = 15, width = 150, height = 45)

        self.answer_entry.focus_set()

        # This starts the timer
        self.update_timer()


    # This function checks the number typed by the user
    def check_typed_answer(self):
        if self.question_answered == True:
            return

        typed_answer = self.answer_entry.get().strip()

        if typed_answer == "":
            messagebox.showerror("Error", "Please type an answer.")
            return

        # This makes sure the user only enters a whole number
        if typed_answer.isdigit() == False:
            messagebox.showerror(
                "Error",
                "Please enter only the number. Do not type the unit."
            )
            return

        self.question_answered = True
        self.quiz_active = False

        # The correct answer is 65
        if typed_answer == "65":
            self.score = self.score + 1
            self.score_label.config(text = "Score: " + str(self.score))

            messagebox.showinfo(
                "Correct",
                "Your answer is correct.\n\nYour score is now " +
                str(self.score) + "."
            )
        else:
            messagebox.showinfo(
                "Incorrect",
                "Your answer is incorrect.\n\nThe correct answer is 65cm²."
            )

        # This prevents the answer from being submitted again
        self.answer_entry.config(state = "disabled")
        self.submit_button.config(state = "disabled")

        # This stops the timer after the question is answered
        if self.timer_job != None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None


    # This function controls the five-minute countdown timer
    def update_timer(self):
        if self.quiz_active == False:
            return

        minutes = self.time_left // 60
        seconds = self.time_left % 60

        if seconds < 10:
            displayed_time = str(minutes) + ":0" + str(seconds)
        else:
            displayed_time = str(minutes) + ":" + str(seconds)

        self.timer_label.config(
            text = "Time Remaining: " + displayed_time
        )

        # This ends the question when the timer reaches zero
        if self.time_left == 0:
            self.quiz_active = False
            self.question_answered = True
            self.timer_job = None

            self.answer_entry.config(state = "disabled")
            self.submit_button.config(state = "disabled")

            messagebox.showinfo(
                "Time Finished",
                "The five-minute timer has ended.\n\nYour score is " +
                str(self.score) + "."
            )
        else:
            self.time_left = self.time_left - 1

            self.timer_job = self.root.after(
                1000,
                self.update_timer
            )


    # This function exits the quiz and returns to difficulty selection
    def exit_quiz(self):
        self.quiz_active = False

        if self.timer_job != None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.difficulty_selection()

    # This function opens the leaderboard for the user to see the rankings of all users who have participated
    def open_leaderboard(self):
        self.clear_screen()

        title_label = tk.Label(self.main_frame, text = "<Leaderboard>", font = title_font, bg = "#87CEEB", fg = text_colour, height = 50)

        title_label.place(x = 0, y = 40, width = window_width, height = 50)

        self.create_back_button()

    # This function destroys the GUI when the "Exit" button on the GUI is clicked
    def exit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# This creates the "Back" button allows for user to go back to the previous section
    def create_back_button(self):
        back_button = tk.Button(self.main_frame, text = "Back", font = ("Arial", 28, "bold"), bg= "#FF0000", fg=text_colour, activebackground = button_hover_colour, relief = "solid", borderwidth = 1, command = self.show_main_menu)

        back_button.place(x = 30, y = 520, width = 120, height = 45)

    # This section creates the back button for the log in section, allowing users to go back to the home page
    def login_back_button(self):
        login_back_button = tk.Button(self.main_frame, text = "Back", font = ("Arial", 28, "bold"), bg = "#FF0000", fg = text_colour, activebackground = button_hover_colour, relief = "solid", borderwidth = 1, command = self.open_log_in)

        login_back_button.place(x = 30, y = 520, width = 120, height = 45)

# This allows for the "Exit" button to close the program when clicked
    def exit_program(self):
        self.root.destroy()

# This is the main function which allows the program to run
if __name__ == "__main__":
    app = MathQuizApp()
    app.run()