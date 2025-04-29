import tkinter as tk
import random
window = tk.Tk()
window.title('Day Mangement')
window.geometry("300x200")
label = tk.Label(window, text="")
label.pack(side ='bottom')
day_catagory = ['chill', 'coding', 'design']
chill_catagory = ['play games','watch movie', 'go outside']
code_catagory = ['api practice', 'ai practice', 'website practice']
design_catagory = ['Minecraft Design', 'Canva Design', 'Figma Design']



def daypicker():
    chosen_day = random.choice(day_catagory)
    return(chosen_day)

def activity(chosen_day):
    if chosen_day == 'chill':
        chosen_activity = random.choice(chill_catagory)
    elif chosen_day == 'coding':
        chosen_activity = random.choice(code_catagory)
    else:
        chosen_activity = random.choice(design_catagory)
    return(chosen_activity)
def button_click():
    chosen_day = daypicker()
    label.config(text= chosen_day +" "+ activity(chosen_day))
button = tk.Button(window, text="click me",fg = 'white', bg = 'green',width=10, height=2, command = button_click)
button.place(relx = 0.5, rely=0.5, anchor=tk.CENTER)
window.mainloop()



