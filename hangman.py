from tkinter import *
from random import *




def destroy():
    root.destroy()

def kuva_uus_sona():
    kuva_skoor()
    global counter
    counter=7
    kuva_counter()

    Label(topframe, text="", width=20, height=2).grid(row=9, column=6)
    Label(topframe, text="", width=20, height=13 ).grid(row=12, column=6)


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
    kuva_nupud()
        
    print(sõna)
    
    return



def kuva_counter():
    Label(bottomframe, text="Misses left: %.f" % counter, font=("Helvetica", 12) ).grid(row=0, column=0, columnspan=3)

def kuva_skoor():
    Label(bottomframe, text="Punkte: %.f" % skoor, font=("Helvetica", 12) ).grid(row=1, column=0, columnspan=3)
    
def kuva_parim_skoor():
    global skoor
    global parim_skoor
    Label(bottomframe, text="Parim skoor: %.f" % parim_skoor, font=("Helvetica, 10")).grid(row=0, column=13, columnspan=15)
    if skoor > parim_skoor:
        parim_skoor = skoor
        Label(bottomframe, text="Parim skoor: %.f" % parim_skoor, font=("Helvetica, 10")).grid(row=0, column=13, columnspan=15)

def voitsid():
    võitsid = Label(topframe, text="Ära arvasid!", font=("Helvetica", 20)).grid(row=9, column=6)
    photo = PhotoImage(file="happy_sticky.png")
    w = Label(topframe, image=photo)
    w.photo = photo
    w.grid(row=12, column=6)
    global skoor
    skoor += counter
    kuva_skoor()

def kaotasid():
    kuva_skoor()
    global counter
    counter =0
    kuva_counter()
    mang_labi = Label(topframe, text="Mäng Läbi!", font=("Helvetica", 20)).grid(row=9, column=6)
    photo = PhotoImage(file="sticky_figure.png")
    w = Label(topframe, image=photo)
    w.photo = photo
    w.grid(row=12, column=6)
    varjatud_sõna.set(sõna.upper())
    Label(topframe, textvariable = varjatud_sõna, font=("Helvetica", 20), width=15).grid(row=5, column=6)
    kuva_parim_skoor()
    global skoor
    skoor = 0




root = Tk()
root.geometry("500x450")

topframe=Frame(root)
topframe.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)



counter = 7
kuva_counter()
skoor = 0

def callback(täht):
    

    global counter
    if counter > 1:

        dis_nupud(täht)
              
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
            
            

            if (nonoh.replace(' ', '')) == sõna.upper():
                voitsid()
                

        else:
            print("Buu, seda tahte pole sonas!")
            counter -=1
            kuva_counter()
            
            


    else:
        kaotasid()


                
def kuva_nupud():
    A_nupp = Button(bottomframe, text="A",command = lambda täht="a": callback(täht),height=2, width=2).grid(row=4, column=2, padx=2, pady=2)
    B_nupp = Button(bottomframe, text="B",command = lambda täht="b": callback(täht),height=2, width=2).grid(row=4, column=3, padx=2, pady=2)
    C_nupp = Button(bottomframe, text="C",command = lambda täht="c": callback(täht),height=2, width=2).grid(row=4, column=4, padx=2, pady=2)
    D_nupp = Button(bottomframe, text="D",command = lambda täht="d": callback(täht),height=2, width=2).grid(row=4, column=5, padx=2, pady=2)
    E_nupp = Button(bottomframe, text="E",command = lambda täht="e": callback(täht),height=2, width=2).grid(row=4, column=6, padx=2, pady=2)
    F_nupp = Button(bottomframe, text="F",command = lambda täht="f": callback(täht),height=2, width=2).grid(row=4, column=7, padx=2, pady=2)
    G_nupp = Button(bottomframe, text="G",command = lambda täht="g": callback(täht),height=2, width=2).grid(row=4, column=8, padx=2, pady=2)
    H_nupp = Button(bottomframe, text="H",command = lambda täht="h": callback(täht),height=2, width=2).grid(row=4, column=9, padx=2, pady=2)
    I_nupp = Button(bottomframe, text="I",command = lambda täht="i": callback(täht),height=2, width=2).grid(row=4, column=10, padx=2, pady=2)
    J_nupp = Button(bottomframe, text="J",command = lambda täht="j": callback(täht),height=2, width=2).grid(row=4, column=11, padx=2, pady=2)
    K_nupp = Button(bottomframe, text="K",command = lambda täht="k": callback(täht),height=2, width=2).grid(row=4, column=12, padx=2, pady=2)
    L_nupp = Button(bottomframe, text="L",command = lambda täht="l": callback(täht),height=2, width=2).grid(row=5, column=0, padx=2, pady=2)
    M_nupp = Button(bottomframe, text="M",command = lambda täht="m": callback(täht),height=2, width=2).grid(row=5, column=1, padx=2, pady=2)
    N_nupp = Button(bottomframe, text="N",command = lambda täht="n": callback(täht),height=2, width=2).grid(row=5, column=2, padx=2, pady=2)
    O_nupp = Button(bottomframe, text="O",command = lambda täht="o": callback(täht),height=2, width=2).grid(row=5, column=3, padx=2, pady=2)
    P_nupp = Button(bottomframe, text="P",command = lambda täht="p": callback(täht),height=2, width=2).grid(row=5, column=4, padx=2, pady=2)
    R_nupp = Button(bottomframe, text="R",command = lambda täht="r": callback(täht),height=2, width=2).grid(row=5, column=5, padx=2, pady=2)
    S_nupp = Button(bottomframe, text="S",command = lambda täht="s": callback(täht),height=2, width=2).grid(row=5, column=6, padx=2, pady=2)
    T_nupp = Button(bottomframe, text="T",command = lambda täht="t": callback(täht),height=2, width=2).grid(row=5, column=7, padx=2, pady=2)
    U_nupp = Button(bottomframe, text="U",command = lambda täht="u": callback(täht),height=2, width=2).grid(row=5, column=8, padx=2, pady=2)
    V_nupp = Button(bottomframe, text="V",command = lambda täht="v": callback(täht),height=2, width=2).grid(row=5, column=9, padx=2, pady=2)
    Õ_nupp = Button(bottomframe, text="Õ",command = lambda täht="õ": callback(täht),height=2, width=2).grid(row=5, column=10, padx=2, pady=2)
    Ä_nupp = Button(bottomframe, text="Ä",command = lambda täht="ä": callback(täht),height=2, width=2).grid(row=5, column=11, padx=2, pady=2)
    Ö_nupp = Button(bottomframe, text="Ö",command = lambda täht="ö": callback(täht),height=2, width=2).grid(row=5, column=12, padx=2, pady=2)
    Ü_nupp = Button(bottomframe, text="Ü",command = lambda täht="ü": callback(täht),height=2, width=2).grid(row=5, column=13, padx=2, pady=2)

kuva_nupud()

def dis_nupud(täht):
            if täht == "a":
                A_nupp= Button(bottomframe, text="A",height=2, width=2, state = DISABLED).grid(row=4, column=2, padx=2, pady=2)
            elif täht == "b":
                B_nupp = Button(bottomframe, text="B",height=2, width=2, state = DISABLED).grid(row=4, column=3, padx=2, pady=2)
            elif täht == "c":
                C_nupp = Button(bottomframe, text="C",height=2, width=2, state = DISABLED).grid(row=4, column=4, padx=2, pady=2)
            elif täht == "d":
                D_nupp = Button(bottomframe, text="D",height=2, width=2, state = DISABLED).grid(row=4, column=5, padx=2, pady=2)
            elif täht == "e":
                E_nupp = Button(bottomframe, text="E",height=2, width=2, state = DISABLED).grid(row=4, column=6, padx=2, pady=2)
            elif täht == "f":
                F_nupp = Button(bottomframe, text="F",height=2, width=2, state = DISABLED).grid(row=4, column=7, padx=2, pady=2)
            elif täht == "g":
                G_nupp= Button(bottomframe, text="G",height=2, width=2, state = DISABLED).grid(row=4, column=8, padx=2, pady=2)
            elif täht == "h":
                H_nupp = Button(bottomframe, text="H",height=2, width=2, state = DISABLED).grid(row=4, column=9, padx=2, pady=2)
            elif täht == "i":
                I_nupp = Button(bottomframe, text="I",height=2, width=2, state = DISABLED).grid(row=4, column=10, padx=2, pady=2)
            elif täht == "j":
                J_nupp = Button(bottomframe, text="J",height=2, width=2, state = DISABLED).grid(row=4, column=11, padx=2, pady=2)
            elif täht == "k":
                K_nupp = Button(bottomframe, text="K",height=2, width=2, state = DISABLED).grid(row=4, column=12, padx=2, pady=2)
            elif täht == "l":
                L_nupp = Button(bottomframe, text="L",height=2, width=2, state = DISABLED).grid(row=5, column=0, padx=2, pady=2)
            elif täht == "m":
                M_nupp= Button(bottomframe, text="M",height=2, width=2, state = DISABLED).grid(row=5, column=1, padx=2, pady=2)
            elif täht == "n":
                N_nupp = Button(bottomframe, text="N",height=2, width=2, state = DISABLED).grid(row=5, column=2, padx=2, pady=2)
            elif täht == "o":
                O_nupp = Button(bottomframe, text="O",height=2, width=2, state = DISABLED).grid(row=5, column=3, padx=2, pady=2)
            elif täht == "p":
                P_nupp = Button(bottomframe, text="P",height=2, width=2, state = DISABLED).grid(row=5, column=4, padx=2, pady=2)
            elif täht == "r":
                R_nupp = Button(bottomframe, text="R",height=2, width=2, state = DISABLED).grid(row=5, column=5, padx=2, pady=2)
            elif täht == "s":
                S_nupp = Button(bottomframe, text="S",height=2, width=2, state = DISABLED).grid(row=5, column=6, padx=2, pady=2)
            elif täht == "t":
                T_nupp= Button(bottomframe, text="T",height=2, width=2, state = DISABLED).grid(row=5, column=7, padx=2, pady=2)
            elif täht == "u":
                U_nupp = Button(bottomframe, text="U",height=2, width=2, state = DISABLED).grid(row=5, column=8, padx=2, pady=2)
            elif täht == "v":
                V_nupp = Button(bottomframe, text="V",height=2, width=2, state = DISABLED).grid(row=5, column=9, padx=2, pady=2)
            elif täht == "õ":
                Õ_nupp = Button(bottomframe, text="Õ",height=2, width=2, state = DISABLED).grid(row=5, column=10, padx=2, pady=2)
            elif täht == "ä":
                Ä_nupp = Button(bottomframe, text="Ä",height=2, width=2, state = DISABLED).grid(row=5, column=11, padx=2, pady=2)
            elif täht == "ö":
                Ö_nupp = Button(bottomframe, text="Ö",height=2, width=2, state = DISABLED).grid(row=5, column=12, padx=2, pady=2)           
            elif täht == "ü":
                Ü_nupp = Button(bottomframe, text="Ü",height=2, width=2, state = DISABLED).grid(row=5, column=13, padx=2, pady=2)           

menu= Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Uus sõna", command=kuva_uus_sona)
subMenu.add_command(label="Exit", command= destroy)
subMenu.add_separator()


       
def arvan_sona_korraga():
    arvatud_sõna = arva_sona.get().upper()
    if arvatud_sõna == sõna.upper():
        varjatud_sõna.set(arvatud_sõna)
        voitsid()
    else:
        kuva_counter()
        kaotasid()


def kuva_sisestuskast():
    if var.get()==1:
        sisestuskast = Entry(bottomframe, textvariable=arva_sona).grid(row=2, column=3, columnspan=5)
        arva_nupp = Button(bottomframe, text="Arvan",command = arvan_sona_korraga).grid(row=2, column=6, columnspan=8)
    else:

        Label(bottomframe,text="", width=30, height=2).grid(row=2, column=3, columnspan=8)


 
var = IntVar()
Checkbutton(bottomframe, text="Tean:", variable=var, command=kuva_sisestuskast).grid(row=2, column=0, columnspan=2)

arva_sona= StringVar()

parim_skoor = 0
kuva_parim_skoor()






root.mainloop()
