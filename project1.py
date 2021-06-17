from matplotlib import pyplot as plt
#from matplotlib import style
import os 
import pandas as pd
import pyttsx3
import speech_recognition as sr
#import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import webbrowser 
#import getpass
#import os
#import smtplib,ssl
import wikipedia
import tkinter as tk 
from tkinter import *
import tkinter.font as font
figure2 = Figure(figsize=(4,3))
query="abc"
os.chdir("D:\dyp\SY\swayam\week3")
data=pd.read_excel('file1.xlsx')
def takeCommand():
    frame1.grid(row=0,column=0)
    #frame3 = Frame(root,padx="60",pady="30",width="500",height="380")
    frame3.grid(row=0,column=1)
    frame2.grid(row=1,columnspan=2)
    trylabel['text']="      "
    labeluser['text']="       "
    labelquery['text']="         "
    
    
    #labelquery.grid_forget()
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        labeluser['text']="User said:"
        labelquery['text']=query
    except Exception as e:
        print(e)   
        trylabel['text']="Try again"
        
        return 'none'
    #return query
    if 'population' in query or 'chart' in query :
            chart()
            
    elif 'Wikipedia' in query:
            res = query.split() 
            speak('Searching Wikipedia...')
            results = wikipedia.summary(res[2], sentences=2)

            speak("According to Wikipedia")
            

            speak(results)

def speak(audio):
    label1 = Label(frame2, text = audio,font=("calibri",20),fg="black")
    label1.pack(side=BOTTOM)
    engine.say(audio)
    engine.runAndWait()

def chart():
     
    subplot2 = figure2.add_subplot(111)
    subplot2.axis('equal')
    subplot2.pie(data["population"], labels = data["c1"],autopct='%1.01f%%')
    #subplot2.title("Pie chart: population accross cities")
    #plt.show()
    chart1 = FigureCanvasTkAgg(figure2, frame3)
    chart1.get_tk_widget().pack(fill=BOTH)
    #chart1.get_tk_widget().pack_forget()

def clear() :
    #chart1.get_tk_widget().destroy()
    frame3.grid_forget()
    frame2.grid_forget()

def close() :
    if messagebox.askyesnocancel(title="Exit", message="Want to close application ?") :
        root.destroy()
    

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('rate',130)
   engine.setProperty('voice',voice.id[1])
#speak("hello sir. Please tell me how may I help you")
root = tk.Tk()
root.geometry("800x600") 
frame1 = Frame(root,padx="60",pady="30",width="500",height="600")
frame2 = Frame(root,padx="60",pady="30",width="800",height="200")
frame3 = Frame(root,padx="60",pady="30",width="500",height="380")
frame1.grid(row=0,column=0)
frame3.grid(row=0,column=1)
frame2.grid(row=1,columnspan=2)
#os.chdir("F:\dyp\SY\python\project")
#photo = PhotoImage(file = r"F:\dyp\SY\python\project\Mic.png")
btn_style = font.Font(weight="bold") 

button1 = tk.Button(frame1,border="8", padx="10", pady="5",text="SPEAK",fg="Black",command=takeCommand)
#button1.config(image="Mic.png")
button2 = tk.Button(frame1,border="8", padx="10", pady="5", text="CLEAR",fg="blue",command=clear)
button3 = tk.Button(frame1,border="8", padx="10", pady="5", text="EXIT",fg="red",command=close)
button1['font']=btn_style
button2['font']=btn_style
button3['font']=btn_style
button1.grid(row=0,column=0,padx="40")
button2.grid(row=1,pady="81")
button3.grid(row=2,)
trylabel = Label(frame2,font=("calibri",20),fg="black")
trylabel.grid()
labeluser= Label(frame2,font=("calibri",20),fg="black")
labelquery= Label(frame2,font=("calibri",20),fg="black")
labeluser.grid(row=0,column=0)
labelquery.grid(row=0,column=1)

 
chart1 = FigureCanvasTkAgg(figure2, frame3)
root.mainloop()
print("end")