import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

form = tk.Tk()
form.title("Anonymisation form")

filename = ""


def uploadandread():
    global filename
    filename = form.filename = filedialog.askopenfilename(initialdir="/", title="Open File",
                                                          filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    print(filename)
    with open(filename) as File:
        reader = csv.reader(File)
        for row in reader:
            global csvcontents
            csvcontents = row
            print(csvcontents)
    messagebox.showinfo("File Upload", "File has been uploaded!")

txtboxfilenameentry = ""


def anonymise():
    if filename != "":
        with open(filename, newline='') as File:
            rows = [row for row in csv.reader(File)]
            number: int = 0
            map = {}
            for row in rows:
                for item in row:
                    if item not in map:
                        map[item] = number
                        number += 1

            global anonymisedresult
            anonymisedresult = [[map[item] for item in row] for row in rows]
            print(anonymisedresult)
            messagebox.showinfo("Data Anonymisation", "Data has been anonymised!")
    else:
        messagebox.showwarning("File Upload Alert", "Please upload a file to anonymise!")


anonymisedresult = ""


def write():
    if filename != "":
        if anonymisedresult != "":
            global writefilename
            writefilename = r"C:\Users\UKFUNC.TRworkexpe04\Desktop\anonymised.csv"
            resultfile = open(writefilename, 'w')
            wr = csv.writer(resultfile)
            wr.writerows([anonymisedresult])
            messagebox.showinfo("Data Write", "Data has been written to a file!")
        else:
            messagebox.showwarning("File Anonymise Alert", "Please anonymise the data!")
    else:
        messagebox.showwarning("File Upload Alert", "Please upload a file to anonymise!")


filenameLabel = tk.Label(form, text="Select the file you would like to encrypt:").grid(row=0, column=0)
btnFileupload = tk.Button(form, text="Upload", command=uploadandread).grid(row=0, column=2)

btnanonymise = tk.Button(form, text="Anonymise", command=anonymise).grid(row=3, column=2)

btnwrite = tk.Button(form, text="Save anonymised data to a new file", command=write).grid(row=5, column=2)

form.mainloop()
