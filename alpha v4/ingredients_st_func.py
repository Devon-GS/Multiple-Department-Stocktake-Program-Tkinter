from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3


def purchases():
    ip = Toplevel()
    ip.attributes("-topmost", True)
    ip.title('Ingredients Purchased')
    ip.iconbitmap('icons/add.ico')
    ip.geometry('435x360')

    # FUNCTIONS
    def submit():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c_slice         = slice_input.get()
        c_grated        = grated_input.get()
        bacon           = bacon_input.get()
        ham             = ham_input.get()
        chicken_mayo    = chicken_mayo_input.get()
        chips           = chips_input.get()
        wraps           = wraps_input.get()
        chicken_strips  = chicken_strips_input.get()
        pizza_base      = pizza_base_input.get()

        query = """UPDATE ingredients SET
            cheeseSlice = ?,
            cheeseGrated = ?,
            bacon = ?,
            ham = ?,
            chickenMayo = ?,
            chips = ?,
            wraps = ?,
            chickenStrips = ?,
            pizzaBase = ?
            
            WHERE rowid = 1"""

        c.execute(query, (c_slice, c_grated, bacon, ham, chicken_mayo, chips, wraps, chicken_strips, pizza_base))

        conn.commit()
        conn.close() 

        slice_input.delete(0,END)
        grated_input.delete(0,END)
        bacon_input.delete(0,END)
        ham_input.delete(0,END)
        chicken_mayo_input.delete(0,END)
        chips_input.delete(0,END)
        wraps_input.delete(0,END)
        chicken_strips_input.delete(0,END)
        pizza_base_input.delete(0,END)

        ip.destroy()

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

    # Chips
    chips_label = Label(ip, text='Chips')
    chips_label.grid(row=6, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    chips_input = Entry(ip)
    chips_input.grid(row=6, column=1, pady=(10, 0))

    # Wraps
    wraps_label = Label(ip, text='Wraps')
    wraps_label.grid(row=7, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    wraps_input = Entry(ip)
    wraps_input.grid(row=7, column=1, pady=(10, 0))

    # Chicken Strips
    chicken_strips_label = Label(ip, text='Chicken Strips')
    chicken_strips_label.grid(row=8, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    chicken_strips_input = Entry(ip)
    chicken_strips_input.grid(row=8, column=1, pady=(10, 0))

    # Pizza Base
    pizza_base_label = Label(ip, text='Pizza Base')
    pizza_base_label.grid(row=9, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    pizza_base_input = Entry(ip)
    pizza_base_input.grid(row=9, column=1, pady=(10, 0)) 

    # Submit and close button
    submit_btn = Button(ip, text='Submit and Close', width=15, command=submit)
    submit_btn.grid(row=10, column=0, columnspan=2, sticky=W+E, padx=(10, 0), pady=(10, 0))

def sales():
    sales = Toplevel()
    sales.attributes("-topmost", True)
    sales.title('Ingredients Sales')
    sales.iconbitmap('icons/add.ico')
    sales.geometry('520x260')

    # FUNCTIONS
    def submit():
        c_slice         = int(s_chicken_mayo_input.get()) * 50



        # c_grated        = grated_input.get()
        # bacon           = bacon_input.get()
        # ham             = ham_input.get()
        # chicken_mayo    = chicken_mayo_input.get()
        # chips           = chips_input.get()
        # wraps           = wraps_input.get()
        # chicken_strips  = chicken_strips_input.get()
        # pizza_base      = pizza_base_input.get()

    # FRAME SANDWICH
    sandwich_frame = LabelFrame(sales, text="Sandwich Sales")
    sandwich_frame.grid(row=0, column=0)

    s_chicken_mayo_label = Label(sandwich_frame, text='Chicken Mayo')
    s_chicken_mayo_label.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    s_chicken_mayo_input = Entry(sandwich_frame)
    s_chicken_mayo_input.grid(row=0, column=1, pady=(10, 0))

    s_hct_label = Label(sandwich_frame, text='Ham Cheese Tomato')
    s_hct_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    s_hct_input = Entry(sandwich_frame)
    s_hct_input.grid(row=1, column=1, pady=(10, 0))

    s_bacon_label = Label(sandwich_frame, text='Bacon and Cheese')
    s_bacon_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    s_bacon_input = Entry(sandwich_frame)
    s_bacon_input.grid(row=2, column=1, pady=(10, 0))

    # FRAME VETKOEK
    vetkoek_frame = LabelFrame(sales, text="Vetkoek Sales")
    vetkoek_frame.grid(row=0, column=1, sticky=N)

    v_chicken_mayo_label = Label(vetkoek_frame, text='Chicken Mayo')
    v_chicken_mayo_label.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    v_chicken_mayo_input = Entry(vetkoek_frame)
    v_chicken_mayo_input.grid(row=0, column=1, pady=(10, 0))

    v_hct_label = Label(vetkoek_frame, text='Ham Cheese Tomato')
    v_hct_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    v_hct_input = Entry(vetkoek_frame)
    v_hct_input.grid(row=1, column=1, pady=(10, 0))

    # FRAME OTHER
    other_frame = LabelFrame(sales, text="Other Item Sales")
    other_frame.grid(row=2, column=0)

    o_wrap_label = Label(other_frame, text='Wraps')
    o_wrap_label.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    o_wrap_input = Entry(other_frame)
    o_wrap_input.grid(row=0, column=1, pady=(10, 0))

    o_pizza_label = Label(other_frame, text='Pizza Slice')
    o_pizza_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    o_pizza_input = Entry(other_frame)
    o_pizza_input.grid(row=1, column=1, pady=(10, 0))

    o_chips_label = Label(other_frame, text='Chips')
    o_chips_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    o_chips_input = Entry(other_frame)
    o_chips_input.grid(row=2, column=1, pady=(10, 0))

    o_breakfast_label = Label(other_frame, text='Breakfast Croissant')
    o_breakfast_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    o_breakfast_input = Entry(other_frame)
    o_breakfast_input.grid(row=3, column=1, pady=(10, 0))

    # Submit and close button
    submit_btn = Button(sales, text='Submit and Close', width=15, command=submit)
    submit_btn.grid(row=2, column=1, columnspan=2, sticky=W+E, padx=(10, 0), pady=(10, 0))
