import json
import os
import tkinter as tk
from tkinter import *

save_file = "save_file.json"

def delete_saved_file():
    global clicks
    global click_points
    global marketThing
    
    clicks = 0
    click_points = 0
    marketThing = 0

    data = {
        "clicks": 0,
        "click_points" : 0,
        "marketThing" : 0
    }
    with open(save_file, "w") as f:
        json.dump(data, f)

    text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")

def save_game():
    data = {
        "clicks": clicks,
        "click_points": click_points,
        "marketThing": marketThing
    }
    with open(save_file, "w") as f:
        json.dump(data, f)

def load_game():
    global clicks, click_points, marketThing
    if os.path.exists(save_file):
        try:
            with open(save_file, "r") as f:
                content = f.read().strip()
                if not content:
                    raise ValueError("Boş dosya.")
                data = json.loads(content)
                clicks = data.get("clicks", 0)
                click_points = data.get("click_points", 0)
                marketThing = data.get("marketThing", 0)
        except (json.JSONDecodeError, ValueError):
            print("Kayıt dosyası bozuk ya da boş. Varsayılan değerlerle başlatılıyor.")
            clicks = 0
            click_points = 0
            marketThing = 0


#main window
root = tk.Tk()
root.geometry("600x400") #main window size
root.title("Clicker Game") #main window title

market = None
marketThing = 0
clicks = 0
click_points = 0
text_var = tk.StringVar()

load_game()

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
                                    height=4,
                                    highlightbackground="black",
                                    highlightcolor="green",
                                    highlightthickness=2,
                                    justify="center",
                                    overrelief="raised",
                                    padx=8,
                                    pady=5,
                                    width=16,
                                    wraplength=100)
    return Button

def market_clicked():
    global market
    if market is None or not market.winfo_exists():
        market = tk.Toplevel()
        market.title("Market")

        # Ürün bilgilerini liste olarak tanımla
        products = [
            ("Wine\n+4500000000 Per Clicks\n250000000000 Click Points", wine_clicked),
            ("Bread\n+175000000 Per Clicks\n10000000000 Click Points", bread_clicked),
            ("Melon\n+16500000 Per Clicks\n1000000000 Click Points", melon_clicked),
            ("Beer\n+4000000 Per Clicks\n250000000 Click Points", beer_clicked),
            ("Cookie\n+390000 Per Clicks\n24000000 Click Points", cookie_clicked),
            ("French Fries\n+80000 Per Clicks\n5000000 Click Points", french_fries_clicked),
            ("Salad\n+15750 Per Clicks\n1000000 Click Points", salad_clicked),
            ("Hamburger\n+5000 Per Clicks\n450000 Click Points", hamburger_clicked),
            ("Pasta\n+1100 Per Clicks\n100000 Click Points", pasta_clicked),
            ("Coke\n+210 Per Clicks\n20000 Click Points", coke_clicked),
            ("Pizza\n+70 Per Clicks\n7500 Click Points", pizza_clicked),
            ("Cake\n+20 Per Clicks\n2500 Click Points", cake_clicked),
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
        save_game()
    
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
    market_buttons_clicked(2500, 20)
    return 0
def pizza_clicked():
    market_buttons_clicked(7500, 70)
    return 0
def coke_clicked():
    market_buttons_clicked(20000, 210)
    return 0
def pasta_clicked():
    market_buttons_clicked(100000, 1100)
    return 0
def hamburger_clicked():
    market_buttons_clicked(450000, 5000)
    return 0
def salad_clicked():
    market_buttons_clicked(1000000, 15750)
    return 0
def french_fries_clicked():
    market_buttons_clicked(5000000, 80000)
    return 0
def cookie_clicked():
    market_buttons_clicked(24000000, 390000)
    return 0
def beer_clicked():
    market_buttons_clicked(250000000, 4000000)
    return 0
def melon_clicked():
    market_buttons_clicked(1000000000, 16500000)
    return 0
def bread_clicked():
    market_buttons_clicked(10000000000, 175000000)
    return 0
def wine_clicked():
    market_buttons_clicked(250000000000, 4500000000)
    return 0

delete_button = tk.Button(root,
                                    text="Restart",
                                    command=delete_saved_file,
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
delete_button.pack(padx=50, pady=10)

def button1_clicked():
    global clicks
    global marketThing
    global click_points
    click_points += 0.5 + marketThing
    clicks += 1
    text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")  # update the label
    save_game()




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

def on_close():
    save_game()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop() #run