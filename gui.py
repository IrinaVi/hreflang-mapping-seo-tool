from tkinter import *
from tkinter import filedialog

FONT_NAME = "Courier"
BLUE="#2596be"

window = Tk()
window.title("Hreflang mapping")
window.config(padx=200, pady=200, bg=BLUE)

#main_label = Label(text="Hreflang mapping", fg="black", bg=BLUE, font=(FONT_NAME, 20, "normal"))
#main_label.grid(column=0, row=0)

# ---------------------------- FILE UPLOAD FUNCTIONS ------------------------------- #

def open_file_1():
    window.filename = filedialog.askopenfilename(initialdir="/Users/timothyfisher/Desktop", title="Select A File", filetypes=(("csv files", "*.csv"),("all files","*.*")))
    return(window.filename)

def open_file_2():
    window.filename = filedialog.askopenfilename(initialdir="/Users/timothyfisher/Desktop", title="Select A File", filetypes=(("csv files", "*.csv"),("all files","*.*")))
    return(window.filename)

# ---------------------------- DOMAIN ENTRY FUNCTIONS ------------------------------- #

def get_domain_1():
    return domain_1.get()

def get_domain_2():
    return domain_2.get()

# ---------------------------- GUI ------------------------------- #

main_label = Label(text="Upload files and add the domain names below", fg="black", bg=BLUE, font=(FONT_NAME, 19, "normal"))
main_label.grid(row=0, columnspan=5)

# -------------------FIRST DOMAIN UPLOAD---------------------- #

upload_label = Label(text="CSV file 1", fg="black", bg=BLUE, font=(FONT_NAME, 16, "normal"))
upload_label.grid(column=0, row=1)

#TODO: add status to the upload
upload_button = Button(window, text='Upload CSV file', command=open_file_1)
upload_button.grid(column=1, row=1)

domain_1_label = Label(text="Enter domain name", fg="black", bg=BLUE, font=(FONT_NAME, 16, "normal"))
domain_1_label.grid(column=3, row=1)

domain_1 = Entry(window)
domain_1.grid(column=4, row=1)

add_domain_1_btn = Button(window, text="Add domain", command=get_domain_1)
add_domain_1_btn.grid(column=5, row=1)

# -------------------SECOND DOMAIN UPLOAD---------------------- #

upload_label = Label(text="CSV file 2", fg="black", bg=BLUE, font=(FONT_NAME, 16, "normal"))
upload_label.grid(column=0, row=2)

upload_button = Button(window, text='Upload CSV file', command=open_file_2)
upload_button.grid(column=1, row=2)

domain_2_label = Label(text="Enter domain name", fg="black", bg=BLUE, font=(FONT_NAME, 16, "normal"))
domain_2_label.grid(column=3, row=2)

domain_2 = Entry(window)
domain_2.grid(column=4, row=2)

add_domain_2_btn = Button(window, text="Add domain", command=get_domain_1)
add_domain_2_btn.grid(column=5, row=2)

window.mainloop()
