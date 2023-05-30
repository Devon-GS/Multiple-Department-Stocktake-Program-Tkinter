from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3


def ingredients_purchase():
    ip = Toplevel()
    ip.attributes("-topmost", True)
    ip.title('Ingredients Purchased')
    ip.iconbitmap('icons/add.ico')
    ip.geometry('435x360')

    # FUNCTIONS
    def submit():
        pass

    # INPUTS AND LABELS
    info_label = Label(ip, text='Submit in grams where applicable')
    info_label.grid(row=0, column=0, columnspan=2, sticky=W+E, pady=(10, 0), padx=(5, 0))

    # Cheese
    slice_label = Label(ip, text='Cheese Slice')
    slice_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    slice_input = Entry(ip)
    slice_input.grid(row=1, column=1, pady=(10, 0))

    grated_label = Label(ip, text='Grated Cheese')
    grated_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    grated_input = Entry(ip)
    grated_input.grid(row=2, column=1, pady=(10, 0))

    # Bacon
    bacon_label = Label(ip, text='Bacon')
    bacon_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    bacon_input = Entry(ip)
    bacon_input.grid(row=3, column=1, pady=(10, 0))

    # Ham
    ham_label = Label(ip, text='Ham')
    ham_label.grid(row=4, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    ham_input = Entry(ip)
    ham_input.grid(row=4, column=1, pady=(10, 0))

    # Chicken Mayo
    chicken_mayo_label = Label(ip, text='Chicken Mayo')
    chicken_mayo_label.grid(row=5, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    chicken_mayo_input = Entry(ip)
    chicken_mayo_input.grid(row=5, column=1, pady=(10, 0))

    # Wraps
    wraps_label = Label(ip, text='Wraps')
    wraps_label.grid(row=6, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    wraps_input = Entry(ip)
    wraps_input.grid(row=6, column=1, pady=(10, 0))

    # Chicken Strips
    chicken_strips_label = Label(ip, text='Chicken Strips')
    chicken_strips_label.grid(row=7, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    chicken_strips_input = Entry(ip)
    chicken_strips_input.grid(row=7, column=1, pady=(10, 0))

    # Pizza Base
    pizza_base_label = Label(ip, text='Pizza Base')
    pizza_base_label.grid(row=8, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    pizza_base_input = Entry(ip)
    pizza_base_input.grid(row=8, column=1, pady=(10, 0)) 

    # Submit and close button
    submit_btn = Button(ip, text='Submit and Close', width=15, command=submit)
    submit_btn.grid(row=9, column=0, columnspan=2, sticky=W+E, padx=(10, 0), pady=(10, 0))