import subprocess, sys, importlib
from urllib.request import urlopen , Request
import json, webbrowser
from tkinter import *
# Check if module installed if not run pip to install it
if not importlib.util.find_spec('bs4'):
	subprocess.check_call([sys.executable, '-m', 'pip' , 'install', 'bs4'])
from bs4 import BeautifulSoup as bs

app = Tk()
app.title('Amana Tracking')
# app.geometry('600x630')
app.state("zoomed")
app.configure(background='lightblue')

def creator():
    webbrowser.open('https://www.instagram.com/ebdeuslave/')   

menu = Menu()
created = Menu(menu,tearoff=False)
menu.add_cascade(label='Created by', menu=created)
created.add_command(label='@ebdeuslave' , command=creator)

def tracking():
	result = ''
	link = 'https://bam-tracking.barid.ma/Tracking/Search?trackingCode=' + inputCAB.get()
	### read html ###
	req = Request(link,headers={'User-Agent': 'Mozilla/5.0'})
	openLink = urlopen(req).read()
	soup = bs(openLink, 'lxml')
	### convert to JSON ###
	json_data = json.loads(openLink)
	### Soup HTML text from JSON ###
	soup = bs(json_data['Html'], 'lxml')
	### Get Data ###
	notFound = soup.find('h5', {'class':'text-orange mt-5 text-uppercase'})
	if notFound != None and 'Aucune information':
		result = 'Code Amana est introuvable'
		resultLabel.config(text=result)

	else:
		city = soup.find('div', {'class':'tooltip_depart margin3 lblRecipient'}).text
		mt = soup.find('span', {'class':'b-subtitle lblMttCrbt'}).text
		date_livraison = soup.find('span', {'class':'b-subtitle text-uppercase'}).text
		if date_livraison == '../../....':
			date_livraison = 'Non Livré'

		ul = soup.find('ul', {'class':'timeline'})
		bullet = ul.find_all('div',{'class': 'bullet'})
		dates = ul.find_all('div',{'class': 'container_date'})
		msgs = ul.find_all('div',{'class': 'mt-3 mb-5'})

		result += f'''
CAB : {inputCAB.get()}
Ville : {city}
Montant : {mt}
Date de livraison : {date_livraison}
		'''

		for x,y,z in zip(bullet, dates, msgs):
			result += f'\n############ {x.text.strip()} ############\n'
			result += y.text.strip() + '\n'
			result += z.text.strip()[6:] + '\n'
			resultLabel.config(text=result)
		print(result)
	
formCAB = Label(app, text='Donnez moi un CAB : ').pack(pady=20)
inputCAB = Entry()
inputCAB.pack(pady=10)


Button(app, text='Track', command=tracking).pack(pady=5)

resultLabel = Label(app, width=100, height=500)
resultLabel.pack()

app.config(menu=menu)
app.mainloop()
