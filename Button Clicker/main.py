import tkinter as tk
import functions
from tkinter import *

#main window
root = tk.Tk()
root.geometry("400x250") #main window size
root.title("Clicker Game") #main window title

market = None
marketThing = 0
clicks = 0
click_points = 0
text_var = tk.StringVar()
text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")

def market_clicked():
    global market
    if market is None or not market.winfo_exists():
        market = tk.Toplevel()
        market.title("Market")
        milkButton = tk.Button(market,
                               text="Milk\n+1.5 Per Clicks\n250 Click Points",
                               command=milk_clicked,
                               activebackground="blue",
                               activeforeground="white",
                               anchor="center",
                               bd=3,
                               bg="lightgray",
                               cursor="hand2",
                               disabledforeground="gray",
                               fg="black",
                               font=("Arial", 12),
                               height=4,
                               highlightbackground="black",
                               highlightcolor="green",
                               highlightthickness=2,
                               justify="center",
                               overrelief="raised",
                               padx=10,
                               pady=5,
                               width=10,
                               wraplength=100)

        milkButton.pack(pady=5)

        chocolateButton = tk.Button(market,
                                    text="Chocolate\n+0.5 Per Clicks\n100 Click Points",
                                    command=chocolate_clicked,
                                    activebackground="blue",
                                    activeforeground="white",
                                    anchor="center",
                                    bd=3,
                                    bg="lightgray",
                                    cursor="hand2",
                                    disabledforeground="gray",
                                    fg="black",
                                    font=("Arial", 12),
                                    height=4,
                                    highlightbackground="black",
                                    highlightcolor="green",
                                    highlightthickness=2,
                                    justify="center",
                                    overrelief="raised",
                                    padx=10,
                                    pady=5,
                                    width=10,
                                    wraplength=100)

        chocolateButton.pack(pady=5)

    else:
        market.lift()  # Eğer zaten açıksa öne getir

def market_buttons_clicked(click_points_amount, increase_amount):
    global click_points
    global  marketThing
    if click_points >= click_points_amount:
        click_points -= click_points_amount
        marketThing += increase_amount
        text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")  # update the label
def chocolate_clicked():
    market_buttons_clicked(100, 0.5)
def milk_clicked():
    market_buttons_clicked(250, 1.5)
def waffle_clicked():
    market_buttons_clicked(750, 5)
def cake_clicked():
    market_buttons_clicked(2500, 25)
def pizza_clicked():
    market_buttons_clicked(7500, 100)
def coke_clicked():
    market_buttons_clicked(20000, 300)
def pasta_clicked():
    market_buttons_clicked(100000, 2000)
def hamburger_clicked():
    market_buttons_clicked(450000, 10000)
def salad_clicked():
    market_buttons_clicked(1000000, 20000)
def french_fries_clicked():
    market_buttons_clicked(5000000, 110000)
def cookie_clicked():
    market_buttons_clicked(24000000, 540000)
def beer_clicked():
    market_buttons_clicked(250000000, 6000000)
def melon_clicked():
    market_buttons_clicked(1000000000, 25000000)
def bread_clicked():
    market_buttons_clicked(10000000000, 300000000)
def wine_clicked():
    market_buttons_clicked(250000000000, 8000000000)

def button1_clicked():
    global clicks
    global marketThing
    global click_points
    click_points += 1 + marketThing
    clicks += 1
    text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")  # update the label




#label widget with all options
label = tk.Label(root,
                 textvariable=text_var,
                 #anchor=tk.CENTER,
                 bg="lightblue",
                 height=3,
                 width=30,
                 #bd=3,
                 font=("Arial", 16, "bold"),
                 #cursor="hand2",
                 #fg="red",
                 padx=15,
                 pady=15,
                 #justify=tk.CENTER,
                 #relief=tk.RAISED,
                 #underline=0,
                 wraplength=250)

#pack the label into the window
label.pack(pady=20) #add padding to the top

market_button = tk.Button(root,
                   text="Market",
                   command=market_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
market_button.pack(padx=50, pady=10)

# Creating a button with specified options
button = tk.Button(root,
                   text="Click Me",
                   command=button1_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=50, pady=10)

root.mainloop() #run