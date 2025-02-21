import tkinter as tk

from PIL import Image
window = tk.Tk()
window.title("Visual Novel")
window.geometry("400x400")

story = "You meet a woman on the way to a Replit meetup IRL"

def i_code():
  global story
  canvas.itemconfig(container, image = code)
  story = "She tries to pull out her laptop and drops it on the floor"
  story_label["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()

def i_replit():
  global story
  canvas.itemconfig(container, image = replit)
  story = "Why I use Replit of course, like every sane individual!"
  story_label["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button5.pack()
  button6.pack()

def i_laptop():
  global story
  canvas.itemconfig(container, image = laptop)
  story = "You pull out your laptop and begin coding"
  story_label["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  button7.pack()
  button8.pack()

def i_dropped_laptop():
  global story
  canvas.itemconfig(container, image = dropped_laptop)
  story = "You drop your laptop and pass out"
  story_label["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  button9.pack()
  button10.pack()

def i_happy():
  global story
  canvas.itemconfig(container, image = happy)
  story = "She smiles at you happily"
  story_label["text"] = story
  button7.pack_forget()
  button8.pack_forget()
  button11.pack()
  button12.pack()

def i_sad():
  global story
  canvas.itemconfig(container, image = sad)
  story = "She looks sadly at you"
  story_label["text"] = story
  button7.pack_forget()
  button8.pack_forget()
  button13.pack()
  button14.pack()

def i_code_again():
  global story
  canvas.itemconfig(container, image = code)
  story = "You pull out your laptop and begin coding"
  story_label["text"] = story
  button9.pack_forget()
  button10.pack_forget()
  button15.pack()
  button16.pack()

def i_dropped_laptop_again():
  global story
  canvas.itemconfig(container, image = dropped_laptop)
  story = "You drop your laptop and pass out"
  story_label["text"] = story
  button11.pack_forget()
  button12.pack_forget()
  button17.pack()
  button18.pack()

def i_happy_again():
  global story
  canvas.itemconfig(container, image = happy)
  story = "She smiles at you happily"
  story_label["text"] = story
  button13.pack_forget()
  button14.pack_forget()
  button19.pack()
  button20.pack()

def i_sad_again():
  global story
  canvas.itemconfig(container, image = sad)
  story = "She looks sadly at you"
  story_label["text"] = story
  button13.pack_forget()
  button14.pack_forget()
  button21.pack()
  button22.pack()

canvas = tk.Canvas(window, width = 300, height = 200)
canvas.pack()
container = canvas.create_image(150,150, image = None)
story_label = tk.Label(text = story)
story_label.pack()
button = tk.Button(text = "Ask her how she codes", command = i_code)
button.pack()
button2 = tk.Button(text = "Tell her about Replit", command = i_replit)
button2.pack()
button3 = tk.Button(text = "Show a laptop", command = i_laptop)
button3.pack()
button4 = tk.Button(text = "Drop the laptop", command = i_dropped_laptop)
button4.pack()
button5 = tk.Button(text = "Show a laptop", command = i_happy)
button5.pack()
button6 = tk.Button(text = "Drop the laptop", command = i_sad)
button6.pack()
button7 = tk.Button(text = "Ask her how she codes", command = i_code_again)
button7.pack()
button8 = tk.Button(text = "Tell her about Replit", command = i_dropped_laptop_again)
button8.pack()
button9 = tk.Button(text = "Show a laptop", command = i_happy_again)
button9.pack()
button10 = tk.Button(text = "Drop the laptop", command = i_sad_again)
button10.pack()
button11 = tk.Button(text = "Show a laptop", command = i_happy_again)
button11.pack()
button12 = tk.Button(text = "Drop the laptop", command = i_sad_again)
button12.pack()
button13 = tk.Button(text = "Show a laptop", command = i_happy_again)
button13.pack()
button14 = tk.Button(text = "Drop the laptop", command = i_sad_again)
button14.pack()
button15 = tk.Button(text = "Show a laptop", command = i_happy_again)
button15.pack()
button16 = tk.Button(text = "Drop the laptop", command = i_sad_again)
button16.pack()
button17 = tk.Button(text = "Show a laptop", command = i_happy_again)
button17.pack()
button18 = tk.Button(text = "Drop the laptop", command = i_sad_again)
button18.pack()
button19 = tk.Button(text = "Show a laptop", command = i_happy_again)
button19.pack()
button20 = tk.Button(text = "Drop the laptop", command = i_sad_again)
button20.pack()
code = tk.PhotoImage(file = "code.png")
replit = tk.PhotoImage(file = "replit.png")
laptop = tk.PhotoImage(file = "laptop.png")
dropped_laptop = tk.PhotoImage(file = "dropped_laptop.png")
happy = tk.PhotoImage(file = "happy.png")
sad = tk.PhotoImage(file = "sad.png")


tk.mainloop()



