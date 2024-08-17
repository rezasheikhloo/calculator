from tkinter import

def typing (event):
    key = event.widget["text"]
    if key == "=":
result.set(round(eval(result.get())), 2)
    else:
        if len(result)