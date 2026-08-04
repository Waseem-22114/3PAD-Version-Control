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
from PIL import Image, ImageTk
import os

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

        note_label = tk.Label(self.main_frame, text = "Note: Use special symbols were neccessary", font = title_font, bg = "#87CEEB", fg = text_colour, height = 50)

        note_label.place(x = 0, y = 120, width = window_width, height = 50)

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
            self.math_quiz("Easy")
        
        elif "Medium" in chosen_difficulty:
            self.math_quiz("Medium")

        elif "Hard" in chosen_difficulty:
            self.math_quiz("Hard")

            # This function displays the Easy math quiz
    def math_quiz(self, difficulty):
        self.clear_screen()

        self.current_difficulty = difficulty
        self.result_saved = False

        # These variables are reset when the quiz begins
        self.score = 0
        self.question_number = 0
        self.time_left = 300
        self.quiz_active = True
        self.waiting_for_next = False
        self.timer_job = None
        self.next_question_job = None

        # These are the questions for the Easy quiz
        self.easy_questions = [
            {
                "question": "\nWhat is the area of the rectangle?",
                "answer": "45",
                "unit": "cm²",
                "image": "rectangle1.png"
            },
            {
                "question": "\nWhat is the answer to this question?",
                "answer": "5/7",
                "unit": "",
                "image": "fraction1.png"
            },
            {
                "question": "\nWhat is the area of the triangle?",
                "answer": "25",
                "unit": "cm",
                "image": "triangle1.png"
            },
        ]

        self.medium_questions = [
            {
                "question": "\nSolve the equation and find the value of x.",
                "answer": "5",
                "unit": "",
                "image": "medium1.png"
            },
        ]

        self.hard_questions = [
            {
                "question": "\nSolve the equation and find the value of x.",
                "answer": "5",
                "unit": "",
                "image": "medium1.png"
            },
        ]


        # This selects the questions for the chosen difficulty
        if difficulty == "Easy":
            self.questions = self.easy_questions

        elif difficulty == "Medium":
            self.questions = self.medium_questions

        elif difficulty == "Hard":
            self.questions = self.hard_questions

        # This randomises the order without repeating questions
        random.shuffle(self.questions)

        # This displays the current question number
        self.question_title = tk.Label(
            self.main_frame,
            text = "Question 1",
            font = ("Arial", 25, "bold"),
            bg = "#87CEEB",
            fg = "black"
        )

        self.question_title.place(
            x = 0,
            y = 15,
            width = 900,
            height = 45
        )

        # This creates the large box around the quiz
        quiz_frame = tk.Frame(
            self.main_frame,
            relief = "solid",
            borderwidth = 1
        )

        quiz_frame.place(
            x = 55,
            y = 70,
            width = 790,
            height = 470
        )

        # This displays the difficulty
        difficulty_label = tk.Label(
            quiz_frame,
            text = "Difficulty: " + difficulty,
            font = ("Arial", 15, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        difficulty_label.place(
            x = 15,
            y = 35,
            width = 210,
            height = 45
        )

        # This displays the logged-in username
        username_label = tk.Label(
            quiz_frame,
            text = "Username: " + self.current_username,
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        username_label.place(
            x = 15,
            y = 100,
            width = 210,
            height = 45
        )

        # This displays the five-minute timer
        self.timer_label = tk.Label(
            quiz_frame,
            text = "Time Remaining: 5:00",
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        self.timer_label.place(
            x = 15,
            y = 165,
            width = 210,
            height = 45
        )

        # This displays the score
        self.score_label = tk.Label(
            quiz_frame,
            text = "Score: 0",
            font = ("Arial", 14, "bold"),
            relief = "solid",
            borderwidth = 1
        )

        self.score_label.place(
            x = 15,
            y = 230,
            width = 210,
            height = 45
        )

        # This displays the question
        self.question_label = tk.Label(
            quiz_frame,
            text = "",
            font = ("Arial", 17, "bold"),
            wraplength = 480,
            justify = "center"
        )

        self.question_label.place(
            x = 265,
            y = 60,
            width = 485,
            height = 70
        )

        # This label displays the image
        self.question_image_label = tk.Label(
            quiz_frame,
            bg = "white",
            relief = "solid",
            borderwidth = 1
        )

        self.question_image_label.place(
            x = 380,
            y = 135,
            width = 250,
            height = 130
        )

        # This tells the user where to type
        self.answer_label = tk.Label(
            quiz_frame,
            text = "Type your answer:",
            font = ("Arial", 17, "bold")
        )

        self.answer_label.place(
            x = 275,
            y = 285,
            width = 210,
            height = 45
        )

        # The user types only the number in this box
        self.answer_entry = tk.Entry(
            quiz_frame,
            font = ("Arial", 18),
            justify = "center",
            relief = "solid",
            borderwidth = 2
        )

        self.answer_entry.place(
            x = 490,
            y = 285,
            width = 150,
            height = 45
        )

        # This displays the unit beside the answer box
        self.unit_label = tk.Label(
            quiz_frame,
            text = "",
            font = ("Arial", 18, "bold"),
            anchor = "w"
        )

        self.unit_label.place(
            x = 650,
            y = 285,
            width = 80,
            height = 45
        )

        # This displays Correct, Wrong or an input error
        self.feedback_label = tk.Label(
            quiz_frame,
            text = "",
            font = ("Arial", 15, "bold")
        )

        self.feedback_label.place(
            x = 300,
            y = 330,
            width = 420,
            height = 35
        )

        # This button submits the answer
        self.submit_button = tk.Button(
            quiz_frame,
            text = "Submit Answer",
            font = ("Arial", 16, "bold"),
            relief = "solid",
            borderwidth = 2
        )

        self.submit_button.place(
            x = 390,
            y = 380,
            width = 220,
            height = 55
        )

        # This button exits the quiz
        exit_button = tk.Button(
            quiz_frame,
            text = "Exit",
            font = ("Arial", 17, "bold"),
            relief = "solid",
            borderwidth = 2
        )

        exit_button.place(
            x = 620,
            y = 15,
            width = 150,
            height = 45
        )

        # This function displays the current question
        def show_question():
            if self.quiz_active == False:
                return

            self.waiting_for_next = False

            current_question = self.questions[self.question_number]

            self.question_title.config(
                text = "Question " +
                str(self.question_number + 1) +
                " of " +
                str(len(self.questions))
            )

            self.question_label.config(
                text = current_question["question"]
            )

            self.unit_label.config(
                text = current_question["unit"]
            )

                      # This loads and resizes the image for the question
            try:
                question_image = Image.open(
                    current_question["image"]
                )

                question_image = question_image.resize(
                    (250, 130)
                )

                self.current_question_image = ImageTk.PhotoImage(
                    question_image
                )

                self.question_image_label.config(
                    image = self.current_question_image,
                    text = ""
                )

            except (FileNotFoundError, OSError):
                self.question_image_label.config(
                    image = "",
                    text = "Image not found",
                    font = ("Arial", 14, "bold")
                )

            self.answer_entry.config(state = "normal")
            self.answer_entry.delete(0, tk.END)

            self.feedback_label.config(text = "")
            self.submit_button.config(state = "normal")

            self.answer_entry.focus_set()

        # This displays the final result on the same page
        def finish_quiz(title_text):
            self.quiz_active = False

            if self.timer_job!=None:
                self.root.after_cancel(self.timer_job)
                self.timer_job=None

            if self.next_question_job!=None:
                self.root.after_cancel(self.next_question_job)
                self.next_question_job=None

            if self.result_saved==False:
                self.save_leaderboard_result()
                self.result_saved=True

            self.show_results_page()

            if self.result_saved == False:
                self.save_leaderboard_result()
                self.result_saved = True

            if self.timer_job != None:
                self.root.after_cancel(self.timer_job)
                self.timer_job = None

            if self.next_question_job != None:
                self.root.after_cancel(self.next_question_job)
                self.next_question_job = None

            self.question_title.config(
                text = title_text
            )

            self.question_label.config(
                text = "Final score: " +
                str(self.score) +
                " out of " +
                str(len(self.questions))
            )

            self.question_image_label.config(
                image = "",
                text = ""
            )

            self.answer_label.config(text = "")
            self.unit_label.config(text = "")
            self.feedback_label.config(text = "")

            self.answer_entry.delete(0, tk.END)
            self.answer_entry.config(state = "disabled")
            self.submit_button.config(state = "disabled")

        # This moves to the next question
        def move_to_next_question():
            self.next_question_job = None

            if self.quiz_active == False:
                return

            self.question_number = self.question_number + 1

            if self.question_number < len(self.questions):
                show_question()
            else:
                finish_quiz("Quiz Finished")

        # This checks the user's answer
        def check_answer():
            if self.quiz_active == False:
                return

            if self.waiting_for_next == True:
                return

            typed_answer = self.answer_entry.get().strip()

            # This checks that something was entered
            if typed_answer == "":
                self.feedback_label.config(
                    text = "Please enter an answer."
                )
                return

            current_question = self.questions[self.question_number]
            correct_answer = current_question["answer"]

            self.waiting_for_next = True

            # This checks whether the answer is correct
            if typed_answer == correct_answer:
                self.score = self.score + 1

                self.score_label.config(
                    text = "Score: " + str(self.score)
                )

                self.feedback_label.config(
                    text = "Correct"
                )
            else:
                self.feedback_label.config(
                    text = "Wrong"
                )

            # This prevents the answer being submitted twice
            self.answer_entry.config(state = "disabled")
            self.submit_button.config(state = "disabled")

            # This waits one second before showing the next question
            self.next_question_job = self.root.after(
                1000,
                move_to_next_question
            )

        # This controls the five-minute timer
        def update_timer():
            self.timer_job = None

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

            if self.time_left == 0:
                finish_quiz("Time Finished")
            else:
                self.time_left = self.time_left - 1

                self.timer_job = self.root.after(
                    1000,
                    update_timer
                )

        # This exits the quiz
        def exit_quiz():
            self.quiz_active = False

            if self.timer_job != None:
                self.root.after_cancel(self.timer_job)
                self.timer_job = None

            if self.next_question_job != None:
                self.root.after_cancel(self.next_question_job)
                self.next_question_job = None

            self.difficulty_selection()

        # These commands connect the buttons to the functions
        self.submit_button.config(
            command = check_answer
        )

        exit_button.config(
            command = exit_quiz
        )

        # Pressing Enter also submits the answer
        self.answer_entry.bind(
            "<Return>",
            lambda event: check_answer()
        )

        # This displays the first question and begins the timer
        show_question()
        update_timer()

    # This saves a completed quiz result
    def save_leaderboard_result(self):
        total_questions = len(self.questions)

        # This calculates how long the user took
        time_used = 300 - self.time_left

        file = open("Leaderboard.txt", "a")

        file.write(
            self.current_difficulty + "," +
            self.current_username + "," +
            str(self.score) + "," +
            str(total_questions) + "," +
            str(time_used) + "\n"
        )

        file.close()

    # This displays the results for the selected difficulty
    def display_leaderboard(self, event = None):
        # This removes the previously displayed results
        for row in self.leaderboard_table.get_children():
            self.leaderboard_table.delete(row)

        selected_difficulty = self.leaderboard_difficulty_box.get()

        try:
            file = open("Leaderboard.txt", "r")
            saved_results = file.readlines()
            file.close()

        except FileNotFoundError:
            saved_results = []

        # This stores the best result from each username
        best_results = {}

        for result in saved_results:
            result = result.strip()

            if result == "":
                continue

            details = result.split(",")

            if len(details) == 5:
                difficulty = details[0]
                username = details[1]

                try:
                    score = int(details[2])
                    total_questions = int(details[3])
                    time_used = int(details[4])

                except ValueError:
                    continue

                if difficulty == selected_difficulty:
                    # This adds the username if they have no result yet
                    if username not in best_results:
                        best_results[username] = [
                            score,
                            total_questions,
                            time_used
                        ]

                    else:
                        old_score = best_results[username][0]
                        old_time = best_results[username][2]

                        # A higher score is better
                        if score > old_score:
                            best_results[username] = [
                                score,
                                total_questions,
                                time_used
                            ]

                        # A faster time is better when scores are equal
                        elif score == old_score and time_used < old_time:
                            best_results[username] = [
                                score,
                                total_questions,
                                time_used
                            ]

        leaderboard_results = []

        for username in best_results:
            score = best_results[username][0]
            total_questions = best_results[username][1]
            time_used = best_results[username][2]

            leaderboard_results.append([
                username,
                score,
                total_questions,
                time_used
            ])

        # Highest scores appear first
        # Faster times appear first when the scores are equal
        leaderboard_results.sort(
            key = lambda result: (-result[1], result[3])
        )

        if len(leaderboard_results) == 0:
            self.leaderboard_table.insert(
                "",
                "end",
                values = ("No results yet", "-", "-")
            )
            return

        for result in leaderboard_results:
            username = result[0]
            score = result[1]
            total_questions = result[2]
            time_used = result[3]

            minutes = time_used // 60
            seconds = time_used % 60

            if seconds < 10:
                displayed_time = str(minutes) + ":0" + str(seconds)
            else:
                displayed_time = str(minutes) + ":" + str(seconds)

            displayed_score = (
                str(score) + "/" + str(total_questions)
            )

            self.leaderboard_table.insert(
                "",
                "end",
                values = (
                    username,
                    displayed_score,
                    displayed_time
                )
            )

        # This displays the user's final result
    def show_results_page(self):
        self.clear_screen()

        total_questions=len(self.questions)
        time_used=300-self.time_left
        minutes=time_used//60
        seconds=time_used%60

        if seconds<10:
            displayed_time=str(minutes)+":0"+str(seconds)
        else:
            displayed_time=str(minutes)+":"+str(seconds)

        if self.score>=total_questions/2:
            result_message="You Win!"
        else:
            result_message="You Lose!"

        title_label=tk.Label(
            self.main_frame,
            text="Results Page: "+result_message,
            font=("Arial",27,"bold"),
            bg="#87CEEB",
            fg="black"
        )
        title_label.place(x=0,y=45,width=900,height=50)

        difficulty_label=tk.Label(
            self.main_frame,
            text="This is your Final Score on "+self.current_difficulty+" Difficulty:",
            font=("Arial",22),
            bg="#87CEEB",
            fg="black"
        )
        difficulty_label.place(x=0,y=115,width=900,height=55)

        username_heading=tk.Label(
            self.main_frame,
            text="Username",
            font=("Arial",18,"bold"),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        username_heading.place(x=98,y=220,width=263,height=75)

        score_heading=tk.Label(
            self.main_frame,
            text="Score",
            font=("Arial",18,"bold"),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        score_heading.place(x=361,y=220,width=165,height=75)

        time_heading=tk.Label(
            self.main_frame,
            text="Time",
            font=("Arial",18,"bold"),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        time_heading.place(x=526,y=220,width=278,height=75)

        username_result=tk.Label(
            self.main_frame,
            text=self.current_username,
            font=("Arial",18),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        username_result.place(x=98,y=295,width=263,height=75)

        score_result=tk.Label(
            self.main_frame,
            text=str(self.score)+"/"+str(total_questions),
            font=("Arial",18),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        score_result.place(x=361,y=295,width=165,height=75)

        time_result=tk.Label(
            self.main_frame,
            text=displayed_time,
            font=("Arial",18),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        time_result.place(x=526,y=295,width=278,height=75)

        main_menu_button=tk.Button(
            self.main_frame,
            text="Main Menu",
            font=("Arial",18,"bold"),
            bg=button_colour,
            fg="black",
            relief="solid",
            borderwidth=1,
            command=self.show_main_menu
        )
        main_menu_button.place(x=350,y=460,width=203,height=50)

        # This opens the leaderboard page
    def open_leaderboard(self):
        self.clear_screen()

        # This displays the leaderboard title
        title_label = tk.Label(
            self.main_frame,
            text = "Leaderboard of All Users",
            font = ("Arial", 28, "bold"),
            bg = "#87CEEB",
            fg = "black"
        )

        title_label.place(
            x = 0,
            y = 15,
            width = 900,
            height = 45
        )

        # This displays the difficulty label
        difficulty_label = tk.Label(
            self.main_frame,
            text = "Difficulty:",
            font = ("Arial", 22, "bold"),
            bg = "#87CEEB",
            fg = "black"
        )

        difficulty_label.place(
            x = 235,
            y = 90,
            width = 190,
            height = 55
        )

        # This dropdown lets the user choose a leaderboard
        self.leaderboard_difficulty_box = ttk.Combobox(
            self.main_frame,
            values = ["Easy", "Medium", "Hard"],
            state = "readonly",
            font = ("Arial", 18)
        )

        self.leaderboard_difficulty_box.place(
            x = 425,
            y = 95,
            width = 270,
            height = 45
        )

        # Easy is displayed first
        self.leaderboard_difficulty_box.set("Easy")

        # This changes the table when another difficulty is chosen
        self.leaderboard_difficulty_box.bind(
            "<<ComboboxSelected>>",
            self.display_leaderboard
        )

        # This changes how the leaderboard table looks
        leaderboard_style = ttk.Style()

        leaderboard_style.configure(
            "Leaderboard.Treeview",
            font = ("Arial", 16),
            rowheight = 50
        )

        leaderboard_style.configure(
            "Leaderboard.Treeview.Heading",
            font = ("Arial", 16, "bold")
        )

        # This creates the leaderboard table
        self.leaderboard_table = ttk.Treeview(
            self.main_frame,
            columns = ("Username", "Score", "Time"),
            show = "headings",
            height = 7,
            style = "Leaderboard.Treeview"
        )

        self.leaderboard_table.heading(
            "Username",
            text = "Username"
        )

        self.leaderboard_table.heading(
            "Score",
            text = "Score"
        )

        self.leaderboard_table.heading(
            "Time",
            text = "Time"
        )

        self.leaderboard_table.column(
            "Username",
            width = 260,
            anchor = "center"
        )

        self.leaderboard_table.column(
            "Score",
            width = 165,
            anchor = "center"
        )

        self.leaderboard_table.column(
            "Time",
            width = 275,
            anchor = "center"
        )

        self.leaderboard_table.place(
            x = 100,
            y = 170,
            width = 700,
            height = 355
        )

        # This exits the leaderboard and returns to the menu
        exit_button = tk.Button(
            self.main_frame,
            text = "Exit",
            font = ("Arial", 18, "bold"),
            bg = "#FF0000",
            fg = "black",
            relief = "solid",
            borderwidth = 1,
            command = self.show_main_menu
        )

        exit_button.place(
            x = 700,
            y = 5,
            width = 200,
            height = 45
        )

        # This loads the Easy results when the page opens
        self.display_leaderboard()

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