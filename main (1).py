import tkinter as tk
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



def button_func(text1, command1):
    Button = tk.Button(market,
                                    text=text1,
                                    command=command1,
                                    activebackground="blue",
                                    activeforeground="white",
                                    anchor="center",
                                    bd=3,
                                    bg="lightgray",
                                    cursor="hand2",
                                    disabledforeground="gray",
                                    fg="black",
                                    font=("Arial", 12),
                                    height=5,
                                    highlightbackground="black",
                                    highlightcolor="green",
                                    highlightthickness=2,
                                    justify="center",
                                    overrelief="raised",
                                    padx=8,
                                    pady=5,
                                    width=25,
                                    wraplength=100)
    return Button

def market_clicked():
    global market
    if market is None or not market.winfo_exists():
        market = tk.Toplevel()
        market.title("Market")

        # Ürün bilgilerini liste olarak tanımla
        products = [
            ("Wine\n+8000000000 Per Clicks\n250000000000 Click Points", wine_clicked),
            ("Bread\n+300000000 Per Clicks\n10000000000 Click Points", bread_clicked),
            ("Melon\n+25000000 Per Clicks\n1000000000 Click Points", melon_clicked),
            ("Beer\n+6000000 Per Clicks\n250000000 Click Points", beer_clicked),
            ("Cookie\n+540000 Per Clicks\n24000000 Click Points", cookie_clicked),
            ("French Fries\n+115000 Per Clicks\n5000000 Click Points", french_fries_clicked),
            ("Salad\n+22000 Per Clicks\n1000000 Click Points", salad_clicked),
            ("Hamburger\n+10000 Per Clicks\n450000 Click Points", hamburger_clicked),
            ("Pasta\n+2000 Per Clicks\n100000 Click Points", pasta_clicked),
            ("Coke\n+300 Per Clicks\n20000 Click Points", coke_clicked),
            ("Pizza\n+100 Per Clicks\n7500 Click Points", pizza_clicked),
            ("Cake\n+25 Per Clicks\n2500 Click Points", cake_clicked),
            ("Waffle\n+5 Per Clicks\n750 Click Points", waffle_clicked),
            ("Milk\n+1.5 Per Clicks\n250 Click Points", milk_clicked),
            ("Chocolate\n+0.5 Per Clicks\n100 Click Points", chocolate_clicked),
        ]

        # Grid yerleşimi için sütun sayısı
        columns = 3

        for idx, (text, func) in enumerate(products):
            row = idx // columns
            col = idx % columns
            btn = button_func(text, func)
            btn.grid(row=row, column=col, padx=5, pady=5)

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
    return 0
def milk_clicked():
    market_buttons_clicked(250, 1.5)
    return 0
def waffle_clicked():
    market_buttons_clicked(750, 5)
    return 0
def cake_clicked():
    market_buttons_clicked(2500, 25)
    return 0
def pizza_clicked():
    market_buttons_clicked(7500, 100)
    return 0
def coke_clicked():
    market_buttons_clicked(20000, 300)
    return 0
def pasta_clicked():
    market_buttons_clicked(100000, 2000)
    return 0
def hamburger_clicked():
    market_buttons_clicked(450000, 10000)
    return 0
def salad_clicked():
    market_buttons_clicked(1000000, 22000)
    return 0
def french_fries_clicked():
    market_buttons_clicked(5000000, 115000)
    return 0
def cookie_clicked():
    market_buttons_clicked(24000000, 540000)
    return 0
def beer_clicked():
    market_buttons_clicked(250000000, 6000000)
    return 0
def melon_clicked():
    market_buttons_clicked(1000000000, 25000000)
    return 0
def bread_clicked():
    market_buttons_clicked(10000000000, 300000000)
    return 0
def wine_clicked():
    market_buttons_clicked(250000000000, 8000000000)
    return 0

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