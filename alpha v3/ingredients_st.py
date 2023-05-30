from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from ingredients_st_buy import ingredients_purchase as buy


def ingredients_stocktake():
    ing = Toplevel()
    ing.attributes("-topmost", True)
    ing.title('Ingredients Purchased')
    ing.iconbitmap('icons/add.ico')
    ing.geometry('435x260')

    # Ingredients bought button
    ing_buy = Button(ing, text='Ingredient Purchases', command=buy)
    ing_buy.grid(row=0, column=0)
        

