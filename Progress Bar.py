from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

window=Tk()
window.geometry('300x300')
window.title('Progress')

def step():
	bar['value'] += 20


bar = Progressbar(window,length=180,)
bar.grid(padx=50,pady=10)
bt=Button(window,text='Progress',command=step).grid(padx=50,pady=10)

window.mainloop()
