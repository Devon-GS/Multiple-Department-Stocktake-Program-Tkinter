from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

def coffee():
    coffee = Toplevel()
    coffee.attributes("-topmost", True)
    coffee.title('Coffee Stock Take')
    coffee.iconbitmap('icons/coffee.ico')
    screen_width = coffee.winfo_screenwidth()
    screen_height = coffee.winfo_screenheight()
    app_width = 800 
    app_height = 800
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    coffee.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    

    # FUNCTIONS
    def display_ciro():      
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT ciroMachineSales FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def display_lavazza():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT lavazzaCapsule FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def display_ciro_cups():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT ciroCoffeeCups FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def display_lavazza_big_cups():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT lavazzaBigCoffeeCups FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def display_lavazza_small_cups():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT lavazzaSmallCoffeeCups FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def display_big_lids():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT bigLids FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def display_small_lids():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute('SELECT smallLids FROM coffee WHERE rowid=1')
        records = c.fetchall()
        sales = records[0][0]
        conn.commit()
        conn.close()
        return sales

    def submit_ciro():
        # Assign amouts to variables
        pre_sales = display_ciro()
        sales_reading = ciro_machine_sales_input.get()
        pos_sales = ciro_pos_sales_input.get()

        if sales_reading == '' or int(sales_reading) <= 0:
            ciro_error_display.config(text='Ciro machine sales not valid. Cannot be Zero. \n Please enter positive number')
        elif pos_sales == '' or int(pos_sales) < 0:
            ciro_error_display.config(text='POS sales not valid. Please enter positive number or Zero')
        else:
            ciro_error_display.config(text='')
            sales_reading = int(sales_reading)
            pos_sales = int(pos_sales)
            # Stock take calculation
            machine_sales = sales_reading - pre_sales
            short_over = pos_sales - machine_sales
            
            # Display stock take info int frame
            # ciro_diplay_frame = LabelFrame(coffee, text="Ciro Stock Display")
            # ciro_diplay_frame.grid(row=0, column=1, sticky=N+S)

            d_current_sales = Label(ciro_diplay_frame, text='Current Machine Sales: ' + str(f'{pre_sales:,}'.replace(',', ' ')))
            d_current_sales.grid(row=0, column=0)

            d_machine_sales = Label(ciro_diplay_frame, text='Machine Sales: ' + str(f'{sales_reading:,}'.replace(',', ' ')))
            d_machine_sales.grid(row=1, column=0)

            d_pos_sales = Label(ciro_diplay_frame, text='POS Sales: ' + str(f'{pos_sales:,}'.replace(',', ' ')))
            d_pos_sales.grid(row=2, column=0)
            
            if short_over > 0:
                short_over_display = Label(ciro_diplay_frame, text='OVER: ' + str(f'{short_over:,}'.replace(',', ' ')))
                short_over_display.grid(row=3, column=0)
            elif short_over < 0:
                short_over_display = Label(ciro_diplay_frame, text='SHORT: ' + str(f'{short_over:,}'.replace(',', ' ')))
                short_over_display.grid(row=3, column=0)
            else:
                short_over_display = Label(ciro_diplay_frame, text='BALANCE: ' + str(f'{short_over:,}'.replace(',', ' ')))
                short_over_display.grid(row=3, column=0)
            
            # Update database with new machine sales
            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = "UPDATE coffee SET ciroMachineSales = ? WHERE rowid = 1"
            query_cups = """UPDATE coffee SET 
                ciroCoffeeCups = ciroCoffeeCups - ?,
                smallLids = smallLids - ? 
                WHERE rowid = 1
                """
            c.execute(query, (sales_reading,))
            c.execute(query_cups, (pos_sales, pos_sales))
            conn.commit()
            conn.close()

            # Update display label and clear input
            ciro_previous_machine_sales_label.config(text='Current Machine Sales: ' + str(f'{display_ciro():,}'.replace(',', ' ')))
            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lids_small_onhand_label.config(text='Ciro cups on Hand: ' + str(display_small_lids()))
            ciro_machine_sales_input.delete(0,END)
            ciro_pos_sales_input.delete(0,END)

    def submit_lavazza():
        onhand = display_lavazza()
        purchases = purchase_input.get()
        sales_big = sales_big_input.get()
        sales_small = sales_small_input.get()
        current_count = current_cap_count_input.get()

        if purchases == '' or int(purchases) < 0:
            lavazza_error_display.config(text='Purchases cannot be negative. \n Please enter positive number / Zero or leave blank')
        elif sales_big == '' or int(sales_big) < 0:
            lavazza_error_display.config(text='Sales (Big) not valid. \n Please enter positive number or Zero')
        elif sales_small == '' or int(sales_small) < 0:
            lavazza_error_display.config(text='Sales (Small) not valid. \n Please enter positive number or Zero')
        elif current_count == '' or int(current_count) < 0:
            lavazza_error_display.config(text='Current count not valid. \n Please enter positive number or Zero')
        else:
            purchases = int(purchase_input.get())
            sales_big = int(sales_big_input.get())
            sales_small = int(sales_small_input.get())
            current_count = int(current_cap_count_input.get())

            # Stock take calculation
            sales = sales_big + sales_small
            sys_onhand = (onhand + purchases) - sales
            short_over = current_count - sys_onhand  

            # Display stock take info int frame
            lavazza_diplay_frame = LabelFrame(coffee, text="Lavazza Stock Display")
            lavazza_diplay_frame.grid(row=1, column=1, sticky=N+S)

            d_onhand = Label(lavazza_diplay_frame, text='Current Machine Sales: ' + str(display_lavazza()))
            d_onhand.grid(row=0, column=0)

            d_purchases = Label(lavazza_diplay_frame, text='Purcahses: ' + str(purchases))
            d_purchases.grid(row=1, column=0)

            d_sales = Label(lavazza_diplay_frame, text='POS Sales: ' + str(sales))
            d_sales.grid(row=2, column=0)

            d_current = Label(lavazza_diplay_frame, text='Current Count: ' + str(current_count))
            d_current.grid(row=3, column=0)
            
            if short_over > 0:
                short_over_display = Label(lavazza_diplay_frame, text='OVER: ' + str(short_over) )
                short_over_display.grid(row=4, column=0)
            elif short_over < 0:
                short_over_display = Label(lavazza_diplay_frame, text='SHORT: ' + str(short_over))
                short_over_display.grid(row=4, column=0)
            else:
                short_over_display = Label(lavazza_diplay_frame, text='BALANCE: ' + str(short_over))
                short_over_display.grid(row=4, column=0)
            
            # Update database with new machine sales
            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = "UPDATE coffee SET lavazzaCapsule = ? WHERE rowid = 1"
            query_cups = """UPDATE coffee SET 
                lavazzaBigCoffeeCups = lavazzaBigCoffeeCups - ?,
                lavazzaSmallCoffeeCups = lavazzaSmallCoffeeCups - ?,
                bigLids = bigLids - ?,
                smallLids = smallLids - ?
                WHERE rowid = 1"""
            c.execute(query, (current_count,))
            c.execute(query_cups, (sales_big, sales_small, sales_big, sales_small))
            conn.commit()
            conn.close()

            # Update display label and clear input
            lavazza_cap_onhand_label.config(text='Current Capsules on Hand: ' + str(display_lavazza()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            purchase_input.delete(0,END)
            sales_big_input.delete(0,END)
            sales_small_input.delete(0,END)
            current_cap_count_input.delete(0,END)

    def reset_cups_lids():
        # Cups
        ciro = ciro_cups_input.get()
        lavazza_big = lavazza_cups_bigs_input.get()
        lavazza_small = lavazza_cups_small_input.get()
        # Lids
        big_lids = lids_big_input.get()
        small_lids = lids_small_input.get()

        if (ciro == '' or int(ciro) < 0 or 
        lavazza_big == '' or int(lavazza_big) < 0 or
        lavazza_small == '' or int(lavazza_small) < 0 or 
        big_lids == '' or int(big_lids) < 0 or 
        small_lids == '' or int(small_lids) < 0):
            cups_error_display.config(text='Cup input cannot be blank or negative. \n If no update required please submit Zero')

        elif int(ciro) == 0:
            lavazza_big = int(lavazza_cups_bigs_input.get())
            lavazza_small = int(lavazza_cups_small_input.get())
            big_lids = int(lids_big_input.get())
            small_lids = int(lids_small_input.get())

            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = """UPDATE coffee SET 
                lavazzaBigCoffeeCups = ?,
                lavazzaSmallCoffeeCups = ?,
                bigLids = ?,
                smallLIds = ?
                WHERE rowid = 1"""
            c.execute(query, (lavazza_big, lavazza_small, big_lids, small_lids))
            conn.commit()
            conn.close()

            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            ciro_cups_input.delete(0,END)
            lavazza_cups_bigs_input.delete(0,END)
            lavazza_cups_small_input.delete(0,END)
            lids_big_input.delete(0,END)
            lids_small_input.delete(0,END)
        elif int(lavazza_big) == 0:
            ciro = int(ciro_cups_input.get())
            lavazza_small = int(lavazza_cups_small_input.get())
            big_lids = int(lids_big_input.get())
            small_lids = int(lids_small_input.get())

            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = """UPDATE coffee SET 
                ciroCoffeeCups = ?,
                lavazzaSmallCoffeeCups = ?,
                bigLids = ?,
                smallLIds = ?
                WHERE rowid = 1"""
            c.execute(query, (ciro, lavazza_small, big_lids, small_lids))
            conn.commit()
            conn.close()

            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            ciro_cups_input.delete(0,END)
            lavazza_cups_bigs_input.delete(0,END)
            lavazza_cups_small_input.delete(0,END)
            lids_big_input.delete(0,END)
            lids_small_input.delete(0,END)
        elif int(lavazza_small) == 0:
            ciro = int(ciro_cups_input.get())
            lavazza_big = int(lavazza_cups_bigs_input.get())
            big_lids = int(lids_big_input.get())
            small_lids = int(lids_small_input.get())

            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = """UPDATE coffee SET 
                ciroCoffeeCups = ?,
                lavazzaBigCoffeeCups = ?,
                bigLids = ?,
                smallLIds = ?
                WHERE rowid = 1"""
            c.execute(query, (ciro, lavazza_big, big_lids, small_lids))
            conn.commit()
            conn.close()

            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            ciro_cups_input.delete(0,END)
            lavazza_cups_bigs_input.delete(0,END)
            lavazza_cups_small_input.delete(0,END)
            lids_big_input.delete(0,END)
            lids_small_input.delete(0,END)
        elif int(big_lids) == 0:
            ciro = int(ciro_cups_input.get())
            lavazza_big = int(lavazza_cups_bigs_input.get())
            lavazza_small = int(lavazza_cups_small_input.get())
            small_lids = int(lids_small_input.get())

            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = """UPDATE coffee SET 
                ciroCoffeeCups = ?,
                lavazzaBigCoffeeCups = ?,
                lavazzaSmallCoffeeCups = ?,
                smallLIds = ?
                WHERE rowid = 1"""
            c.execute(query, (ciro, lavazza_big, lavazza_small, small_lids))
            conn.commit()
            conn.close()

            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            ciro_cups_input.delete(0,END)
            lavazza_cups_bigs_input.delete(0,END)
            lavazza_cups_small_input.delete(0,END)
            lids_big_input.delete(0,END)
            lids_small_input.delete(0,END)
        elif int(small_lids) == 0:
            ciro = int(ciro_cups_input.get())
            lavazza_big = int(lavazza_cups_bigs_input.get())
            lavazza_small = int(lavazza_cups_small_input.get())
            big_lids = int(lids_big_input.get())

            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = """UPDATE coffee SET 
                ciroCoffeeCups = ?,
                lavazzaBigCoffeeCups = ?,
                lavazzaSmallCoffeeCups = ?,
                bigLids = ?
                WHERE rowid = 1"""
            c.execute(query, (ciro, lavazza_big, lavazza_small, big_lids))
            conn.commit()
            conn.close()

            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            ciro_cups_input.delete(0,END)
            lavazza_cups_bigs_input.delete(0,END)
            lavazza_cups_small_input.delete(0,END)
            lids_big_input.delete(0,END)
            lids_small_input.delete(0,END)
        else:
            ciro = int(ciro_cups_input.get())
            lavazza_big = int(lavazza_cups_bigs_input.get())
            lavazza_small = int(lavazza_cups_small_input.get())
            big_lids = int(lids_big_input.get())
            small_lids = int(lids_small_input.get())

            conn = sqlite3.connect('database/stock.db') 
            c = conn.cursor()
            # Query DB
            query = """UPDATE coffee SET
                ciroCoffeeCups = ?, 
                lavazzaBigCoffeeCups = ?,
                lavazzaSmallCoffeeCups = ?,
                bigLids = ?,
                smallLIds = ?
                WHERE rowid = 1"""
            c.execute(query, (ciro, lavazza_big, lavazza_small, big_lids, small_lids))
            conn.commit()
            conn.close()

            ciro_cups_onhand_label.config(text='Ciro cups on Hand: ' + str(display_ciro_cups()))
            lavazza_cups_big_onhand_label.config(text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
            lavazza_cups_small_onhand_label.config(text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
            lids_small_onhand_label.config(text='Lids 250ml on Hand: ' + str(display_small_lids()))
            lids_big_onhand_label.config(text='Lids 350ml on Hand: ' + str(display_big_lids()))
            ciro_cups_input.delete(0,END)
            lavazza_cups_bigs_input.delete(0,END)
            lavazza_cups_small_input.delete(0,END)
            lids_big_input.delete(0,END)
            lids_small_input.delete(0,END)

    def view_stock():
        conn = sqlite3.connect('database/stock.db')
        c = conn.cursor()
        # Query DB
        c.execute("""SELECT
            ciroMachineSales,
            lavazzaCapsule,
            ciroCoffeeCups,
            lavazzaBigCoffeeCups,
            lavazzaSmallCoffeeCups,
            bigLids,
            smallLids
            FROM coffee 
            WHERE rowid=1""")
        stock_level = c.fetchall()
        conn.commit()
        conn.close()

        cms.config(text='Ciro Machine Sales: ' + str(stock_level[0][0]))
        lc.config(text='Lavazza Capsules: ' + str(stock_level[0][1]))
        cc.config(text='Ciro Cups: ' + str(stock_level[0][2]))
        lbc.config(text='Lavazza Big Cups: ' + str(stock_level[0][3]))
        lsc.config(text='Lavazza Small Cups: ' + str(stock_level[0][4]))
        bl.config(text='Big Lids: ' + str(stock_level[0][5]))
        sl.config(text='Small Lids: ' + str(stock_level[0][6]))

    # CIRO FRAME
    ciro_frame = LabelFrame(coffee, text="Ciro Coffee")
    ciro_frame.grid(row=0, column=0)

    ciro_previous_machine_sales_label = Label(ciro_frame, text='Current Machine Sales: ' + str(f'{display_ciro():,}'.replace(',', ' ')))
    ciro_previous_machine_sales_label.grid(row=0, column=0)

    ciro_machine_sales_label = Label(ciro_frame, text='Ciro Machine Sales')
    ciro_machine_sales_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    ciro_machine_sales_input = Entry(ciro_frame)
    ciro_machine_sales_input.grid(row=1, column=1, pady=(10, 0))

    ciro_pos_sales_label = Label(ciro_frame, text='Ciro Pos Sales')
    ciro_pos_sales_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    ciro_pos_sales_input = Entry(ciro_frame)
    ciro_pos_sales_input.grid(row=2, column=1, pady=(10, 0))

    ciro_error_display = Label(ciro_frame, text=' ')
    ciro_error_display.grid(row=3, column=0, columnspan=2, sticky=W+E)

    submit_ciro = Button(ciro_frame, text='Submit Ciro Stock Take', command=submit_ciro)
    submit_ciro.grid(row=4, column=0)

    # LAVAZZA FRAME
    lavazza_frame = LabelFrame(coffee, text="Lavazza Coffee")
    lavazza_frame.grid(row=1, column=0)

    lavazza_cap_onhand_label = Label(lavazza_frame, text='Current Capsules on Hand: ' + str(display_lavazza()))
    lavazza_cap_onhand_label.grid(row=0, column=0)

    purchase_label = Label(lavazza_frame, text='Purchases')
    purchase_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    purchase_input = Entry(lavazza_frame)
    purchase_input.grid(row=1, column=1, pady=(10, 0))

    sales_big_label = Label(lavazza_frame, text='Lavazza POS Sales Large Cups')
    sales_big_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    sales_big_input = Entry(lavazza_frame)
    sales_big_input.grid(row=2, column=1, pady=(10, 0))

    sales_small_label = Label(lavazza_frame, text='Lavazza POS Sales Small Cups')
    sales_small_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    sales_small_input = Entry(lavazza_frame)
    sales_small_input.grid(row=3, column=1, pady=(10, 0))

    current_cap_count_label = Label(lavazza_frame, text='Current Capsule Count')
    current_cap_count_label.grid(row=4, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    current_cap_count_input = Entry(lavazza_frame)
    current_cap_count_input.grid(row=4, column=1, pady=(10, 0))

    lavazza_error_display = Label(lavazza_frame, text=' ')
    lavazza_error_display.grid(row=5, column=0, columnspan=2, sticky=W+E)

    submit_lavazza = Button(lavazza_frame, text='Submit Lavazza Stock Take', command=submit_lavazza)
    submit_lavazza.grid(row=6, column=0)

    # CUP FRAME
    cup_frame = LabelFrame(coffee, text="Coffee Cup and Lid Stock")
    cup_frame.grid(row=2, column=0)

    # Current stock display 
    ciro_cups_onhand_label = Label(cup_frame, text='Ciro cups on Hand: ' + str(display_ciro_cups()))
    ciro_cups_onhand_label.grid(row=0, column=0)

    lavazza_cups_big_onhand_label = Label(cup_frame, text='Lavazza Cups 350ml on Hand: ' + str(display_lavazza_big_cups()))
    lavazza_cups_big_onhand_label.grid(row=1, column=0)

    lavazza_cups_small_onhand_label = Label(cup_frame, text='Lavazza Cups 250ml on Hand: ' + str(display_lavazza_small_cups()))
    lavazza_cups_small_onhand_label.grid(row=2, column=0)

    lids_big_onhand_label = Label(cup_frame, text='Lids 350ml on Hand: ' + str(display_big_lids()))
    lids_big_onhand_label.grid(row=3, column=0)

    lids_small_onhand_label = Label(cup_frame, text='Lids 250ml on Hand: ' + str(display_small_lids()))
    lids_small_onhand_label.grid(row=4, column=0)

    # Reset Frame
    reset_frame = LabelFrame(cup_frame)
    reset_frame.grid(row=5, column=0)

    reset_label = Label(reset_frame, text='Reset Cup Stock Level:')
    reset_label.grid(row=0, column=0)

    ciro_cups_label = Label(reset_frame, text='Ciro Cups')
    ciro_cups_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    ciro_cups_input = Entry(reset_frame)
    ciro_cups_input.grid(row=1, column=1, pady=(10, 0))

    lavazza_cups_bigs_label = Label(reset_frame, text='Lavazza Cups 350ml')
    lavazza_cups_bigs_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    lavazza_cups_bigs_input = Entry(reset_frame)
    lavazza_cups_bigs_input.grid(row=2, column=1, pady=(10, 0))

    lavazza_cups_small_label = Label(reset_frame, text='Lavazza Cups 250ml')
    lavazza_cups_small_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    lavazza_cups_small_input = Entry(reset_frame)
    lavazza_cups_small_input.grid(row=3, column=1, pady=(10, 0))

    lids_big_label = Label(reset_frame, text='Lids 350ml')
    lids_big_label.grid(row=4, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    lids_big_input = Entry(reset_frame)
    lids_big_input.grid(row=4, column=1, pady=(10, 0))
    
    lids_small_label = Label(reset_frame, text='Lids 250ml')
    lids_small_label.grid(row=5, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    lids_small_input = Entry(reset_frame)
    lids_small_input.grid(row=5, column=1, pady=(10, 0))

    cups_error_display = Label(reset_frame, text=' ')
    cups_error_display.grid(row=6, column=0, columnspan=2, sticky=W+E)

    submit_cups = Button(reset_frame, text='Submit Lavazza Stock Take', command=reset_cups_lids)
    submit_cups.grid(row=7, column=0)

    # View current Stock Level frame
    view_stock_frame = LabelFrame(coffee, text="View Current Stock Levels")
    view_stock_frame.grid(row=2, column=1, sticky=N+S+E+W)

    submit_view_stock = Button(view_stock_frame, text='View Stock Levels', command=view_stock)
    submit_view_stock.grid(row=0, column=0)

    cms = Label(view_stock_frame, text=' ')
    cms.grid(row=1, column=0)

    lc = Label(view_stock_frame, text=' ')
    lc.grid(row=2, column=0)

    cc = Label(view_stock_frame, text=' ')
    cc.grid(row=3, column=0)

    lbc = Label(view_stock_frame, text=' ')
    lbc.grid(row=4, column=0)

    lsc = Label(view_stock_frame, text=' ')
    lsc.grid(row=5, column=0)

    bl = Label(view_stock_frame, text=' ')
    bl.grid(row=6, column=0)

    sl = Label(view_stock_frame, text=' ')
    sl.grid(row=7, column=0)

    
            
     


    