
try:
    import Tkinter as tkinter

except(ModuleNotFoundError):
    import tkinter as tkinter

tk = tkinter.Tk()

def GUI(str, strinfo):


    tk.resizable(0, 0)
    tk.configure(background='white')
    #tk.attributes('-fullscreen', True)
    tk.title("PlantPy")
    tk.geometry("800x480")
    """
    lbltitle = tkinter.Label(tk, text=str, font=("Arial Bold", 30), background="white")
    lbltitle.place(x=230, y=100)
    lblinfo = tkinter.Label(tk, text=strinfo, font=("Arial Bold", 15), background="white")
    lblinfo.place(x=250, y=240)
    b.bind()
    back = tkinter.Frame(master=tk, bg='white')
    """
    C = tkinter.Canvas(tk, bg="blue", height=800, width=480)
    filename = tkinter.PhotoImage(file="1.png")
    background_label = tkinter.Label(tk, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    def inc():
        korv = open('num.txt', 'r+')
        i = korv.read()
        korv.close()
        korv = open('num.txt', 'w+')

        y = int(i)
        print(y)
        y = y+1
        if y > 10:
            y = 1

        korv.write((y.__str__()))
        korv.close()
        return y

    def callback():
        quit()

    def pic():

        #img2 = tkinter.PhotoImage(file="1.png")
        filename.configure(file=("%i.png" % inc()))

    b = tkinter.Button(tk, text="    ", command=pic, bg="white")

    b.place(x=760, y=440)
    tk.mainloop()

