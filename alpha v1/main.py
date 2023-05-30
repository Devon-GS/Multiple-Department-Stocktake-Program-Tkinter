from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Sasol De Bron - Stock Count')
root.iconbitmap('icons/muffin_icon.ico')
root.geometry('435x225')

# FUNCTIONS
def reset():
    response = messagebox.askyesno('WARNING MESSAGE', 'You are about to overwrite stock level. Would you like to proceed?', icon='warning')
    if response == 1:
        # Create a database or connect to one
        conn = sqlite3.connect('muffin_stock.db')
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
    conn = sqlite3.connect('muffin_stock.db')
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
    conn = sqlite3.connect('muffin_stock.db')
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
    conn = sqlite3.connect('muffin_stock.db')
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
                           + '\nActual stock = ' +str(actual_stock_onhand) + ' grams'
                           )
    elif actual_stock_onhand < sys_stock_onhand:
        x = sys_stock_onhand - actual_stock_onhand
        messagebox.showinfo('STOCK SHORT', 'Stock short by ' + str(x) + ' grams'
                           + '\n\nSystem Stock = ' + str(sys_stock_onhand) + ' grams' 
                           + '\nActual stock = ' +str(actual_stock_onhand) + ' grams',
                           icon='warning'
                           )
    else:
        messagebox.showinfo('STOCK SHORT', 'Stock short by 0 grams'
                           + '\n\nSystem Stock = ' + str(sys_stock_onhand) + ' grams' 
                           + '\nActual stock = ' +str(actual_stock_onhand) + ' grams',
                           icon='warning'
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
    conn = sqlite3.connect('muffin_stock.db')
    # Create cursor 
    c = conn.cursor()
    # Query DB
    c.execute('SELECT stock FROM muffins WHERE rowid=1')
    records = c.fetchall()
    messagebox.showinfo('Info', 'Current Stock Level is ' + str(records[0][0]) + ' grams')
    #  Commit Changes to db
    conn.commit()
    # Close Connection to db
    conn.close()

# INPUTS AND LABELS
# Initialize or Reset Stock
reset_label = Label(root, text='Initialize or Reset Stock Level')
reset_label.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
reset_input = Entry(root)
reset_input.grid(row=0, column=1, pady=(10, 0))

# Purchases label and Input
purchase_label = Label(root, text='Purchases')
purchase_label.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
purchase_input = Entry(root)
purchase_input.grid(row=2, column=1, pady=(10, 0))

# Sales label and Input
sales_label = Label(root, text='Sales from last Stocktake to Now')
sales_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
sales_input = Entry(root)
sales_input.grid(row=3, column=1, pady=(10, 0))

# Actual count label and Input
actual_count_label = Label(root, text='Actual count')
actual_count_label.grid(row=4, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
actual_count_input = Entry(root)
actual_count_input.grid(row=4, column=1, pady=(10, 0))

# BUTTONS
# Initialize or Reset Stock Button
reset_btn = Button(root, text='Reset Stock Level', width=15, command=reset)
reset_btn.grid(row=0, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

# Purchases Button
purchase_btn = Button(root, text='Add Purchases', width=15, command=purchases)
purchase_btn.grid(row=2, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

# Sales Button
sales_btn = Button(root, text='Add Sales', width=15, command=sales)
sales_btn.grid(row=3, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

# Actual Stock
actual_count_btn = Button(root, text='Calulate Stock Take', width=15,command=actual)
actual_count_btn.grid(row=4, column=2, sticky=W, padx=(10, 0), pady=(10, 0))

# View Current Stock
view_stock_btn = Button(root, text='View Current Stock', command=view)
view_stock_btn.grid(row=5, column=0, columnspan=3, sticky=W+E, pady=(10, 0), padx=(5, 0))

# Exit Button
exit_btn = Button(root, text='Exit', command=root.quit)
exit_btn.grid(row=6, column=0, columnspan=3, sticky=W+E, pady=(10, 0), padx=(5, 0))

# Run program
root.mainloop()