import json
import os
import tkinter as tk
from tkinter import *

save_file = "save_file.json"

def update_statistics():
    statistics_var.set(f"""Clicks: {clicks}
Click Points: {click_points}
Click Points Per Click: {marketThing + 1}
Chocolate: {chocolate}
Milk: {milk}
Waffle: {waffle}
Cake: {cake}
Pizza: {pizza}
Coke: {coke}
Pasta: {pasta}
Hamburger: {hamburger}
Salad: {salad}
French Fries: {french_fries}
Cookie: {cookie}
Beer: {beer}
Melon: {melon}
Bread: {bread}
Wine: {wine}""")

def delete_saved_file():
    global clicks, click_points, marketThing, wine, bread, melon, beer, cookie, french_fries, salad, hamburger, pasta, coke, pizza, cake, waffle, milk, chocolate

    clicks = 0
    click_points = 0
    marketThing = 0
    wine = 0
    bread = 0
    melon = 0
    beer = 0
    cookie = 0
    french_fries = 0
    salad = 0
    hamburger = 0
    pasta = 0
    coke = 0
    pizza = 0
    cake = 0
    waffle = 0
    milk = 0
    chocolate = 0
    
    data = {
        "clicks": 0,
        "click_points" : 0,
        "marketThing" : 0,
        "wine": 0,
        "bread": 0,
        "melon": 0,
        "beer": 0,
        "cookie": 0,
        "french_fries": 0,
        "salad": 0,
        "hamburger": 0,
        "pasta": 0,
        "coke": 0,
        "pizza": 0,
        "cake": 0,
        "waffle": 0,
        "milk": 0,
        "chocolate": 0
    }
    with open(save_file, "w") as f:
        json.dump(data, f)

    update_statistics()
    text_var.set(f"Click Points Per Click: {marketThing + 1}\nYou clicked {clicks} times.\nClick Points: {click_points}")

def save_game():
    data = {
        "clicks": clicks,
        "click_points": click_points,
        "marketThing": marketThing,
        "wine": wine,
        "bread": bread,
        "melon": melon,
        "beer": beer,
        "cookie": cookie,
        "french_fries": french_fries,
        "salad": salad,
        "hamburger": hamburger,
        "pasta": pasta,
        "coke": coke,
        "pizza": pizza,
        "cake": cake,
        "waffle": waffle,
        "milk": milk,
        "chocolate": chocolate
    }
    with open(save_file, "w") as f:
        json.dump(data, f)

def load_game():
    global clicks, click_points, marketThing, wine, bread, melon, beer, cookie, french_fries, salad, hamburger, pasta, coke, pizza, cake, waffle, milk, chocolate
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
                wine = data.get("wine", 0)
                bread = data.get("bread", 0)
                melon = data.get("melon", 0)
                beer = data.get("beer", 0)
                cookie = data.get("cookie", 0)
                french_fries = data.get("french_fries", 0)
                salad = data.get("salad", 0)
                hamburger = data.get("hamburger", 0)
                pasta = data.get("pasta", 0)
                coke = data.get("coke", 0)
                pizza = data.get("pizza", 0)
                cake = data.get("cake", 0)
                waffle = data.get("waffle", 0)
                milk = data.get("milk", 0)
                chocolate = data.get("chocolate", 0)
                
        except (json.JSONDecodeError, ValueError):
            print("Kayıt dosyası bozuk ya da boş. Varsayılan değerlerle başlatılıyor.")
            clicks = 0
            click_points = 0
            marketThing = 0
            wine = 0
            bread = 0
            melon = 0
            beer = 0
            cookie = 0
            french_fries = 0
            salad = 0
            hamburger = 0
            pasta = 0
            coke = 0
            pizza = 0
            cake = 0
            waffle = 0
            milk = 0
            chocolate = 0


#main window
root = tk.Tk()
root.geometry("600x400") #main window size
root.title("Clicker Game") #main window title

statistics = None
market = None

marketThing = 0
clicks = 0
click_points = 0
text_var = tk.StringVar()

load_game()

text_var.set(f"Click Points Per Click: {marketThing + 1}\nYou clicked {clicks} times.\nClick Points: {click_points}")

statistics_var = tk.StringVar()
statistics_var.set(f"Clicks: {clicks}\nClick Points: {click_points}\nClick Points Per Click: {marketThing + 1}\nChocolate: {chocolate}\nMilk: {milk}\nWaffle: {waffle}\nCake: {cake}\nPizza: {pizza}\nCoke: {coke}\nPasta: {pasta}\nHamburger: {hamburger}\nSalad: {salad}\nFrench Fries: {french_fries}\nCookie: {cookie}\nBeer: {beer}\nMelon: {melon}\nBread: {bread}\nWine: {wine}") 

def statistics_func():
    global statistics
    if statistics is None or not statistics.winfo_exists():
        statistics = tk.Toplevel()
        statistics.title("Statistics")

        statistics_label = tk.Label(statistics,
            textvariable=statistics_var,
            bg="lightblue",
            height=60,
            width=120,
            font=("Arial", 24, "bold"),
            padx=15,
            pady=15,
            wraplength=250)
        statistics_label.pack()
    else:
        statistics.lift()


statistics_button = tk.Button(root,
                        text="Statistics",
                        command=statistics_func,
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
                        padx=18,
                        pady=5,
                        width=15,
                        wraplength=100)

statistics_button.pack(padx=50, pady=10)

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
                                    padx=10,
                                    pady=5,
                                    width=15,
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
        text_var.set(f"Click Points Per Click: {marketThing + 1}\nYou clicked {clicks} times.\nClick Points: {click_points}") # update the label
        save_game()

wine = 0
bread = 0
melon = 0
beer = 0
cookie = 0
french_fries = 0
salad = 0
hamburger = 0
pasta = 0
coke = 0
pizza = 0
cake = 0
waffle = 0
milk = 0
chocolate = 0
  
def chocolate_clicked():
    global chocolate
    market_buttons_clicked(100, 0.5)
    chocolate += 1
    update_statistics()
    return 0
def milk_clicked():
    global milk
    market_buttons_clicked(250, 1.5)
    milk += 1
    update_statistics()
    return 0
def waffle_clicked():
    global waffle
    market_buttons_clicked(750, 5)
    waffle += 1
    update_statistics()
    return 0
def cake_clicked():
    global cake
    market_buttons_clicked(2500, 20)
    cake += 1
    update_statistics()
    return 0
def pizza_clicked():
    global pizza
    market_buttons_clicked(7500, 70)
    pizza += 1
    update_statistics()
    return 0
def coke_clicked():
    global coke
    market_buttons_clicked(20000, 210)
    coke += 1
    update_statistics()
    return 0
def pasta_clicked():
    global pasta
    market_buttons_clicked(100000, 1100)
    pasta += 1
    update_statistics()
    return 0
def hamburger_clicked():
    global hamburger
    market_buttons_clicked(450000, 5000)
    hamburger += 1
    update_statistics()
    return 0
def salad_clicked():
    global salad
    market_buttons_clicked(1000000, 15750)
    salad += 1
    update_statistics()
    return 0
def french_fries_clicked():
    global french_fries 
    market_buttons_clicked(5000000, 80000)
    french_fries += 1
    update_statistics()
    return 0
def cookie_clicked():
    global cookie
    market_buttons_clicked(24000000, 390000)
    cookie += 1
    update_statistics()
    return 0
def beer_clicked():
    global beer
    market_buttons_clicked(250000000, 4000000)
    beer += 1
    update_statistics()
    return 0
def melon_clicked():
    global melon
    market_buttons_clicked(1000000000, 16500000)
    melon += 1
    update_statistics()
    return 0
def bread_clicked():
    global bread
    market_buttons_clicked(10000000000, 175000000)
    bread += 1
    update_statistics()
    return 0
def wine_clicked():
    global wine
    market_buttons_clicked(250000000000, 4500000000)
    wine += 1
    update_statistics()
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
    text_var.set(f"Click Points Per Click: {marketThing + 1}\nYou clicked {clicks} times.\nClick Points: {click_points}")
    save_game()
    update_statistics()


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