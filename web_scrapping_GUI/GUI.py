import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from webScrapping import scrape_hotel_data
from tkcalendar import DateEntry

'''run function used  for GUI and give some info about program'''

root = tk.Tk()
root.title("Best Hotels for You")


def fetch_and_display():
    city = city_var.get()
    check_in_date = check_in_var.get()
    check_out_date = check_out_var.get()
    order_by = order.get()
    hotels = []

    # for control the date in lower then out
    try:
        check_in_Number = int(check_in_date.replace("-", ""))
        check_out_Number = int(check_out_date.replace("-", ""))
        if check_in_Number > check_out_Number: raise ValueError
        if city == "" or check_in_date == "" or check_out_date == "" or order_by == "": raise ValueError
        hotels = scrape_hotel_data(city, check_in_date, check_out_date, order_by)

        for i, hotel in enumerate(hotels):
            tree.insert("", "end", values=(
                i + 1, hotel['name'], hotel['location'], hotel['distance'], hotel['rating'], hotel['price'],
                hotel['comfort'][-3:]))

    except ValueError:
        messagebox.showerror("error about dates",
                             " Dates must be number and check in date can not be later then out date\n Your inputs are deleted \n Pls enter dates again")
        check_in_var.set("")
        check_out_var.set("")
    except Exception as e:
        print(f"an error occured\n {e}")
        aa = f"an error occured\n {e} \n program starting again \n pls take care to check in and out dates"
        messagebox.showinfo("Input type problem", aa)
        os.execv(sys.executable, [sys.executable] + sys.argv)


# Variables


cities = ["Marseille", "Dubrovnik", "Bari", "Zadar", "Barcelona", "Valencia", "Amsterdam", "Madrid", "Heraklion",
          "Bastia", 'Berlin', 'Paris', 'Rome', 'Madrid', 'Vienna', 'Lisbon', 'Prague', 'Warsaw', 'Brussels', 'Helsinki']
orderBy = ["price", "comfort", "rating"]
# Widgets
city_var = tk.StringVar()
ttk.Label(root, text="City:").pack()
ttk.Combobox(root, textvariable=city_var, values=cities).pack()

order = tk.StringVar()
ttk.Label(root, text="Order by:").pack()
ttk.Combobox(root, textvariable=order, values=orderBy).pack()

check_in_var = tk.StringVar()
ttk.Label(root, text="Check-in (YYYY-MM-DD):").pack()
ttk.Entry(root, textvariable=check_in_var).pack()

check_out_var = tk.StringVar()
ttk.Label(root, text="Check-out (YYYY-MM-DD):").pack()
ttk.Entry(root, textvariable=check_out_var).pack()

DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2).pack(padx=10, pady=10)

'''tl eu checkboxlari ayarla'''
currencyType = tk.StringVar()
ttk.Radiobutton(root, text='TL', variable=currencyType, value='TL').pack()
ttk.Radiobutton(root, text='EU', variable=currencyType, value='EU').pack()

'''button search'''
style = ttk.Style()
style.configure('Custom.TButton', foreground='blue', background='lightgray', font=('Helvetica', 12))
ttk.Button(root, text="Search", command=fetch_and_display, style='Custom.TButton').pack()

# Treeview to display hotels
tree = ttk.Treeview(root, columns=("Order", "Hotel Title", "Address", "Distance", "Rating", "Price", "Comfort"),
                    show='headings')
for col in tree["columns"]:
    tree.heading(col, text=col)
tree.pack()

root.mainloop()
