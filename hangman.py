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
    
  
    
#teen nupule A funktsiooni
def a_käsk():
    try:
        
        if "a" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "a":
                    i +=[indeksid-1]
                    
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)

            for o in i:
                nonoh[o*2] = "A"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
                    

    except:
        print("Böö, seda tähte polnud")

def b_käsk():
    try:
        
        if "b" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "b":
                    i +=[indeksid-1]
                    
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)

            for o in i:
                nonoh[o*2] = "B"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
    except:
        print("Böö, seda tähte polnud")



def e_käsk():
    try:
        if "e" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "e":
                    i += [indeksid-1]
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)
            for o in i:
                nonoh[o*2] = "E"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
    except:
        print("Böö, seda tähte polnud")

def i_käsk():
    try:
        if "i" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "i":
                    i += [indeksid-1]
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)
            for o in i:
                nonoh[o*2] = "I"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
    except:
        print("Böö, seda tähte polnud")

def k_käsk():
    try:
        if "k" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "k":
                    i += [indeksid-1]
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)
            for o in i:
                nonoh[o*2] = "K"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
    except:
        print("Böö, seda tähte polnud")


def o_käsk():
    try:
        if "o" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "o":
                    i += [indeksid-1]
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)
            for o in i:
                nonoh[o*2] = "O"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
    except:
        print("Böö, seda tähte polnud")

def s_käsk():
    try:
        if "s" in sõna:
            sõne = list(sõna)
            indeksid = 0
            i = []

            for el in sõne:
                indeksid +=1
                if el == "s":
                    i += [indeksid-1]
            nonoh = varjatud_sõna.get()
            nonoh = list(nonoh)
            for o in i:
                nonoh[o*2] = "S"
            nonoh = "".join(nonoh)
            varjatud_sõna.set(nonoh)
    except:
        print("Böö, seda tähte polnud")
        
    



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



A_nupp = Button(bottomframe, text="A",command = a_käsk).pack(side=LEFT)
B_nupp = Button(bottomframe, text="B",command = b_käsk).pack(side=LEFT)
C_nupp = Button(bottomframe, text="C").pack(side=LEFT)
D_nupp = Button(bottomframe, text="D").pack(side=LEFT)
E_nupp = Button(bottomframe, text="E",command = e_käsk).pack(side=LEFT)
F_nupp = Button(bottomframe, text="F").pack(side=LEFT)
G_nupp = Button(bottomframe, text="G").pack(side=LEFT)
H_nupp = Button(bottomframe, text="H").pack(side=LEFT)
I_nupp = Button(bottomframe, text="I",command = i_käsk).pack(side=LEFT)
J_nupp = Button(bottomframe, text="J").pack(side=LEFT)
K_nupp = Button(bottomframe, text="K",command = k_käsk).pack(side=LEFT)
L_nupp = Button(bottomframe, text="L").pack(side=LEFT)
M_nupp = Button(bottomframe, text="M").pack(side=LEFT)
N_nupp = Button(bottomframe, text="N").pack(side=LEFT)
O_nupp = Button(bottomframe, text="O",command = o_käsk).pack(side=LEFT)
P_nupp = Button(bottomframe, text="P").pack(side=LEFT)
R_nupp = Button(bottomframe, text="R").pack(side=LEFT)
S_nupp = Button(bottomframe, text="S",command = s_käsk).pack(side=LEFT)
T_nupp = Button(bottomframe, text="T").pack(side=LEFT)
U_nupp = Button(bottomframe, text="U").pack(side=LEFT)
V_nupp = Button(bottomframe, text="V").pack(side=LEFT)
Õ_nupp = Button(bottomframe, text="Õ").pack(side=LEFT)
Ä_nupp = Button(bottomframe, text="Ä").pack(side=LEFT)
Ö_nupp = Button(bottomframe, text="Ö").pack(side=LEFT)
Ü_nupp = Button(bottomframe, text="Ü").pack(side=LEFT)


root.mainloop()
