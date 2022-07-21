import tkinter as tk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.exit)
        self.label = tk.Label(text='Hello Cruel World...')
        self.label.pack()

        self.button = tk.Button(text='Exit', command=self.exit)
        self.button.pack()
    
    def exit(self):
        self.label['text'] = 'Goodbye Cruel World...'
        self.button['text'] = 'Please Wait...'
        self.button['state'] = 'disabled'
        self.after(2000, self.destroy)

window = Window()
window.mainloop()