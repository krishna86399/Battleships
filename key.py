# from pynput import keyboard
from pynput.keyboard import Key, Listener
  
# def show(key):
    
#     if key == Key.enter:
#         print("good")
          
#     if key != Key.enter:
#         print("try again")
	
#     # by pressing 'delete' button 
#     # you can terminate the loop 
#     if key == Key.enter: 
#         return False
  
# # Collect all event until released
# with Listener(on_press = show) as listener:
#     listener.join()

import tkinter as tk

app = tk.Tk()
app.geometry("200x100")

def callback(event):
    label["text"] = "You pressed Enter"

app.bind('<Return>', callback)

label = tk.Label(app, text="")
label.pack()

app.mainloop()








