from tkinter import *
from random import *



def destroy():
    root.destroy()

def kuva_uus_sõna():
    #kuva_aknas1 = False

    #if kuva_aknas1 == True:
    #    topframe.destroy()
        
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
    
    kuva_aknas = Label(topframe, textvariable = varjatud_sõna).pack(side=LEFT)
    kuva_aknas1 = True
    
    print(sõna)
    
    return

### Üritan teha ühe ainsa callbacki nuppude jaoks

counter = 0

def callback(täht):
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
        if täht not in sõna:
            print("Böö, seda tähte polnud")
            counter +=1
    else:
        print("MÄNGLÄBI")
                    
        

    






root = Tk()
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



A_nupp = Button(bottomframe, text="A",command = lambda täht="a": callback(täht)).pack(side=LEFT)
B_nupp = Button(bottomframe, text="B",command = lambda täht="b": callback(täht)).pack(side=LEFT)
C_nupp = Button(bottomframe, text="C",command = lambda täht="c": callback(täht)).pack(side=LEFT)
D_nupp = Button(bottomframe, text="D",command = lambda täht="d": callback(täht)).pack(side=LEFT)
E_nupp = Button(bottomframe, text="E",command = lambda täht="e": callback(täht)).pack(side=LEFT)
F_nupp = Button(bottomframe, text="F",command = lambda täht="f": callback(täht)).pack(side=LEFT)
G_nupp = Button(bottomframe, text="G",command = lambda täht="g": callback(täht)).pack(side=LEFT)
H_nupp = Button(bottomframe, text="H",command = lambda täht="h": callback(täht)).pack(side=LEFT)
I_nupp = Button(bottomframe, text="I",command = lambda täht="i": callback(täht)).pack(side=LEFT)
J_nupp = Button(bottomframe, text="J",command = lambda täht="j": callback(täht)).pack(side=LEFT)
K_nupp = Button(bottomframe, text="K",command = lambda täht="k": callback(täht)).pack(side=LEFT)
L_nupp = Button(bottomframe, text="L",command = lambda täht="l": callback(täht)).pack(side=LEFT)
M_nupp = Button(bottomframe, text="M",command = lambda täht="m": callback(täht)).pack(side=LEFT)
N_nupp = Button(bottomframe, text="N",command = lambda täht="n": callback(täht)).pack(side=LEFT)
O_nupp = Button(bottomframe, text="O",command = lambda täht="o": callback(täht)).pack(side=LEFT)
P_nupp = Button(bottomframe, text="P",command = lambda täht="p": callback(täht)).pack(side=LEFT)
R_nupp = Button(bottomframe, text="R",command = lambda täht="r": callback(täht)).pack(side=LEFT)
S_nupp = Button(bottomframe, text="S",command = lambda täht="s": callback(täht)).pack(side=LEFT)
T_nupp = Button(bottomframe, text="T",command = lambda täht="t": callback(täht)).pack(side=LEFT)
U_nupp = Button(bottomframe, text="U",command = lambda täht="u": callback(täht)).pack(side=LEFT)
V_nupp = Button(bottomframe, text="V",command = lambda täht="v": callback(täht)).pack(side=LEFT)
Õ_nupp = Button(bottomframe, text="Õ",command = lambda täht="õ": callback(täht)).pack(side=LEFT)
Ä_nupp = Button(bottomframe, text="Ä",command = lambda täht="ä": callback(täht)).pack(side=LEFT)
Ö_nupp = Button(bottomframe, text="Ö",command = lambda täht="ö": callback(täht)).pack(side=LEFT)
Ü_nupp = Button(bottomframe, text="Ü",command = lambda täht="ü": callback(täht)).pack(side=LEFT)


root.mainloop()
