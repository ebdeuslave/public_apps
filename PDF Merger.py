import os
from PyPDF2 import PdfFileMerger
from datetime import date
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg

app = Tk()
app.title('PDF Merger, By Ebdeu')
app.geometry('300x300+600+300')
app.configure(background='coral')

today = date.today()
F = f'Commandes {today}.pdf'

def directory():
    global get_dir
    get_dir = filedialog.askdirectory()                # select PDFs folder
    getdir.configure(text=get_dir)                    # Show the directory
    if not get_dir:
        getdir.configure(text='/PATH/')
        

def mergePDF():
    try:
        merger = PdfFileMerger()
        list_pdf = []
        for path in os.listdir(get_dir):
            full_path = os.path.join(get_dir, path)
            if os.path.isfile(full_path):
                if full_path.endswith('pdf'):
                    list_pdf.append(full_path)   # find files end with .pdf and put them in a list 
        if list_pdf:
            for pdf_file in list_pdf:
                merger.append(pdf_file)
            merger.write(F)
            merger.close()
            msg.showinfo('Merged',f'{F} Merged in {os.getcwd()}') 
        else:
            msg.showwarning('PDFs not found', 'PDFs not found')
    except:
            msg.showerror('Invalid Folder', 'Choose a folder')


browse = Button(app, text='Browse Folder', command=directory,width=10)
browse.pack(pady=30)
getdir = Label(app, text='/PATH/')
getdir.pack(padx=1,pady=1)
merge = Button(app, text='Merge PDFs', command=mergePDF,activebackground='white',activeforeground='black',bg='lightblue',bd =1,padx=1,pady=1,width=12,font='calibri 10')
merge.pack(pady=70)

app.mainloop()


