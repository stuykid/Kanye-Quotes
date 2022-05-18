#import libraries
from tkinter import *
import requests

#function to access API data
def get_quote():
    #fetching data
    response = requests.get("https://api.kanye.rest")
    #alerts us if there are any issues accessing the data
    response.raise_for_status()
    #formatting data to be unpacked in json
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)



canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.gif")
canvas.create_image(150, 200, image=background_img)
quote_text = canvas.create_text(150, 207, text='Kanye says....', width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.gif")
# Button to toggle quotes
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
#Aligning Kanye's face with quote box
kanye_button.grid(row=1, column=0)



window.mainloop()