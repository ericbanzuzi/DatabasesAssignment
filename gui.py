import tkinter as tk
from tkterminal import Terminal

window = tk.Tk()

terminal = Terminal(pady=5, padx=5)
terminal.shell = True
terminal.pack(expand=True, fill='both')
terminal.run_command('python terminal.py','y')

window.mainloop()