from tkinter import *
import requests

def new_text():
    quote = requests.get("https://api.kanye.rest")
    quote.raise_for_status()
    text = quote.json()["quote"]
    canvas1.itemconfig(canvas_text,text=text)

window = Tk()
background = PhotoImage(file="background.png")
window.title("Kanya App")
quote = requests.get("https://api.kanye.rest")
quote.raise_for_status()
text = quote.json()["quote"]

canvas1 = Canvas(width=310, height=430)
back_image = PhotoImage(file="background.png")
canvas1.create_image(155, 225, image=back_image)
canvas_text = canvas1.create_text(155, 225, text=text, width=250, font=("Arial",15,'italic'), fill='white')
canvas1.grid(row=0, column=0)

button = Button(width=110, height=150)
face_image = PhotoImage(file="kanye.png")
button.config(image=face_image, bg ="white",command=new_text, bd=0)
button.grid(row=1, column=0)






window.mainloop()

























