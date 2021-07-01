import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.value = 100;
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self)
        self.label['text'] = 'Введите здоровье бойца'
        self.label.pack()
        
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        self.button = tk.Button(self)
        self.button['text'] = 'Ввод'
        self.button['command'] = self.change_value
        self.button.pack()

        self.quit = tk.Button(self, text='Подтвердить', command=self.master.destroy)
        self.quit.pack()

    def change_value(self):
        self.value = self.entry.get()
        self.label['text'] = 'Здоровье установлено: {}'.format(self.value)
