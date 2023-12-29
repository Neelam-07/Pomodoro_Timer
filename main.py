from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    count_down(70)    #the fun call  
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min= math.floor(count / 60)
    sec= count % 60

    if sec < 10:
    sec = f"0{sec}"    
    canvas.itemconfig(timer, text= f"{min}:{sec}")  
    if count >0:
       window.after(1000, count_down, count - 1 )     

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("POMODORA")  #means tomato in italian ..
window.config(padx=100, pady=50, bg= YELLOW)

#label:
label= Label(text="Timer", font= (FONT_NAME, 30, "bold"), fg= GREEN, bg= YELLOW)    
label.grid(column=2, row= 1)

#create a canvas from canvas widget !! to import pic in our gui:
canvas= Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
photo= PhotoImage(file= "/Neelam Rawat/python/Day_28,tkinter_dynamic_Typing_pamadora/tomato.png") 
canvas.create_image(100, 105, image= photo)
timer= canvas.create_text(100, 130, text= "00:00", fill= "white", font=(FONT_NAME, 20, "bold")) 
canvas.grid(column=2, row= 2)

#button:
start_button= Button(text= "Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=start_time )
start_button.grid(column=1, row= 3)

restart_button= Button(text= "restart", font=(FONT_NAME, 10, "normal"), highlightthickness=0) 
restart_button.grid(column=3, row= 3)

check_mark_label= Label(text= "✔", font=(FONT_NAME, 10, "normal"), fg= GREEN)
check_mark_label.grid(column=2, row=3)

window.mainloop()  

