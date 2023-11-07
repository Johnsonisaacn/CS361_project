from tkinter import *
from random import randint
import ttkbootstrap as tb

root = Tk()
root.title('Practice German Language Flashcards')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("700x500")
style = tb.Style(theme='vapor')


words = [
    (("Guten Tag"), ("Good day")),
    (("Auf Wiedersehen"), ("Goodbye")),
    (("Danke"), ("Thank you")),
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

def next():
    global hinter, hint_count
    #clear screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    hinter = ""
    hint_count = 0
    #create random selection
    global rand_word
    rand_word = randint(0, count-1)
    #update label with German Word
    german_word.config(text=words[rand_word][0])

def answer():
    if my_entry.get().lower() == words[rand_word][1].lower():
        answer_label.config(text=f"Correct! {words[rand_word][0]} is {words[rand_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[rand_word][0]} is not {my_entry.get()}")

#keep track of hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[rand_word][1]):
        hinter = hinter + words[rand_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1
    else:
        pass


german_word = Label(root, text="", font=("Helvetica", 36))
german_word.pack(pady=20)

answer_label = Label(root, text="", font=("Helvetica", 18))
answer_label.pack(pady=10)

#create hint label
hint_label = Label(root, font=("helvetica", 19), text="")
hint_label.pack(pady=10)

my_entry = Entry(root, font=("Helvetica", 36))
my_entry.pack(pady=10, padx=20)

#create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, font=("Helvetica", 18),  text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, font=("Helvetica", 18), text="Next", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, font=("Helvetica", 18), text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)



#run at program start
next()


root.mainloop()
