from tkinter import

def typing (event):
    key = event.widget["text"]
    if key == "=":
result.set(round(eval(result.get())), 2)
    else:
        if len(result.get())< 8:
            result.set(result.get()+key)

 def mouse_enter(event):
    event.widget.config(background="lightblue", foreground="black")
