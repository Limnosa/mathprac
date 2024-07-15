import random
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from fpdf import FPDF
import os
import sys

def create():
    num1 = int(smallest_number_spinbox.get())
    num2 = int(largest_number_spinbox.get())
    num3 = int(numbers_spinbox.get())
    action = action_var.get()
    res = []

    if num2 > num1 and num3 != 0 and action is not None:
            for i in range(num3):
                x = random.randint(num1, num2)
                y = random.randint(num1, num2)
                if action == "add":
                    res.append(f"{x} + {y} =")
                elif action == "sub":
                    res.append(f"{x} - {y} =")
                elif action == "multi":
                    res.append(f"{x} x {y} =")
                elif action == "div":
                    res.append(f"{x} ÷ {y} =")

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=13)

            rows_per_page = 31
            cols_per_page = 3
            print_h = pdf.h - pdf.t_margin - pdf.b_margin
            print_w = pdf.w - pdf.l_margin - pdf.r_margin
            c_h = print_h / rows_per_page
            c_w = print_w / cols_per_page

            for j in range(rows_per_page):
                for k in range(cols_per_page):
                    index = j * cols_per_page + k
                    if index < len(res):
                        pdf.cell(c_w, c_h, res[index], border=1, ln=0, align="L")
                pdf.ln()

            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            pdf.output(file_path)
    else:
        tkinter.messagebox.showwarning(title="Error", message="Please enter valid values!")

window = tkinter.Tk()
window.title('Mathprac')
ico = Image.open(r'icon.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

window_width = 410
window_height = 360
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.minsize(window_width, window_height)
window.maxsize(1000, 900)

bg = PhotoImage(file=r'background.png')
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

title_frame = tkinter.Label(window, text="MATH WORKSHEET CREATOR", bg="white", font=("Helvetica", 20, "bold", "italic"))
title_frame.pack(pady=(10, 0))

frame = tkinter.Frame(window, bg="white")
frame.pack()

action_frame = tkinter.LabelFrame(frame, text="SET ACTION", bg="white", font=("Helvetica", 12, "bold"))
action_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

MODES = [
    ("Addition", "add"),
    ("Subtraction", "sub"),
    ("Multiplication", "multi"),
    ("Division", "div"),
]

action_var = StringVar()
action_var.set("add")

for idx, (text, mode) in enumerate(MODES):
    row = idx // 2
    column = idx % 2
    rb = Radiobutton(action_frame, text=text, variable=action_var, value=mode, bg="white")
    rb.grid(row=row, column=column, sticky="w", padx=10, pady=5)


parameters_frame = tkinter.LabelFrame(frame, text="SET PARAMETERS", bg="white", font=("Helvetica", 12, "bold"))
parameters_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

smallest_number_label = tkinter.Label(parameters_frame, text="Smallest number", bg="white")
smallest_number_label.grid(row=0, column=0)
largest_number_label = tkinter.Label(parameters_frame, text="Largest number", bg="white")
largest_number_label.grid(row=1, column=0)
numbers_label = tkinter.Label(parameters_frame, text="Number of operations", bg="white")
numbers_label.grid(row=2, column=0)

smallest_number_spinbox = tkinter.Spinbox(parameters_frame, from_=0, to="infinity")
largest_number_spinbox = tkinter.Spinbox(parameters_frame, from_=0, to="infinity")
numbers_spinbox = tkinter.Spinbox(parameters_frame, from_=0, to="infinity")
smallest_number_spinbox.grid(row=0, column=1)
largest_number_spinbox.grid(row=1, column=1)
numbers_spinbox.grid(row=2, column=1)

for widget in parameters_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = tkinter.Button(frame, text="Create", command=create)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()