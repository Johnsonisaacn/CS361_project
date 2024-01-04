from tkinter import *
from tkinter import ttk
from random import randint
import ttkbootstrap as tb
import zmq
from tkinter.messagebox import askyesno

#zeromq setup
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


#window
root = Tk()
root.title('Flashcards')
root.geometry("800x800")
style = tb.Style(theme='solar')

def confirm_exit():
    answer = askyesno(title="Exit", message="Do you really want to exit?")
    if answer:
        root.destroy()

def message():
    global pop
    pop = Toplevel(root)
    pop.title("Welcome!")
    pop.geometry("500x500")
    pop.config(bg="white")
    message = """Welcome to my flashcard app! To use, you can flip 
    through the cards using the buttons or the left and right keys.
    Using the right key or NEXT button lets you scroll through the
    flashcard deck at random. Using the left key or PREV button 
    lets you view previous cards that you've already viewed, but
    if you go forward through the deck again, it will be at random.
    You can also use enter or the FLIP button to flip the card and 
    view the English or German language translation."""
    pop_label = Label(pop, text=message, bg="white", font=("helvetica", 12))
    pop_label.pack(pady=10)

words = [
    (("sein"), ("to be")),
    (("kommen"), ("to come")),
    (("Ich heiße..."), ("My name is...")),
    (("Bitte"), ("Please/you're welcome")),
    (("Was?"), ("What?")),
    (("Warum?"), ("Why?")),
    (("Woher?"), ("Where?")),
    (("Tag"), ("Day")),
    (("Woch"), ("Week")),
    (("Monat"), ("Month")),
    (("Jahr"), ("Year")),
]
#get a count of our words list
count = len(words)
#array to go back 10 cards
previous_indices = []

def prev():
    if len(previous_indices) < 1:
        return
    front_word.config(text=words[previous_indices[len(previous_indices) - 1]][0])
    previous_indices.pop(len(previous_indices) - 1)

def key_prev(event):
    if event:
        prev()

def flip():
    global front_back
    if front_back == "front":
        front_back = "back"
        front_word.config(text=words[rand_word][1])

    else:
        front_back = "front"
        front_word.config(text=words[rand_word][0])
    message = "play sound"
    socket.send_string(message)
    message = socket.recv()


def key_flip(event):
    if event:
        flip()

def next():
    #create random selection
    global front_back
    front_back = "front"
    global rand_word
    rand_word = randint(0, count-1)
    #update previous indices to go back through cards
    if len(previous_indices) >= 10:
        previous_indices.pop(0)
    previous_indices.append(rand_word)
    #update label with German Word
    front_word.config(text=words[rand_word][0])

def key_next(event):
    if event:
        next()

#create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

prev_button = Button(button_frame, font=("Helvetica", 18), text="Prev", command=prev)
root.bind('<Any-KeyPress-Left>', key_prev)
prev_button.grid(row=0, column=0)

flip_button = Button(button_frame, font=("Helvetica", 18), text="Flip", command=flip)
root.bind('<Any-KeyPress-Return>', key_flip)
flip_button.grid(row=0, column=1, padx=20)

next_button = Button(button_frame, font=("Helvetica", 18), text="Next", command=next)
root.bind('<Any-KeyPress-Right>', key_next)
next_button.grid(row=0, column=2)

front_word = Label(root, justify="center", wraplength=800,  text="", font=("Helvetica", 120))
front_word.pack(pady=10)

#run at program start
next()
message()

root.protocol("WM_DELETE_WINDOW", confirm_exit)
root.mainloop()
