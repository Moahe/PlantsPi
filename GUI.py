
try:
    import Tkinter as tkinter

except(ModuleNotFoundError):
    import tkinter as tkinter

tk = tkinter.Tk()


def GUI(strinfo):

    print(strinfo)
    strtemp = strinfo['dd']['temperature']
    strlux = strinfo['dd']['light']

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

    label_lux = tkinter.Label(tk, text=""+str(strlux), bg="white", fg='grey')
    label_temp = tkinter.Label(tk, text="" + str(strtemp)+" °C", bg="white", fg='grey')

    def inc():
        korv = open('num.txt', 'r+')
        i = korv.read()
        korv.close()
        korv = open('num.txt', 'w+')

        y = int(i)
        print(y)
        y = y+1
        if y > 11:
            y = 1

        korv.write((y.__str__()))
        forgetalllabels()
        korv.close()
        return y

    def inc2(y):

        korv = open('num.txt', 'w+')

        korv.write((y.__str__()))
        korv.close()

        return y

    def callback():
        quit()

    def pic():

        #img2 = tkinter.PhotoImage(file="1.png")
        filename.configure(file=("%i.png" % inc()))

    def forgetalllabels():
        label_lux.place_forget()
        label_temp.place_forget()

    def tempclick():
        forgetalllabels()
        filename.configure(file=("%i.png" % inc2(6)))
        label_temp.config(font=("Press Start 2P", 25))
        label_temp.place(x=573, y=130, height=50, width=150)

    def sunclick():
        forgetalllabels()
        filename.configure(file=("%i.png" % inc2(9)))
        label_lux.config(font=("Pontano Sans", 25))
        label_lux.place(x=573, y=130, height=50, width=150)

    def waterclick():
        forgetalllabels()
        filename.configure(file=("%i.png" % inc2(4)))





    b = tkinter.Button(tk, command=pic, bg="white", height = 63, width = 63, borderwidth=0)
    poly = tkinter.PhotoImage(file="Polygonl.png")
    b.config(image = poly)
    b.place(x=38, y=385)

    b2 = tkinter.Button(tk, command=pic, bg="white", height = 63, width = 63, borderwidth=0)
    poly2 = tkinter.PhotoImage(file="Polygonr.png")
    b2.config(image = poly2)
    b2.place(x=200, y=385)

    b3 = tkinter.Button(tk, command=tempclick, bg="white", height = 63, width = 63, borderwidth=0)
    poly3 = tkinter.PhotoImage(file="temp.png")
    b3.config(image = poly3)
    b3.place(x=614, y=380)

    b4 = tkinter.Button(tk, command=sunclick, bg="white", height = 63, width = 63, borderwidth=0)
    poly4 = tkinter.PhotoImage(file="sun.png")
    b4.config(image = poly4)
    b4.place(x=695, y=380)

    b5 = tkinter.Button(tk, command=waterclick, bg="#3EBAFF", height = 63, width = 63, borderwidth=0)
    poly5 = tkinter.PhotoImage(file="Group.png")
    b5.config(image = poly5)
    b5.place(x=535, y=380)
    """
    label2 = tkinter.Label(tk, text="")
    label2.config(text="Hejhopp korv"+str(strtemp))
    label2.config(font=("MS", 44))
    label2.place(x=200, y=385)"""

    label2 = tkinter.Label(tk, text="I am easy \n to take care\n of and need\n partial shade and \neven temperatures."
                                    "\nI am well known \n for being able\n to purify\n the air\n", bg="white")
    label2.config(font=("Pontano Sans", 15))
    label2.place(x=30, y=60, height=320, width=249)

    label3 = tkinter.Label(tk, text="I am a Dracaena Rikki", bg="white")
    label3.place(x=50, y=50, height=30, width=200)
    label3.config(font=("Pontano Sans", 15))
    """
    """

    tk.mainloop()

