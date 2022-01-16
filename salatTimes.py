#BeautifulSoup a data scraping library
from bs4 import BeautifulSoup as bs
# Tkinter a Graphical User Interface Library 
from tkinter import *
import tkinter as tk
# Urllib for making web requests and read html pages
import urllib
import datetime

# TKINTER GUI 
top = tk.Tk()
top.title('Prayer Time - Casablanca')
top.geometry('550x320')
top.configure(background='coral')
filename = tk.PhotoImage(file = r"C:\masjid.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Link to scrape data from 
link = 'https://lematin.ma/horaire-priere-casablanca.html'

# Scraping data 
salat = urllib.request.Request(link, headers={'User-Agent' : 'Magic Browser'})
salaat = urllib.request.urlopen(salat)
salaatsoup = bs(salaat, 'lxml')
sobh = salaatsoup.find('span', attrs={'id' : 'As-sobh'}).text
chourouq = salaatsoup.find('span', attrs={'id' : 'Al-chourouq'}).text
dohr = salaatsoup.find('span', attrs={'id' : 'Ad-dohr'}).text
aasr = salaatsoup.find('span', attrs={'id' : 'Al-asr'}).text
maghreb = salaatsoup.find('span', attrs={'id' : 'Al-maghrib'}).text
ishaa = salaatsoup.find('span', attrs={'id' : 'Al-ichae'}).text
date = salaatsoup.find('div', attrs={'id' : 'date'}).text

# Func to get scraped data
def Prayer():
    global lbl
    lbl.config(text='Prayer Time in Casablanca\n' + date +'\n\n' +
               'As-sobh : ' + sobh  + '\n' +
               'Achourouq : ' + chourouq + '\n' + 
               'Ad-dohr : ' + dohr + '\n' + 
               'Al-Asr : ' + aasr + '\n' + 
               'Al-Maghreb : ' + maghreb + '\n' + 
               'Al-Ishae : ' + ishaa + '\n\n')  
               
    
    Btn2.config(state='active')
    Btn.config(state='disabled')
    
# Hide data
def hideinfos():
    lbl.config(text='Prayer Time in Casablanca')
    Btn2.config(state='disabled')
    Btn.config(state='active')
    
#month = salaatsoup.find('table', attrs={'class' : 'table table-striped'}).text
#print(month)

# TKINTER buttons
Btn = tk.Button(top, text='Get Prayer Time' , command=Prayer,activebackground='white',activeforeground='black',bg='lightblue3',bd =3,padx=5,pady=5,width=13,font='calibri 10')
Btn.pack(pady=30)
lbl = Label(top, text='Prayer Time in Casablanca')
lbl.pack()
Btn2 = tk.Button(top, text='Hide infos', command=hideinfos, state='disabled')
Btn2.pack(pady=10)

top.mainloop()



