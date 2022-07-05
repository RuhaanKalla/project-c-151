# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:47:55 2022

@author: dell
"""
from tkinter import*
root = Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(background = "purple")

label_months = Label(root, fg = "cyan" , bg = "purple" , font = 25)
label_profit = Label(root,fg = "cyan" , bg = "purple" , font = 25)
label_max_profit = Label(root,fg = "cyan" , bg = "purple" , font = 25)
label_min_profit = Label(root,fg = "cyan" , bg = "purple" , font = 25)

label_profit.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)
label_months.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)
label_max_profit.place(relx = 0.5 , rely = 0.6, anchor = CENTER)
label_min_profit.place(relx = 0.5 , rely = 0.8, anchor = CENTER)

months = ("January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December")

profits = (5000 , 98000 , 90000 , 45000 , 60000 , 40000  ,150000 , 700000 , 54000 , 65000 , 78000)
label_months["text"] = "Months : " + str(months)
label_profit["text"] = "Profit : " + str(profits)
max_profits_index = 0
min_profits_index = 0
def max_profits():
    max_profits = max(profits)
    max_profits_index = profits.index(max_profits)
    max_profits_month = months[max_profits_index]
    label_max_profit["text"] = "The maximum profit which is " + str(max_profits) + " was recorded in " + str(max_profits_month)

def min_profits():
    min_profits = min(profits)
    min_profits_index = profits.index(min_profits)
    min_profits_month = months[min_profits_index]
    label_min_profit["text"] = "The minimum profit which is " + str(min_profits) + " was recorded in " + str(min_profits_month)    

btn_max_profit = Button(root , text = "Show max profitable month" , command = max_profits , fg = "purple" , bg = "cyan" , font = 25)
btn_max_profit.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
btn_min_profit = Button(root , text = "Show min profitable month" , command = min_profits , fg = "purple" , bg = "cyan" , font = 25)
btn_min_profit.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)
print(max_profits_index)


print(min_profits_index)
root.mainloop()