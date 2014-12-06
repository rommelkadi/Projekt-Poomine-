from tkinter import *
from random import *




def destroy():
    root.destroy()


def kuva_uus_sõna():
     
    global varjatud_sõna
    f = open("sõnadelist.txt")
    read = f.readlines()
    f.close()
    x = randint(0,len(read)-1)
    

    global sõna
    sõna = read[x]
    sõna = sõna.strip("\n")
    

    varjatud_sõna = StringVar()
    varjatud_sõna.set((len(sõna)*"_ "))
    
    kuva_aknas = Label(topframe, textvariable = varjatud_sõna, font=("Helvetica", 20), width=15).grid(row=5, column=6)


    
    print(sõna)
    
    return

### Üritan teha ühe ainsa callbacki nuppude jaoks

counter = 0

def callback(täht):

#Kustuta need hiljem ära! see ei toimi nii. Aga võiks toimida, hetkel idee oli see, et iga tähe jaoks eraldi funktsioon teha, või siis kasutada sõnastikku, panna täht selleks võtmesõnaks ja nupp vasteks {} sisse
 #   if täht =="a":
 #       A_nupp.config(state="disabled")
    

    global counter
    if counter < 7:
              
        if täht in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == täht:
                    i +=[indeksid-1]
                    
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)

            for o in i:
                nonoh[o*2] = täht.upper()
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)


#Kui sõna on õigesti vastatud kuvab ära arvasid! See replace värk on vajalik sest muidu ta ei saa aru et need on samasugused kuna meil nonohis on tühikud vahel
            if (nonoh.replace(' ', '')) == sõna.upper():
                võitsid = Label(topframe, text="Ära arvasid!", font=("Helvetica", 20)).grid(row=9, column=6)


        else:
            print("Buu, seda tahte pole sonas!")
            counter +=1
            print(counter)


    else:
        #print("MÄNGLÄBI")
        mang_labi = Label(topframe, text="Mäng Läbi!", font=("Helvetica", 20)).grid(row=9, column=6)
        photo = PhotoImage(file="sticky_figure.png")
        w = Label(topframe, image=photo)
        w.photo = photo
        w.grid(row=12, column=6)
                    





root = Tk()
root.geometry("500x400")

topframe=Frame(root)
topframe.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

    


menu= Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Uus mäng", command=kuva_uus_sõna)
subMenu.add_command(label="Exit", command= destroy)
subMenu.add_separator()




A_nupp = Button(bottomframe, text="A",command = lambda täht="a": callback(täht),height=2, width=2).grid(row=0, column=2, padx=2, pady=2)
B_nupp = Button(bottomframe, text="B",command = lambda täht="b": callback(täht),height=2, width=2).grid(row=0, column=3, padx=2, pady=2)
C_nupp = Button(bottomframe, text="C",command = lambda täht="c": callback(täht),height=2, width=2).grid(row=0, column=4, padx=2, pady=2)
D_nupp = Button(bottomframe, text="D",command = lambda täht="d": callback(täht),height=2, width=2).grid(row=0, column=5, padx=2, pady=2)
E_nupp = Button(bottomframe, text="E",command = lambda täht="e": callback(täht),height=2, width=2).grid(row=0, column=6, padx=2, pady=2)
F_nupp = Button(bottomframe, text="F",command = lambda täht="f": callback(täht),height=2, width=2).grid(row=0, column=7, padx=2, pady=2)
G_nupp = Button(bottomframe, text="G",command = lambda täht="g": callback(täht),height=2, width=2).grid(row=0, column=8, padx=2, pady=2)
H_nupp = Button(bottomframe, text="H",command = lambda täht="h": callback(täht),height=2, width=2).grid(row=0, column=9, padx=2, pady=2)
I_nupp = Button(bottomframe, text="I",command = lambda täht="i": callback(täht),height=2, width=2).grid(row=0, column=10, padx=2, pady=2)
J_nupp = Button(bottomframe, text="J",command = lambda täht="j": callback(täht),height=2, width=2).grid(row=0, column=11, padx=2, pady=2)
K_nupp = Button(bottomframe, text="K",command = lambda täht="k": callback(täht),height=2, width=2).grid(row=0, column=12, padx=2, pady=2)
L_nupp = Button(bottomframe, text="L",command = lambda täht="l": callback(täht),height=2, width=2).grid(row=1, column=0, padx=2, pady=2)
M_nupp = Button(bottomframe, text="M",command = lambda täht="m": callback(täht),height=2, width=2).grid(row=1, column=1, padx=2, pady=2)
N_nupp = Button(bottomframe, text="N",command = lambda täht="n": callback(täht),height=2, width=2).grid(row=1, column=2, padx=2, pady=2)
O_nupp = Button(bottomframe, text="O",command = lambda täht="o": callback(täht),height=2, width=2).grid(row=1, column=3, padx=2, pady=2)
P_nupp = Button(bottomframe, text="P",command = lambda täht="p": callback(täht),height=2, width=2).grid(row=1, column=4, padx=2, pady=2)
R_nupp = Button(bottomframe, text="R",command = lambda täht="r": callback(täht),height=2, width=2).grid(row=1, column=5, padx=2, pady=2)
S_nupp = Button(bottomframe, text="S",command = lambda täht="s": callback(täht),height=2, width=2).grid(row=1, column=6, padx=2, pady=2)
T_nupp = Button(bottomframe, text="T",command = lambda täht="t": callback(täht),height=2, width=2).grid(row=1, column=7, padx=2, pady=2)
U_nupp = Button(bottomframe, text="U",command = lambda täht="u": callback(täht),height=2, width=2).grid(row=1, column=8, padx=2, pady=2)
V_nupp = Button(bottomframe, text="V",command = lambda täht="v": callback(täht),height=2, width=2).grid(row=1, column=9, padx=2, pady=2)
Õ_nupp = Button(bottomframe, text="Õ",command = lambda täht="õ": callback(täht),height=2, width=2).grid(row=1, column=10, padx=2, pady=2)
Ä_nupp = Button(bottomframe, text="Ä",command = lambda täht="ä": callback(täht),height=2, width=2).grid(row=1, column=11, padx=2, pady=2)
Ö_nupp = Button(bottomframe, text="Ö",command = lambda täht="ö": callback(täht),height=2, width=2).grid(row=1, column=12, padx=2, pady=2)
Ü_nupp = Button(bottomframe, text="Ü",command = lambda täht="ü": callback(täht),height=2, width=2).grid(row=1, column=13, padx=2, pady=2)


root.mainloop()
