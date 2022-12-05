# Python program to test
# internet speed
import tkinter as tk
from tkinter import *
import speedtest
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import threading
import time
from multiprocessing import Process

global speedWithUnits
speedWithUnits = ''
option=''
def downloadSpeed():
	global option
	option='Download Speed'
	showSpeed()

def uploadSpeed():
	global option
	option='Upload Speed'
	showSpeed()

def ping():
	global option
	option='Ping'
	showSpeed()

def showSpeed():
	global option
	st = speedtest.Speedtest()
	if option == 'Download Speed':
		speed=(st.download())
	elif option == 'Upload Speed':
		speed=(st.upload())
	elif option == 'Ping':
		servernames =[]
		st.get_servers(servernames)
		Pingspeed =(st.results.ping)
		speed = -1
	speedWithUnits=''
	if(speed == -1):
		speedWithUnits=str(Pingspeed)+" ms"
	elif(speed<1000):
		speedWithUnits=str(round(speed, 3))+" bps"
	elif(speed<1000000):
		speedWithUnits=str(round(speed/1000, 3))+" Kbps"
	elif(speed<1000000000):
		speedWithUnits=str(round(speed/1000000, 3))+" Mbps"
	else:
		speedWithUnits=str(round(speed/1000000000, 3))+" Gbps"
	tkinter.messagebox.showinfo("Internet Speed Test Tool",  "Hello! Your " +option+" Speed is:"+speedWithUnits)

#Creating the main window 
wn = tkinter.Tk() 
wn.title("Network Speed Test Tool")
wn.geometry('1300x750')

#add background image
bg = PhotoImage(file = "professor.png")
label1 = Label( wn, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)

Label(wn, text='Network Speed Test Tool(ECE422)',bg='ivory3',
      fg='black', font=('times new roman', 28)).place(x=120, y=80, anchor=NW)

Label(wn, text='Choose any of the below options',bg='ivory3',
      fg='black', font=('times new roman', 18)).place(x=230, y=135)

#Button to Check Download Speed
Button(wn, text="Test Download Speed", bg='ivory3',font=('times new roman', 15),width=25,height=2,
       command=downloadSpeed).place(x=240, y=200)

#Button to Check Upload Speed
Button(wn, text="Test Upload Speed", bg='ivory3',font=('times new roman', 15),width=25,height=2,
       command=uploadSpeed).place(x=240, y=270)
	   
#Button to convert Audio to PDF form
Button(wn, text="Test Ping", bg='ivory3',font=('times new roman', 15),width=25,height=2,
       command=ping).place(x=240, y=340)

#Runs the window till it is closed
wn.mainloop()
