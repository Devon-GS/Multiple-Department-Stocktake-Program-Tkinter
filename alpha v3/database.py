from tkinter import *
from os import path
from tkinter import messagebox
import sqlite3

def reset():
    response = messagebox.askyesno('WARNING MESSAGE', 'You are about to overwrite all stock levels. Would you like to proceed?', icon='warning')
    if response == 1:
        # Create a database or connect to one
        conn = sqlite3.connect('database/muffin_stock.db')
        # Create cursor 
        c = conn.cursor()
        # Query DB
        # Create table when run for first time
        c.execute('CREATE TABLE IF NOT EXISTS muffins (stock REAL, purchases REAL, sales REAL)')
        c.execute("""CREATE TABLE IF NOT EXISTS ingredients (
            cheeseSlice REAL,
            cheeseGrated REAL,
            bacon REAL,
            ham REAL,
            chickenMayo REAL,
            chips REAL,
            wraps REAL,
            chickenStrips REAL,
            pizzaBase REAL 
                )""")

        # Delete all rows
        c.execute('DELETE FROM muffins')
        c.execute('DELETE FROM ingredients')
        
        # Reset stock, perchases and level to zero
        query_muffin = "INSERT INTO muffins (rowid, stock, purchases, sales) VALUES (1, 0, 0 ,0)"
        query_ingredients = """INSERT INTO ingredients (
            rowid,
            cheeseSlice,
            cheeseGrated,
            bacon,
            ham,
            chickenMayo,
            chips,
            wraps,
            chickenStrips,
            pizzaBase
            )
            VALUES (1, 0, 0, 0, 0 ,0 ,0, 0, 0, 0)"""
        c.execute(query_muffin)
        c.execute(query_ingredients)

        #  Commit Changes to db
        conn.commit()
        # Close Connection to db
        conn.close()     

def database_init():
    # Create a database or connect to one
    conn = sqlite3.connect('database/muffin_stock.db')
    # Create cursor 
    c = conn.cursor()
    # Query DB
    # Create table when run for first time
    c.execute('CREATE TABLE IF NOT EXISTS muffins (stock REAL, purchases REAL, sales REAL)')
    c.execute("""CREATE TABLE IF NOT EXISTS ingredients (
        cheeseSlice REAL,
        cheeseGrated REAL,
        bacon REAL,
        ham REAL,
        chickenMayo REAL,
        chips REAL,
        wraps REAL,
        chickenStrips REAL,
        pizzaBase REAL 
            )""")

    # Delete all rows
    c.execute('DELETE FROM muffins')
    c.execute('DELETE FROM ingredients')
    
    # Reset stock, perchases and level to zero
    query_muffin = "INSERT INTO muffins (rowid, stock, purchases, sales) VALUES (1, 0, 0 ,0)"
    query_ingredients = """INSERT INTO ingredients (
        rowid,
        cheeseSlice,
        cheeseGrated,
        bacon,
        ham,
        chickenMayo,
        chips,
        wraps,
        chickenStrips,
        pizzaBase
        )
        VALUES (1, 0, 0, 0, 0 ,0 ,0, 0, 0, 0)"""
    c.execute(query_muffin)
    c.execute(query_ingredients)

    #  Commit Changes to db
    conn.commit()
    # Close Connection to db
    conn.close()     



