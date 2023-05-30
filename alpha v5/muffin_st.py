from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

def muffin_stocktake():
    muffin = Toplevel()
    muffin.attributes("-topmost", True)
    muffin.title('Muffin Stock Take')
    muffin.iconbitmap('icons/muffin_icon.ico')
    muffin.geometry('435x260')

    # FUNCTIONS
    def reset():
        response = messagebox.askyesno('WARNING MESSAGE', 'You are about to overwrite muffin stock level. Would you like to proceed?', icon='warning')
        if response == 1:
            # Create a database or connect to one
            conn = sqlite3.connect('database/muffin_stock.db')
            # Create cursor 
            c = conn.cursor()
            # Query DB
            # Create table when run for first time
            c.execute('CREATE TABLE IF NOT EXISTS muffins (stock REAL, purchases REAL, sales REAL)')

            # Delete all rows
            c.execute('DELETE FROM muffins')
            
            # Reset stock, perchases and level to zero
            query_reset = "INSERT INTO muffins (rowid, stock, purchases, sales) VALUES (1, 0, 0 ,0)"
            c.execute(query_reset)

            # Reset stock users input
            reset = reset_input.get()
            query = "UPDATE muffins SET stock = ? WHERE rowid = 1"
            c.execute(query, (reset,))
            #  Commit Changes to db
            conn.commit()
            # Close Connection to db
            conn.close() 
        else:
            messagebox.showinfo('Info', 'Stock Not Reset')

        reset_input.delete(0,END)

    def purchases():
        # Create a database or connect to one
        conn = sqlite3.connect('database/stock.db')
        # Create cursor 
        c = conn.cursor()
        # Query DB
        purchases = purchase_input.get()
        query = "UPDATE muffins SET purchases = ? WHERE rowid = 1"
        c.execute(query, (purchases,))
        #  Commit Changes to db
        conn.commit()
        # Close Connection to db
        conn.close()
        purchase_input.delete(0,END)

    def sales():
        # Create a database or connect to one
        conn = sqlite3.connect('database/stock.db')
        # Create cursor 
        c = conn.cursor()
        # Query DB
        sales = sales_input.get()
        query = "UPDATE muffins SET sales = ? WHERE rowid = 1"
        c.execute(query, (sales,))
        #  Commit Changes to db
        conn.commit()
        # Close Connection to db
        conn.close()
        sales_input.delete(0,END)

    def actual():
        # Create a database or connect to one
        conn = sqlite3.connect('database/stock.db')
        # Create cursor 
        c = conn.cursor()
        # Query DB
        c.execute('SELECT * FROM muffins WHERE rowid=1')
        records = c.fetchall()
        sys_stock = records[0][0]
        purchases = records[0][1]
        sales = records[0][2]

        actual_stock_onhand = float(actual_count_input.get())

        sys_stock_onhand = (sys_stock + purchases) - sales
        if actual_stock_onhand > sys_stock_onhand:
            
            x = actual_stock_onhand - sys_stock_onhand
            messagebox.showinfo('STOCK OVER', 'Stock over by ' + str(x) + ' grams'
                            + '\n\nSystem Stock = ' + str(sys_stock_onhand) + ' grams' 
                            + '\nActual stock = ' +str(actual_stock_onhand) + ' grams',
                            icon='warning'
                            )
        elif actual_stock_onhand < sys_stock_onhand:
            x = sys_stock_onhand - actual_stock_onhand
            messagebox.showinfo('STOCK SHORT', 'Stock short by ' + str(x) + ' grams'
                            + '\n\nSystem Stock = ' + str(sys_stock_onhand) + ' grams' 
                            + '\nActual stock = ' +str(actual_stock_onhand) + ' grams',
                            icon='warning'
                            )
        else:
            messagebox.showinfo('STOCK EVEN', 'Stock Even'
                            + '\n\nSystem Stock = ' + str(sys_stock_onhand) + ' grams' 
                            + '\nActual stock = ' +str(actual_stock_onhand) + ' grams',
                            icon='info'
                            )

        query = ("""
                    UPDATE muffins SET 
                    stock = ?,
                    purchases = 0,
                    sales = 0        
                    WHERE rowid = 1
                """)
        c.execute(query, (actual_stock_onhand,))        
        #  Commit Changes to db
        conn.commit()
        # Close Connection to db
        conn.close()

        actual_count_input.delete(0,END)
    
    def view():
        # Create a database or connect to one
        conn = sqlite3.connect('database/stock.db')
        # Create cursor 
        c = conn.cursor()
        # Query DB
        c.execute('SELECT stock FROM muffins WHERE rowid=1')
        records = c.fetchall()
        current_stock = records[0][0]
        view_stock_label = Label(muffin, text=current_stock, borderwidth=2, relief='solid')
        view_stock_label.grid(row=6, column=0, columnspan=3, ipadx=30, ipady=10)
        # messagebox.showinfo('Info', 'Current Stock Level is ' + str(records[0][0]) + ' grams')
        #  Commit Changes to db
        conn.commit()
        # Close Connection to db
        conn.close()

    # INPUTS AND LABELS
    # Initialize or Reset Stock
    reset_label = Label(muffin, text='Initialize or Reset Stock Level')
    reset_label.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    global reset_input
    reset_input = Entry(muffin)
    reset_input.grid(row=0, column=1, pady=(10, 0))

    # Purchases label and Input
    purchase_label = Label(muffin, text='Purchases')
    purchase_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    global purchase_input
    purchase_input = Entry(muffin)
    purchase_input.grid(row=2, column=1, pady=(10, 0))

    # Sales label and Input
    sales_label = Label(muffin, text='Sales from last Stocktake to Now')
    sales_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    global sales_input
    sales_input = Entry(muffin)
    sales_input.grid(row=3, column=1, pady=(10, 0))

    # Actual count label and Input
    actual_count_label = Label(muffin, text='Actual count')
    actual_count_label.grid(row=4, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    global actual_count_input
    actual_count_input = Entry(muffin)
    actual_count_input.grid(row=4, column=1, pady=(10, 0))

    # BUTTONS
    # Initialize or Reset Stock Button
    reset_btn = Button(muffin, text='Reset Stock Level', width=15, command=reset)
    reset_btn.grid(row=0, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

    # Purchases Button
    purchase_btn = Button(muffin, text='Add Purchases', width=15, command=purchases)
    purchase_btn.grid(row=2, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

    # Sales Button
    sales_btn = Button(muffin, text='Add Sales', width=15, command=sales)
    sales_btn.grid(row=3, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

    # Actual Stock
    actual_count_btn = Button(muffin, text='Calulate Stock Take', width=15,command=actual)
    actual_count_btn.grid(row=4, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

    # View Current Stock
    view_stock_btn = Button(muffin, text='View Current Stock', command=view)
    view_stock_btn.grid(row=5, column=0, columnspan=3, sticky=W+E, pady=(10, 0), padx=(5, 0))

    # Exit Button
    exit_btn = Button(muffin, text='Exit', command=muffin.destroy)
    exit_btn.grid(row=7, column=0, columnspan=3, sticky=W+E, pady=(10, 0), padx=(5, 0))