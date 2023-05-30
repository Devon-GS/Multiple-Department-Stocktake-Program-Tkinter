from tkinter import *
from os import path
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import os
import shutil

def reset():
    response = messagebox.askyesno('WARNING MESSAGE', 'You are about to overwrite all stock levels. Would you like to proceed?', icon='warning')
    if response == 1:
        # Create a database or connect to one
        conn = sqlite3.connect('database/stock.db')
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
        c.execute("""CREATE TABLE IF NOT EXISTS ingredientsSales (
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
        c.execute("""CREATE TABLE IF NOT EXISTS coffee (
            ciroMachineSales INTEGER,
            lavazzaCapsule INTEGER,
            ciroCoffeeCups INTRGER,
            lavazzaBigCoffeeCups INTEGER,
            lavazzaSmallCoffeeCups INTEGER,
            bigLids INTEGER,
            smallLids INTEGER
                )""")

        # Delete all rows
        c.execute('DELETE FROM muffins')
        c.execute('DELETE FROM ingredients')
        c.execute('DELETE FROM ingredientsSales')
        c.execute('DELETE FROM coffee')
        
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
        query_ingredients_sales = """INSERT INTO ingredientsSales (
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
        query_coffee_sales = """INSERT INTO coffee (
            rowid,
            ciroMachineSales,
            lavazzaCapsule,
            ciroCoffeeCups,
            lavazzaBigCoffeeCups,
            lavazzaSmallCoffeeCups,
            bigLids,
            smallLids
            )
            VALUES (1, 0, 0, 0, 0, 0, 0, 0)"""
        c.execute(query_muffin)
        c.execute(query_ingredients)
        c.execute(query_ingredients_sales)
        c.execute(query_coffee_sales)

        #  Commit Changes to db
        conn.commit()
        # Close Connection to db
        conn.close()

def database_init():
    # Create a database or connect to one
    conn = sqlite3.connect('database/stock.db')
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
    c.execute("""CREATE TABLE IF NOT EXISTS ingredientsSales (
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
    c.execute("""CREATE TABLE IF NOT EXISTS coffee (
        ciroMachineSales INTEGER,
        lavazzaCapsule INTEGER,
        ciroCoffeeCups INTRGER,
        lavazzaBigCoffeeCups INTEGER,
        lavazzaSmallCoffeeCups INTEGER,
        bigLids INTEGER,
        smallLids INTEGER
            )""")

    # Delete all rows
    c.execute('DELETE FROM muffins')
    c.execute('DELETE FROM ingredients')
    c.execute('DELETE FROM ingredientsSales')
    c.execute('DELETE FROM coffee')
    
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
    query_ingredients_sales = """INSERT INTO ingredientsSales (
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
    query_coffee_sales = """INSERT INTO coffee (
        rowid,
        ciroMachineSales,
        lavazzaCapsule,
        ciroCoffeeCups,
        lavazzaBigCoffeeCups,
        lavazzaSmallCoffeeCups,
        bigLids,
        smallLids
        )
        VALUES (1, 0, 0, 0, 0, 0, 0, 0)"""
    c.execute(query_muffin)
    c.execute(query_ingredients)
    c.execute(query_ingredients_sales)
    c.execute(query_coffee_sales)

    #  Commit Changes to db
    conn.commit()
    # Close Connection to db
    conn.close()     

def backup():
    folder = filedialog.askdirectory(initialdir='shell:MyComputerFolder')
    src = "database/stock.db"
    dest = folder
    shutil.copy(src, dest)
