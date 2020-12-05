import tkinter as tk
from time import strftime

window = tk.Tk()
window.title('Clock')
window.configure(bg='purple')
window.resizable(0, 0)


def time():
    hr = strftime("%H")
    mi = strftime("%M")
    se = strftime("%S")
    meridian = strftime("%p")
    string = f'{hr}:{mi}:{se}\n{meridian}'
    lbl.configure(text=string)
    lbl.after(1000, time)


lbl = tk.Label(window, font=('Laksaman', 40, 'bold'),
               background='purple',
               foreground='white')
lbl.pack(padx=15, pady=(0, 10), expand=True)

time()
window.mainloop()
