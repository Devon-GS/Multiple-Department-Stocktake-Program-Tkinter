from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import ingredients_st_func as i


def ingredients_stocktake():
    ing = Toplevel()
    ing.attributes("-topmost", True)
    ing.title('Ingredients Stock Take')
    ing.iconbitmap('icons/add.ico')
    ing.geometry('435x260')

    # Ingredients bought button
    ing_buy = Button(ing, text='Ingredient Purchases', command=i.purchases)
    ing_buy.grid(row=0, column=0)

    # Item sales button
    sale = Button(ing, text='Item Sales', command=i.sales)
    sale.grid(row=1, column=0)

    # Stock take button
    stock_take = Button(ing, text='Stock Take')
    stock_take.grid(row=2, column=0)

    # View current stock levels
    stock_level = Button(ing, text='View Current Stock')
    stock_level.grid(row=3, column=0)

    # Reset data base button
    reset_btn = Button(ing, text='Reset Data base')
    reset_btn.grid(row=4, column=0)

    # Exit button
    exit_btn = Button(ing, text='Exit')
    exit_btn.grid(row=5, column=0)





    

     

