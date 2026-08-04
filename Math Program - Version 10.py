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
from tkinter import PhotoImage

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
        self.current_username=""
        self.timer_job = None
        self.lives=3
        self.main()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_menu_button(self, text, y_position, command):
        button = tk.Button(self.main_frame, text = text, font = ("Georgia", 25, "bold") , bg = button_colour, fg = text_colour, activebackground = button_hover_colour, activeforeground = text_colour, relief = "solid", borderwidth = 1, command = command)

        button.place(x = button_x, y = y_position, width = button_width, height = button_height)
        return button

# This is the displays the title of the GUI
    def main(self):
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
        self.main()

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

        note_label = tk.Label(self.main_frame, text = "Note: Use special symbols where neccessary", font = title_font, bg = "#87CEEB", fg = text_colour, height = 50)

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
        self.lives=3
        self.question_number = 0
        self.time_left = 300
        self.quiz_active = True
        self.waiting_for_next = False
        self.timer_job = None
        self.next_question_job = None

        # These are the questions for the Easy quiz
        self.easy_questions = [
            {"question": "\nWhat is the area of the rectangle?", "answer": "45", "unit": "cm²", "image": "images/easy2.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "5/7", "unit": "", "image": "images/easy1.png"},
            {"question": "\nWhat is the area of the triangle?", "answer": "25", "unit": "cm", "image": "images/easy3.png"},
            {"question": "\nWhat is the area of the triangle?", "answer": "36", "unit": "cm", "image": "images/easy4.png"},
            {"question": "\nWhat is the missing angle x?", "answer": "125", "unit": "", "image": "images/easy5.png"},
            {"question": "\nWhat is the area of the rectangle?", "answer": "36", "unit": "cm", "image": "images/easy6.png"},
            {"question": "\nWhat is the area of the rectangle?", "answer": "21", "unit": "cm", "image": "images/easy7.png"},
            {"question": "\nWork out the answer to this question", "answer": "3/10", "unit": "", "image": "images/easy8.png"},
            {"question": "\nWhat is the missing angle w?", "answer": "59", "unit": "", "image": "images/easy9.png"},
            {"question": "\nWhat is the missing number?", "answer": "12", "unit": "", "image": "images/easy10.png"},
            {"question": "\nWhat is the area of the rectangle?", "answer": "36", "unit": "cm²", "image": "images/easy11.png"},
            {"question": "\nWhat is area of the rectangle?", "answer": "18", "unit": "cm²", "image": "images/easy12.png"},
            {"question": "\nWhat is the area of the triangle?", "answer": "14", "unit": "cm²", "image": "images/easy13.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "77", "unit": "", "image": "images/easy14.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "56", "unit": "", "image": "images/easy15.png"},
            {"question": "\nWhat is the area of the rectangle?", "answer": "56", "unit": "cm²", "image": "images/easy16.png"},
            {"question": "\nWhat is the area of the rectangle?", "answer": "48", "unit": "cm²", "image": "images/easy17.png"},
            {"question": "\nWork out the answer to this question", "answer": "4.6", "unit": "", "image": "images/easy18.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "1.7", "unit": "", "image": "images/easy19.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "3/5", "unit": "", "image": "images/easy20.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "2/9", "unit": "", "image": "images/easy21.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "8/11", "unit": "", "image": "images/easy22.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "1/10", "unit": "", "image": "images/easy23.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "3/8", "unit": "", "image": "images/easy24.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "3/20", "unit": "", "image": "images/easy25.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "27", "unit": "", "image": "images/easy26.png"},
            {"question": "\nWhat is the answer to this question?", "answer": "56", "unit": "", "image": "images/easy27.png"},
            {"question": "\nHow many lines of symmetry does this shape have?", "answer": "1", "unit": "", "image": "images/easy28.png"},
            {"question": "\nHow many lines of symmetry does this shape have?", "answer": "2", "unit": "", "image": "images/easy29.png"},
            {"question": "\nWhat is the missing number?", "answer": "4", "unit": "", "image": "images/easy30.png"},
            ]

        self.medium_questions =  [
    {"question": "\nSolve 3x + 7 = 25.", "answer": "6", "unit": "", "image": "images/medium1.png"
     },
    {"question": "\nSolve 4(x - 2) = 28.", "answer": "9", "unit": "", "image": "images/medium2.png"
     },
    {"question": "\nWhen a = 5 and b = 2, work out 3a² - 4b.", "answer": "67", "unit": "", "image": "images/medium3.png"
    },
    {"question": "\nThe nth term of a sequence is 4n - 1. Work out the 8th term.", "answer": "31", "unit": "", "image": "images/medium4.png"
    },
    {"question": "\nSolve 2x + 9 = 5x - 6.", "answer": "5", "unit": "", "image": "images/medium5.png"
    },
    {"question": "\nEvaluate 2⁴ x 2².", "answer": "64", "unit": "", "image": "images/medium6.png"
    },
    {"question": "\nEvaluate 3³ - 2⁴.", "answer": "11", "unit": "", "image": "images/medium7.png"
    },
    {"question": "\nEvaluate (5² + 7) ÷ 4.", "answer": "8", "unit": "", "image": "images/medium8.png"
    },
    {"question": "\nEvaluate √225 + 2³.", "answer": "23", "unit": "", "image": "images/medium9.png"
    },
    {"question": "\nUse BIDMAS to work out 24 ÷ (3 + 1) + 5 x 2.", "answer": "16", "unit": "", "image": "images/medium10.png"
    },
    {"question": "\nUse BIDMAS to work out 7 + 3² x 2.", "answer": "25", "unit": "", "image": "images/medium11.png"
    },
    {"question": "\nUse BIDMAS to work out 50 - [6 + 2 x 5].", "answer": "34", "unit": "", "image": "images/medium12.png"
    },
    {"question": "\nThe angles in a triangle are 2x°, (x + 20)° and 70°. Find x.", "answer": "30", "unit": "", "image": "images/medium13.png"
    },
    {"question": "\nThe lines are parallel. Find x.", "answer": "68", "unit": "", "image": "images/medium14.png"
    },
    {"question": "\nFind one interior angle of a regular hexagon.", "answer": "120", "unit": "", "image": "images/medium15.png"
    },
    {"question": "\nA right-angled triangle has shorter sides of 9 cm and 12 cm. Find x.", "answer": "15", "unit": "cm", "image": "images/medium16.png"
    },
    {"question": "\nWork out the area of this trapezium.", "answer": "78", "unit": "cm²", "image": "images/medium17.png"
    },
    {"question": "\nWork out the area of this circle using π = 22/7.", "answer": "154", "unit": "cm²", "image": "images/medium18.png"
    },
    {"question": "\nWork out the volume of this triangular prism.", "answer": "120", "unit": "cm³", "image": "images/medium19.png"
    },
    {"question": "\nWork out the area of this L-shaped polygon.", "answer": "68", "unit": "cm²", "image": "images/medium20.png"
    },
    {"question": "\nWork out the mean of 7, 8, 10, 11 and 14.", "answer": "10", "unit": "", "image": "images/medium21.png"
    },
    {"question": "\nWork out the median of 3, 8, 12, 15, 19 and 23.", "answer": "13.5", "unit": "", "image": "images/medium22.png"
    },
    {"question": "\nUse the table to find the range.", "answer": "6", "unit": "", "image": "images/medium23.png"
    },
    {"question": "\nUse the table to find the mean.", "answer": "3", "unit": "", "image": "images/medium24.png"
    },
    {"question": "\nA bag contains 4 red, 3 blue and 5 green counters. What is the probability of not choosing green?", "answer": "7/12", "unit": "", "image": "images/medium25.png"
    },
    {"question": "\nA spinner has 8 equal sections. What is the probability of not landing on yellow?", "answer": "5/8", "unit": "", "image": "images/medium26.png"
    },
    {"question": "\nFind the highest common factor (HCF) of 42 and 70.", "answer": "14", "unit": "", "image": "images/medium27.png"
    },
    {"question": "\nFind the lowest common multiple (LCM) of 12 and 18.", "answer": "36", "unit": "", "image": "images/medium28.png"
    },
    {"question": "\nHow many positive factors does 36 have?", "answer": "9", "unit": "", "image": "images/medium29.png"
    },
    {"question": "\nWhat is the smallest number greater than 50 that is a multiple of both 6 and 8?", "answer": "72", "unit": "", "image": "images/medium30.png"
    },
]

        self.hard_questions =  [
    {"question": "\nSolve 5x - 7 = 3x + 15.", "answer": "11", "unit": "", "image": "images/hard1.png"
    },
    {"question": "\nSolve 3(2x - 5) = 4x + 9.", "answer": "12", "unit": "", "image": "images/hard2.png"
    },
    {"question": "\nSolve the simultaneous equations and give the value of x: x + y = 17 and x - y = 5.", "answer": "11", "unit": "", "image": "images/hard3.png"
    },
    {"question": "\nThe equation x² - 7x + 12 = 0 has two solutions. Give the larger solution.", "answer": "4", "unit": "", "image": "images/hard4.png"
    },
    {"question": "\nWork out (x + 4)(x + 2) when x = 3.", "answer": "35", "unit": "", "image": "images/hard5.png"
    },
    {"question": "\nThe nth term of a sequence is 5n - 2. Work out the 12th term.", "answer": "58", "unit": "", "image": "images/hard6.png"
    },
    {"question": "\nUse the laws of indices to evaluate 3⁴ x 3² ÷ 3³.", "answer": "27", "unit": "", "image": "images/hard7.png"
    },
    {"question": "\nEvaluate (2³)² ÷ 2³.", "answer": "8", "unit": "", "image": "images/hard8.png"
    },
    {"question": "\nUse BIDMAS to work out 4³ - 3² x 2.", "answer": "46", "unit": "", "image": "images/hard9.png"
    },
    {"question": "\nUse BIDMAS to work out 72 ÷ [3(4 + 2)] + 2³.", "answer": "12", "unit": "", "image": "images/hard10.png"
    },
    {"question": "\nUse BIDMAS to work out 5 + {18 ÷ [3² - 3]} x 4.", "answer": "17", "unit": "", "image": "images/hard11.png"
    },
    {"question": "\nEvaluate (3.6 x 10⁵) ÷ (1.2 x 10²). Give an ordinary number.", "answer": "3000", "unit": "", "image": "images/hard12.png"
    },
    {"question": "\nThe angles in a triangle are (x + 15)°, (2x + 5)° and (3x - 20)°. Find x.", "answer": "30", "unit": "", "image": "images/hard13.png"
    },
    {"question": "\nThe lines are parallel. The two marked co-interior angles are shown. Find x.", "answer": "30", "unit": "", "image": "images/hard14.png"
    },
    {"question": "\nA regular polygon has an exterior angle of 24°. How many sides does it have?", "answer": "15", "unit": "", "image": "images/hard15.png"
    },
    {"question": "\nA right-angled triangle has shorter sides of 7 cm and 24 cm. Find x.", "answer": "25", "unit": "cm", "image": "images/hard16.png"
    },
    {"question": "\nWork out the area of this sector using π = 22/7.", "answer": "462", "unit": "cm²", "image": "images/hard17.png"
    },
    {"question": "\nWork out the circumference of this circle using π = 22/7.", "answer": "44", "unit": "cm", "image": "images/hard18.png"
    },
    {"question": "\nWork out the total area of the rectangle and semicircle.", "answer": "189", "unit": "cm²", "image": "images/hard19.png"
    },
    {"question": "\nWork out the volume of this cylinder using π = 22/7.", "answer": "1540", "unit": "cm³", "image": "images/hard20.png"
    },
    {"question": "\nWork out the surface area of this cuboid.", "answer": "158", "unit": "cm²", "image": "images/hard21.png"
    },
    {"question": "\nUse the frequency table to find the mean.", "answer": "11.5", "unit": "", "image": "images/hard22.png"
    },
    {"question": "\nUse the grouped table to calculate the estimated mean.", "answer": "16", "unit": "", "image": "images/hard23.png"
    },
    {"question": "\nUse the ordered data to find the interquartile range.", "answer": "11", "unit": "", "image": "images/hard24.png"
    },
    {"question": "\nA bag contains 3 red and 2 blue counters. Two counters are taken without replacement. What is the probability that both are red?", "answer": "3/10", "unit": "", "image": "images/hard25.png"
    },
    {"question": "\nUse the two-way table to find the probability that a randomly chosen student is a girl who passed.", "answer": "21/50", "unit": "", "image": "images/hard26.png"
    },
    {"question": "\nFind the highest common factor (HCF) of 84 and 126.", "answer": "42", "unit": "", "image": "images/hard27.png"
    },
    {"question": "\nFind the lowest common multiple (LCM) of 18 and 30.", "answer": "90", "unit": "", "image": "images/hard28.png"
    },
    {"question": "\nWhat is the smallest number that must be added to 347 to make a multiple of 9?", "answer": "4", "unit": "", "image": "images/hard29.png"
    },
    {"question": "\nWhat is the smallest whole number that must multiply 180 to make a perfect square?", "answer": "5", "unit": "", "image": "images/hard30.png"
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
        self.question_title = tk.Label(self.main_frame , text = "Question 1" , font = ("Arial" , 25 , "bold") , bg = "#87CEEB" , fg = "black")

        self.question_title.place(x = 0 , y = 15 , width = 900 , height = 45)

        # This creates the large box around the quiz
        quiz_frame = tk.Frame(self.main_frame , relief = "solid" , borderwidth = 1)

        quiz_frame.place(x = 55 , y = 70 , width = 790 , height = 470)

        # This displays the difficulty
        difficulty_label = tk.Label(quiz_frame , text = "Difficulty: " + difficulty , font = ("Arial" , 15 , "bold") , relief = "solid" , borderwidth = 1)

        difficulty_label.place(x = 15 , y = 35 , width = 210 , height = 45)

        # This displays the logged-in username
        username_label = tk.Label(quiz_frame , text = "Username: " + self.current_username , font = ("Arial" , 14 , "bold") , relief = "solid" , borderwidth = 1)

        username_label.place(x = 15 , y = 100 , width = 210 , height = 45)

        # This displays the five-minute timer
        self.timer_label = tk.Label(quiz_frame , text = "Time Remaining: 5:00" , font = ("Arial", 14, "bold") , relief = "solid" , borderwidth = 1)

        self.timer_label.place(x = 15 , y = 165 , width = 210 , height = 45)

        # This displays the score
        self.score_label = tk.Label(quiz_frame , text = "Score: 0" , font = ("Arial" , 14 , "bold") , relief = "solid" , borderwidth = 1)

        self.score_label.place(x = 15 , y = 230 , width = 210 , height = 45)

        # This creates the lives box
        lives_box=tk.Frame(quiz_frame , relief = "solid" , borderwidth = 1)

        lives_box.place(x = 15, y = 295 , width = 210 , height = 75)

        lives_label=tk.Label(lives_box , text = "Lives:" , font = ("Arial" , 14 , "bold"))

        lives_label.place(x = 5 , y = 20 , width = 60 , height = 35)

        # This loads the heart image
        heart_picture = Image.open("images/heart.png")
        heart_picture = heart_picture.resize((40 , 40))
        self.heart_image = ImageTk.PhotoImage(heart_picture)

        # First heart
        self.heart_one = tk.Label(lives_box , image = self.heart_image)

        self.heart_one.place(x = 70 , y = 17 , width = 40 , height = 40)

        # Second heart
        self.heart_two = tk.Label(lives_box , image = self.heart_image)

        self.heart_two.place(x = 115 , y = 17 , width = 40 , height = 40)

        # Third heart
        self.heart_three = tk.Label(lives_box , image = self.heart_image)

        self.heart_three.place(x = 160 , y = 17 , width = 40 , height = 40)

        # This displays the question
        self.question_label = tk.Label(quiz_frame , text = "", font = ("Arial" , 17 , "bold") , wraplength = 480 , justify = "center")

        self.question_label.place(x = 265 , y = 60 , width = 485 , height = 70)

        # This label displays the image
        self.question_image_label = tk.Label(quiz_frame , bg = "white" , relief = "solid" , borderwidth = 1)

        self.question_image_label.place(x = 380 , y = 135 , width = 250 , height = 130)

        # This tells the user where to type
        self.answer_label = tk.Label(quiz_frame , text = "Type your answer:" , font = ("Arial" , 17 , "bold"))

        self.answer_label.place(x = 275 , y = 285 , width = 210 , height = 45)

        # The user types only the number in this box
        self.answer_entry = tk.Entry(quiz_frame, font = ("Arial" , 18) , justify = "center" , relief = "solid" , borderwidth = 2)

        self.answer_entry.place(x = 490 , y = 285 , width = 150 , height = 45)

        # This displays the unit beside the answer box
        self.unit_label = tk.Label(quiz_frame , text = "" , font = ("Arial" , 18 , "bold") , anchor = "w")

        self.unit_label.place(x = 650 , y = 285 , width = 80 , height = 45)

        # This displays Correct, Wrong or an input error
        self.feedback_label = tk.Label(quiz_frame , text = "" , font = ("Arial" , 15 , "bold"))

        self.feedback_label.place(x = 300 , y = 330 , width = 420 , height = 35)

        # This button submits the answer
        self.submit_button = tk.Button(quiz_frame , text = "Submit Answer" , font = ("Arial" , 16 , "bold") , relief = "solid" , borderwidth = 2)

        self.submit_button.place(x = 390 , y = 380 , width = 220 , height = 55)

        # This button exits the quiz
        exit_button = tk.Button(quiz_frame , text = "Exit" , font = ("Arial" , 17 , "bold") , relief = "solid" , borderwidth = 2)

        exit_button.place(x = 620 , y = 15 , width = 150 , height = 45)

        # This function displays the current question
        def show_question():
            if self.quiz_active == False:
                return

            self.waiting_for_next = False

            current_question = self.questions[self.question_number]

            self.question_title.config(text = "Question " + str(self.question_number + 1) + " of " + str(len(self.questions)))

            self.question_label.config(text = current_question["question"])

            self.unit_label.config(text = current_question["unit"])

            # This loads and resizes the image for the question
            try:
                question_image = Image.open(current_question["image"])

                question_image = question_image.resize((250 , 130))

                self.current_question_image = ImageTk.PhotoImage(question_image)

                self.question_image_label.config(image = self.current_question_image , text = "")

            except (FileNotFoundError , OSError):self.question_image_label.config (image = "" , text = "Image not found" , font = ("Arial" , 14 , "bold"))

            self.answer_entry.config(state = "normal")
            self.answer_entry.delete(0, tk.END)

            self.feedback_label.config(text = "")
            self.submit_button.config(state = "normal")

            self.answer_entry.focus_set()

        # This displays the final result on the same page
        def finish_quiz(title_text):
            self.quiz_active = False

            if self.timer_job!= None:
                self.root.after_cancel(self.timer_job)
                self.timer_job = None

            if self.next_question_job!= None:
                self.root.after_cancel(self.next_question_job)
                self.next_question_job = None

            if self.result_saved == False:
                self.save_leaderboard_result()
                self.result_saved = True

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

            self.question_title.config(text= title_text)

            self.question_label.config(text = "Final score: " + str(self.score) + " out of " + str(len(self.questions)))

            self.question_image_label.config(image = "" , text = "")

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
                self.feedback_label.config(text = "Please enter an answer.")
                return

            current_question = self.questions[self.question_number]
            correct_answer = current_question["answer"]

            self.waiting_for_next = True

                        # This checks whether the answer is correct
            if typed_answer == correct_answer:
                self.score = self.score+1

                self.score_label.config(text = "Score: " + str(self.score))

                self.feedback_label.config(text = "Correct")

            else:
                self.feedback_label.config(text = "Wrong")

                self.lives=self.lives-1

                # This removes one heart
                if self.lives == 2:
                    self.heart_three.place_forget()

                elif self.lives == 1:
                    self.heart_two.place_forget()

                elif self.lives == 0:
                    self.heart_one.place_forget()

            # This prevents the answer being submitted twice
            self.answer_entry.config(state = "disabled")
            self.submit_button.config(state = "disabled")

            # The quiz ends when the user loses all three lives
            if self.lives == 0:
                self.next_question_job=self.root.after(1000 , lambda:finish_quiz ("Lives Finished"))

            else:
                self.next_question_job=self.root.after(1000 , move_to_next_question)

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

            self.timer_label.config(text = "Time Remaining: " + displayed_time)

            if self.time_left == 0:
                finish_quiz("Time Finished")
            else:
                self.time_left = self.time_left - 1

                self.timer_job = self.root.after(1000 , update_timer)

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
        self.submit_button.config(command = check_answer)

        exit_button.config(command = exit_quiz)

        # Pressing Enter also submits the answer
        self.answer_entry.bind("<Return>" , lambda event: check_answer())

        # This displays the first question and begins the timer
        show_question()
        update_timer()

    # This saves a completed quiz result
    def save_leaderboard_result(self):
        total_questions = len(self.questions)

        # This calculates how long the user took
        time_used = 300 - self.time_left

        file = open("Leaderboard.txt" , "a")

        file.write(self.current_difficulty + "," +
self.current_username + "," + str(self.score) + "," + str(total_questions) + "," + str(time_used) + "\n")
        file.close()

    # This displays the results for the selected difficulty
    def display_leaderboard(self, event = None):

        # This removes the previously displayed results
        for row in self.leaderboard_table.get_children():
            self.leaderboard_table.delete(row)

        selected_difficulty = self.leaderboard_difficulty_box.get()

        try:
            file = open("Leaderboard.txt" , "r")
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
                        best_results[username] = [score , total_questions , time_used]

                    else:
                        old_score = best_results[username][0]
                        old_time = best_results[username][2]

                        # A higher score is better
                        if score > old_score:
                            best_results[username] = [score , total_questions , time_used]

                        # A faster time is better when scores are equal
                        elif score == old_score and time_used < old_time:
                            best_results[username] = [score , total_questions , time_used]
        leaderboard_results = []

        for username in best_results:
            score = best_results[username][0]
            total_questions = best_results[username][1]
            time_used = best_results[username][2]

            leaderboard_results.append([username , score , total_questions , time_used])

        # Highest scores appear first
        # Faster times appear first when the scores are equal
        leaderboard_results.sort(key = lambda result: (-result[1] , result[3]))

        if len(leaderboard_results) == 0:
            self.leaderboard_table.insert("" , "end" , values = ("No results yet" , "-" , "-"))
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

            displayed_score = (str(score) + "/" + str(total_questions))

            self.leaderboard_table.insert("" , "end" , values = (username , displayed_score , displayed_time))

        # This displays the user's final result
    def show_results_page(self):
        self.clear_screen()

        total_questions = len(self.questions)
        time_used = 300-self.time_left
        minutes = time_used//60
        seconds = time_used%60

        if seconds<10:
            displayed_time = str(minutes) + ":0"+str(seconds)
        else:
            displayed_time = str(minutes) + ":"+str(seconds)

        if self.lives == 0:
            result_message = "You Lose!"

        elif self.score>= total_questions/2:
            result_message = "You Win!"

        else:
            result_message = "You Lose!"

        title_label = tk.Label(self.main_frame , text = "Results Page: " + result_message , font = ("Arial" , 27 , "bold") , bg= "#87CEEB" , fg="black")
        title_label.place(x = 0 , y = 45 , width = 900 , height = 50)

        difficulty_label = tk.Label(self.main_frame , text = "This is your Final Score on " + self.current_difficulty + " Difficulty:" , font = ("Arial" , 22) , bg = "#87CEEB" , fg = "black")
        difficulty_label.place(x = 0 , y = 115 , width = 900 , height = 55)

        username_heading = tk.Label(self.main_frame , text = "Username" , font = ("Arial" , 18 , "bold") , bg = "white" , relief = "solid" , borderwidth = 1)
        username_heading.place(x = 98 , y = 220 , width = 263 , height = 75)

        score_heading = tk.Label(self.main_frame , text = "Score" , font = ("Arial" , 18 , "bold") , bg = "white" , relief = "solid" , borderwidth = 1)
        score_heading.place(x = 361 , y = 220 , width = 165 , height = 75)

        time_heading = tk.Label(self.main_frame, text = "Time" , font = ("Arial" , 18 , "bold") , bg = "white" , relief = "solid" , borderwidth = 1)
        time_heading.place(x = 526 , y = 220 , width = 278 , height = 75)

        username_result = tk.Label(self.main_frame , text = self.current_username , font = ("Arial" , 18) , bg = "white" , relief = "solid" , borderwidth = 1)
        username_result.place(x = 98 , y = 295 , width = 263 , height = 75)

        score_result = tk.Label(self.main_frame , text = str(self.score) + "/" + str(total_questions) , font = ("Arial" , 18) , bg = "white" , relief = "solid" , borderwidth = 1)
        score_result.place(x = 361 , y = 295 , width = 165 , height = 75)

        time_result = tk.Label(self.main_frame , text = displayed_time , font = ("Arial" , 18) , bg = "white" , relief = "solid" , borderwidth = 1)
        time_result.place(x = 526 , y = 295 , width = 278 , height = 75)

        main_menu_button = tk.Button(self.main_frame , text = "Main Menu" , font = ("Arial" , 18 , "bold") , bg = button_colour , fg = "black" , relief = "solid" , borderwidth = 1 , command = self.main)
        main_menu_button.place(x = 350 , y = 460 , width = 203 , height = 50)

        # This opens the leaderboard page
    def open_leaderboard(self):
        self.clear_screen()

        # This displays the leaderboard title
        title_label = tk.Label(self.main_frame , text = "Leaderboard of All Users" , font = ("Arial" , 28 , "bold") , bg = "#87CEEB" , fg = "black")

        title_label.place(x = 0 , y = 15 , width = 900 , height = 45)

        # This displays the difficulty label
        difficulty_label = tk.Label(self.main_frame , text = "Difficulty:" , font = ("Arial" , 22 , "bold") , bg = "#87CEEB" , fg = "black")

        difficulty_label.place(x = 235 , y = 90 , width = 190 , height = 55)

        # This dropdown lets the user choose a leaderboard
        self.leaderboard_difficulty_box = ttk.Combobox(self.main_frame , values = ["Easy" , "Medium" , "Hard"] , state = "readonly" , font = ("Arial" , 18))

        self.leaderboard_difficulty_box.place(x = 425 , y = 95 , width = 270 , height = 45)

        # Easy is displayed first
        self.leaderboard_difficulty_box.set("Easy")

        # This changes the table when another difficulty is chosen
        self.leaderboard_difficulty_box.bind("<<ComboboxSelected>>" , self.display_leaderboard)

        # This changes how the leaderboard table looks
        leaderboard_style = ttk.Style()

        leaderboard_style.configure("Leaderboard.Treeview" , font = ("Arial" , 16) , rowheight = 50)

        leaderboard_style.configure("Leaderboard.Treeview.Heading" , font = ("Arial" , 16 , "bold"))

        # This creates the leaderboard table
        self.leaderboard_table = ttk.Treeview(self.main_frame , columns = ("Username" , "Score" , "Time") , show = "headings" , height = 7 , style = "Leaderboard.Treeview")

        self.leaderboard_table.heading("Username" , text = "Username")

        self.leaderboard_table.heading("Score" , text = "Score")

        self.leaderboard_table.heading("Time" , text = "Time")

        self.leaderboard_table.column("Username" , width = 260 , anchor = "center")

        self.leaderboard_table.column("Score" , width = 165 , anchor = "center")

        self.leaderboard_table.column("Time" , width = 275 , anchor = "center")

        self.leaderboard_table.place(x = 100 , y = 170 , width = 700 , height = 355)

        # This exits the leaderboard and returns to the menu
        exit_button = tk.Button(self.main_frame , text = "Exit" , font = ("Arial" , 18 , "bold") , bg = "#FF0000" , fg = "black" , relief = "solid" , borderwidth = 1 , command = self.main)

        exit_button.place(x = 700 , y = 5 , width = 200 , height = 45)

        # This loads the Easy results when the page opens
        self.display_leaderboard()

    # This function destroys the GUI when the "Exit" button on the GUI is clicked
    def exit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# This creates the "Back" button allows for user to go back to the previous section
    def create_back_button(self):
        back_button = tk.Button(self.main_frame, text = "Back", font = ("Arial", 28, "bold"), bg= "#FF0000", fg=text_colour, activebackground = button_hover_colour, relief = "solid", borderwidth = 1, command = self.main)

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