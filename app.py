from gtts import gTTS
# import os
import tkinter as tk
from io import BytesIO 
import pygame
import time

pygame.init()
pygame.mixer.init()

# def wait():
#     while pygame.mixer.get_busy():
#         time.sleep(.1)

def speak(text):
    mp3_fo = BytesIO()
    tts = gTTS(text ,lang="en")
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    
    sound.play()
    # wait()

def timeInWords():                                    #Time in words
    h = int(time.localtime().tm_hour)
    m = int(time.localtime().tm_min)
    hour={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",0:"twelve"}
    min={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine"}

    if m==0:
        result = hour[h%12]+" o' clock"
    elif m==1:
        result = min[m]+" minute past "+hour[h%12]
    elif m==30:
        result = "half past "+hour[h%12]
    elif m==15:
        result = "quarter past "+hour[h%12]
    elif m==45:
        result = "quarter to "+hour[(h+1)%12]
    elif m>30:
        result = min[60-m]+" minutes to "+hour[(h+1)%12]
    else:
        result = min[m]+" minutes past "+hour[h%12]

    if h<12:
        result=result+"am"
    else:
        result=result+"pm"

    return result

def update_time():                                      #Binary time and updating
    current_hr = int(time.localtime().tm_hour)
    current_min = int(time.localtime().tm_min)
    if int(current_hr)==0:
        current_hr=str(12)
        am.config(fg="red",bg="black")
        pm.config(fg="#303030",bg="black")
    elif int(current_hr)==12:
        pm.config(fg="red",bg="black")
        am.config(fg="#303030",bg="black")
    elif int(current_hr)>12:
        current_hr=str(int(current_hr)-12)
        pm.config(fg="red",bg="black")
        am.config(fg="#303030",bg="black")
    else:
        am.config(fg="red",bg="black")
        pm.config(fg="#303030",bg="black")

    # print(current_hr,type(current_hr))
    bm=bin(int(current_min))[2::]
    bh=bin(int(current_hr))[2::]
    bh=('0')*(4-len(bh))+bh
    bm=('0')*(6-len(bm))+bm
    if bm[0]=='1':
        time_label1.config(fg="red",bg="black")
    else:
        time_label1.config(fg="#303030",bg="black")
    if bm[1]=='1':
        time_label2.config(fg="red",bg="black")
    else:
        time_label2.config(fg="#303030",bg="black")
    if bm[2]=='1':
        time_label3.config(fg="red",bg="black")
    else:
        time_label3.config(fg="#303030",bg="black")
    if bm[3]=='1':
        time_label4.config(fg="red",bg="black")
    else:
        time_label4.config(fg="#303030",bg="black")
    if bm[4]=='1':
        time_label5.config(fg="red",bg="black")
    else:
        time_label5.config(fg="#303030",bg="black")
    if bm[5]=='1':
        time_label6.config(fg="red",bg="black")
    else:
        time_label6.config(fg="#303030",bg="black")
    
    if bh[0]=='1':
        time_label7.config(fg="red",bg="black")
    else:
        time_label7.config(fg="#303030",bg="black")
    if bh[1]=='1':
        time_label8.config(fg="red",bg="black")
    else:
        time_label8.config(fg="#303030",bg="black")
    if bh[2]=='1':
        time_label9.config(fg="red",bg="black")
    else:
        time_label9.config(fg="#303030",bg="black")
    if bh[3]=='1':
        time_label10.config(fg="red",bg="black")
    else:
        time_label10.config(fg="#303030",bg="black")
        #   res+=" "+str(min[i])
    global text
    text=timeInWords()
    # print(text)
    # print("looping")
    time_label.config(text=f"{time.strftime('%H:%M:%S')}",fg="red",bg="black")
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Binary Clock")
root.minsize(400,230)
root.maxsize(400,230)
root.configure(bg='black')

time_label1 = tk.Label(root, text="32 ", font=("Helvetica", 20))
time_label1.place(x=50, y=100)
time_label2 = tk.Label(root, text="16 ", font=("Helvetica", 20))
time_label2.place(x=100, y=100)
time_label3 = tk.Label(root, text="8 ", font=("Helvetica", 20))
time_label3.place(x=150, y=100)
time_label4 = tk.Label(root, text="4 ", font=("Helvetica", 20))
time_label4.place(x=200, y=100)
time_label5 = tk.Label(root, text="2", font=("Helvetica", 20))
time_label5.place(x=250, y=100)
time_label6 = tk.Label(root, text="1", font=("Helvetica", 20))
time_label6.place(x=300, y=100)
pm = tk.Label(root, text="pm", font=("Helvetica", 20))
pm.place(x=240, y=20)
am = tk.Label(root, text="am", font=("Helvetica", 20))
am.place(x=300, y=20)

time_label7 = tk.Label(root, text="8", font=("Helvetica", 20))
time_label7.place(x=50, y=20)
time_label8 = tk.Label(root, text="4", font=("Helvetica", 20))
time_label8.place(x=100, y=20)
time_label9 = tk.Label(root, text="2", font=("Helvetica", 20))
time_label9.place(x=150, y=20)
time_label10 = tk.Label(root, text="1", font=("Helvetica", 20))
time_label10.place(x=200, y=20)

time_label=tk.Label(root, text="", font=("Helvetica", 20))
time_label.place(x=130,y=180)

speak_but = tk.Button(root,
                      text=f"What's Time Now",
                      bg="red",fg="black",
                      command=lambda: speak(text))
speak_but.place(x=135,y=150)

update_time()  # Start updating the time label

root.mainloop()