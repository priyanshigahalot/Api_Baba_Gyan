from tkinter import *
import requests
color="#80BCBD"

def get_quote():
 response= requests.get(url="https://api.kanye.rest")
 response.raise_for_status()
 data=response.json()
 quote=data["quote"]
 canvas.itemconfig(quote_text,text=quote)

window = Tk()
window.title("what he  Says...")
window.config(padx=50, pady=50,bg=color)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=" Baba ka Gyan Goes HERE", width=250, font=("Arial", 30, "bold"), fill="#1D2B53")

canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,bg=color)
kanye_button.grid(row=1, column=0)



window.mainloop()