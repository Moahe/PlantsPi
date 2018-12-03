
import tkinter


def GUI(str, strinfo):
    tk = tkinter.Tk()
    tk.resizable(0, 0)
    tk.configure(background='white')
    #tk.attributes('-fullscreen', True)
    tk.title("PlantPy")
    tk.geometry("800x480")
    lbltitle = tkinter.Label(tk, text=str, font=("Arial Bold", 30), background="white")
    lbltitle.place(x = 250, y= 120)
    lblinfo = tkinter.Label(tk, text=strinfo, font=("Arial Bold", 15), background="white")
    lblinfo.place(x=250, y=240)
    back = tkinter.Frame(master=tk, bg='white')
    tk.mainloop()

