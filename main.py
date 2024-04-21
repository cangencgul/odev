import tkinter as tk
import numpy as np
import os
img = []
def resimleri_al():
    resim_adlari = []
    resim_klasoru = os.getcwd()+"\\resimler"
    for resim in os.listdir(resim_klasoru):
        resim_adlari.append(resim)
    for i in range(len(resim_adlari)):
        os.chdir(resim_klasoru)
        img.append(tk.PhotoImage(file="%s"%(resim_adlari[i])))

root = tk.Tk()
resimleri_al()

img2 = tk.PhotoImage(file="wire2.gif")
img3 = tk.PhotoImage(file="resistor.GIF")
img4 = tk.PhotoImage(file="wire4.GIF")
img5 = tk.PhotoImage(file="wire3.GIF")
img6 = tk.PhotoImage(file="wire6.GIF")
img7 = tk.PhotoImage(file="wire5.GIF")

frame1 = tk.Frame(root)
frame1.grid(row=0,column=0)
frame11 = tk.Frame(frame1)
frame11.grid(row=1,column=2)
frame12 = tk.Frame(frame1)
frame12.grid(row=2,column=5)
frame13 = tk.Frame(frame1)
frame13.grid(row=5,column=2)
frame14 = tk.Frame(frame1)
frame14.grid(row=7,column=4)
frame15 = tk.Frame(frame1)
frame15.grid(row=5,column=6)
frame16 = tk.Frame(frame1)
frame16.grid(row=1,column=6)
frame2 = tk.Frame(root)
frame2.grid(row=0,column=1)
buton1 = tk.Label(frame1,image=img6).grid(row=0,column=0)
buton2 = tk.Label(frame1,image=img[15]).grid(row=0,column=1)
buton4 = tk.Label(frame1,image=img[15]).grid(row=0,column=3)
buton5 = tk.Label(frame1,image=img[12]).grid(row=0,column=4)
buton6 = tk.Label(frame1,image=img[15]).grid(row=0,column=5)
buton7 = tk.Label(frame1,image=img[15]).grid(row=0,column=6)
buton8 = tk.Label(frame1,image=img[15]).grid(row=0,column=7)
buton9 = tk.Label(frame1,image=img7).grid(row=0,column=8)
buton10 = tk.Label(frame1,image=img5).grid(row=8,column=0)
buton11 = tk.Label(frame1,image=img[15]).grid(row=8,column=1)
buton12 = tk.Label(frame1,image=img[15]).grid(row=8,column=2)
buton13 = tk.Label(frame1,image=img[15]).grid(row=8,column=3)
buton14= tk.Label(frame1,image=img[15]).grid(row=8,column=4)
buton15 = tk.Label(frame1,image=img[15]).grid(row=8,column=5)
buton16 = tk.Label(frame1,image=img[15]).grid(row=8,column=6)
buton17 = tk.Label(frame1,image=img[15]).grid(row=8,column=7)
buton18 = tk.Label(frame1,image=img4).grid(row=8,column=8)
buton19 = tk.Label(frame1,image=img[11]).grid(row=4,column=0)
buton20 = tk.Label(frame1,image=img[15]).grid(row=4,column=1)
buton21 = tk.Label(frame1,image=img[15]).grid(row=4,column=2)
buton22 = tk.Label(frame1,image=img[15]).grid(row=4,column=3)
buton23 = tk.Label(frame1,image=img[7]).grid(row=4,column=4)
buton24 = tk.Label(frame1,image=img[15]).grid(row=4,column=5)
buton25 = tk.Label(frame1,image=img[15]).grid(row=4,column=6)
buton26 = tk.Label(frame1,image=img[15]).grid(row=4,column=7)
buton27 = tk.Label(frame1,image=img[10]).grid(row=4,column=8)
buton28 = tk.Label(frame1,image=img2).grid(row=1,column=0)
buton29 = tk.Label(frame1,image=img2).grid(row=2,column=0)
buton30 = tk.Label(frame1,image=img2).grid(row=3,column=0)
buton31 = tk.Label(frame1,image=img2).grid(row=5,column=0)
buton32 = tk.Label(frame1,image=img2).grid(row=6,column=0)
buton33 = tk.Label(frame1,image=img2).grid(row=7,column=0)
buton34 = tk.Label(frame1,image=img2).grid(row=1,column=4)
buton35 = tk.Label(frame1,image=img2).grid(row=2,column=4)
buton36 = tk.Label(frame1,image=img2).grid(row=3,column=4)
buton37 = tk.Label(frame1,image=img2).grid(row=1,column=8)
buton38 = tk.Label(frame1,image=img2).grid(row=2,column=8)
buton39 = tk.Label(frame1,image=img2).grid(row=3,column=8)
buton40 = tk.Label(frame1,image=img2).grid(row=5,column=8)
buton41 = tk.Label(frame1,image=img2).grid(row=6,column=8)
buton42 = tk.Label(frame1,image=img2).grid(row=7,column=8)
buton = []
spin_deger = []
spin_veri = []
satir_1 = [0,0,0]
satir_2 = [0,0,0]
satir_3 = [0,0,0]
sonuc = [0,0,0]
ek_denklem_1 = [0,0,0]
ek_denklem_1_s = [0]
ek_denklem_2 = [0,0,0]
ek_denklem_2_s = [0]
ek_denklem_3 = [0,0,0]
ek_denklem_3_s = [0]
ek_denklem_4 = [0,0,0]
ek_denklem_4_s = [0]
ek_denklem_5 = [0,0,0]
ek_denklem_5_s = [0]
ek_denklem_6 = [0,0,0]
ek_denklem_6_s = [0]
for i in range(1,8):
    buton.append(i)
    spin_deger.append(tk.IntVar())
    spin_veri.append(tk.StringVar())

def func1(i,x,y):
    global birinci,ikinci,ucuncu,dorduncu,besinci,altinci
    if y == 2:
        buton[i].config(image=img[9],bg="green")
    else:
        buton[i].config(image=img3,bg="green")
    if y==1:
        birinci = x
    elif y==2:
        ikinci = x
    elif y==3:
        ucuncu = x
    elif y==4:
        dorduncu = x
    elif y==5:
        besinci = x
    elif y==6:
        altinci = x
def func2(i,x,y):
    global birinci,ikinci,ucuncu,dorduncu,besinci,altinci
    if y == 2:
        buton[i].config(image=img[13],bg="green")
    else:
        buton[i].config(image=img[14],bg="green")
    if y==1:
        birinci = x
    elif y==2:
        ikinci = x
    elif y==3:
        ucuncu = x
    elif y==4:
        dorduncu = x
    elif y==5:
        besinci = x
    elif y==6:
        altinci = x
def func3(i,x,y):
    global birinci,ikinci,ucuncu,dorduncu,besinci,altinci
    if y == 2:
        buton[i].config(image=img[4],bg="green")
    else:
        buton[i].config(image=img[6],bg="green")
    if y==1:
        birinci = x
    elif y==2:
        ikinci = x
    elif y==3:
        ucuncu = x
    elif y==4:
        dorduncu = x
    elif y==5:
        besinci = x
    elif y==6:
        altinci = x
def func5(i,x,y):
    global birinci,ikinci,ucuncu,dorduncu,besinci,altinci
    if y == 2:
        buton[i].config(image=img[0],bg="green")
    else:
        buton[i].config(image=img[1],bg="green")
    if y==1:
        birinci = x
    elif y==2:
        ikinci = x
    elif y==3:
        ucuncu = x
    elif y==4:
        dorduncu = x
    elif y==5:
        besinci = x
    elif y==6:
        altinci = x
def func4(i,x,y):
    global birinci,ikinci,ucuncu,dorduncu,besinci,altinci
    if y == 2:
        buton[i].config(image=img[2],bg="green")
    else:
        buton[i].config(image=img[3],bg="green")
    if y==1:
        birinci = x
    elif y==2:
        ikinci = x
    elif y==3:
        ucuncu = x
    elif y==4:
        dorduncu = x
    elif y==5:
        besinci = x
    elif y==6:
        altinci = x

def matris():
    a = [0,0,0]
    b = [0,0,0]
    c = [0,0,0]
    a_s = [0]
    b_s = [0]
    c_s = [0]

    if birinci ==3 or birinci == 5:
        a  = ek_denklem_1
        a_s = ek_denklem_1_s
        if altinci ==3 or altinci ==5:
            b = ek_denklem_6
            b_s = ek_denklem_6_s
            if dorduncu ==3 or dorduncu ==5:
                c = ek_denklem_4
                c_s = ek_denklem_4_s
            elif ucuncu ==3 or ucuncu == 5:
                c = ek_denklem_3
                c_s = ek_denklem_3_s
            elif besinci ==3 or besinci == 5:
                c = ek_denklem_5
                c_s = ek_denklem_5_s
            else:
                c = satir_3
                c_s[0] = sonuc[2]
        elif ikinci  == 3 or ikinci ==5:
            b = ek_denklem_2
            b_s = ek_denklem_2_s
            if dorduncu ==3 or dorduncu ==5:
                c = ek_denklem_4
                c_s = ek_denklem_4_s
            elif ucuncu ==3 or ucuncu == 5:
                c = ek_denklem_3
                c_s = ek_denklem_3_s
            elif besinci ==3 or besinci == 5:
                c = ek_denklem_5
                c_s = ek_denklem_5_s
            else:
                c= satir_3
                c_s[0] = sonuc[2]
        elif ucuncu == 3 or ucuncu == 5:
            b = ek_denklem_3
            b_s = ek_denklem_3_s
            if ikinci ==3 or ikinci ==5:
                c = ek_denklem_2
                c_s = ek_denklem_2_s
            elif altinci ==3 or altinci == 5:
                c = ek_denklem_6
                c_s = ek_denklem_6_s
            elif besinci ==3 or besinci == 5:
                c = ek_denklem_5
                c_s = ek_denklem_5_s
            else:
                c = satir_2
                c_s[0] = sonuc[1]
        elif dorduncu == 3 or dorduncu ==5:
            b = ek_denklem_4
            b_s = ek_denklem_4_s
            if ikinci ==3 or ikinci ==5:
                c = ek_denklem_2
                c_s = ek_denklem_2_s
            elif altinci ==3 or altinci == 5:
                c = ek_denklem_6
                c_s = ek_denklem_6_s
            elif besinci ==3 or besinci == 5:
                c = ek_denklem_5
                c_s = ek_denklem_5_s
            else:
                c = satir_2
                c_s[0] = sonuc[1]
        elif besinci == 3 or besinci == 5:
            b = ek_denklen_5
            b_s = ek_denklen_5_s
            if ikinci ==3 or ikinci ==5:
                c = ek_denklem_2
                c_s = ek_denklem_2_s
            elif altinci ==3 or altinci == 5:
                c = ek_denklem_6
                c_s = ek_denklem_6_s
            elif dorduncu ==3 or dorduncu == 5:
                c = ek_denklem_4
                c_s = ek_denklem_4_s
            elif ucuncu == 3 or ucuncu == 5:
                c = ek_denklem_3
                c_s = ek_denklem_3_s
            else:
                c[0] = satir_2[0]+satir_3[0]
                c[1] = satir_2[1]+satir_3[1]
                c[2] = satir_2[2]+satir_3[2]
                c_s[0] =sonuc[1]+sonuc[2]
        else:
            b = satir_2
            b_s[0] = sonuc[1]
            c = satir_3
            c_s[0] = sonuc[2]
    elif altinci == 3 or altinci ==5:
        a= ek_denklem_6
        a_s = ek_denklem_6_s
        if ikinci == 3 or ikinci ==5:
            b= ek_denklem_2
            b_s = ek_denklem_2_s
            if dorduncu ==3 or dorduncu ==5:
                c = ek_denklem_4
                c_s = ek_denklem_4_s
            elif ucuncu ==3 or ucuncu == 5:
                c = ek_denklem_3
                c_s = ek_denklem_3_s
            elif besinci ==3 or besinci == 5:
                c = ek_denklem_5
                c_s = ek_denklem_5_s
            else: 
                c = satir_3
                c_s[0] = sonuc[2]
        elif besinci == 3 or besinci ==5:
            b= ek_denklem_5
            b_s = ek_denklem_5_s
            if birinci == 3 or birinci == 5:
                c= ek_denklem_1
                c_s = ek_denklem_1_s
            elif ikinci ==3 or ikinci ==5:
                c= ek_denklem_2
                c_s = ek_denklem_2_s
            elif ucuncu ==3 or ucuncu ==5:
                c = ek_denklem_3
                c_s = ek_denklem_3_s
            else:
                c= satir_1
                c_s[0] = sonuc[0]
        elif dorduncu == 3 or dorduncu == 5:
            b= ek_denklem_4
            b_s = ek_denklem_4_s
            if birinci == 3 or birinci == 5:
                c= ek_denklem_1
                c_s = ek_denklem_1_s
            elif ikinci ==3 or ikinci ==5:
                c= ek_denklem_2
                c_s = ek_denklem_2_s
            elif ucuncu ==3 or ucuncu ==5:
                c = ek_denklem_3
                c_s = ek_denklem_3_s
            else:
                c= satir_1
                c_s[0] = sonuc[0]
        elif ucuncu == 3 or ucuncu == 5:
            b= ek_denklem_3
            b_s = ek_denklem_3_s
            c[0] = satir_1[0]+satir_3[0]
            c[1] = satir_1[1]+satir_3[1]
            c[2] = satir_1[2]+satir_3[2]
            c_s[0] = sonuc[0]+sonuc[2]
        else:
            b= satir_1
            b_s[0] = sonuc[0]
            c= satir_3
            c_s[0] = sonuc[2]
    elif ikinci == 3 or ikinci == 5:
        a= ek_denklem_2
        a_s = ek_denklem_2_s
        if dorduncu ==3 or dorduncu ==5:
            b = ek_denklem_4
            b_s = ek_denklem_4_s
        elif ucuncu ==3 or ucuncu == 5:
            b = ek_denklem_3
            b_s = ek_denklem_3_s
        elif besinci ==3 or besinci == 5:
            b = ek_denklem_5
            b_s = ek_denklem_5_s
        else:
            b = satir_3
            b_s[0] = sonuc[2]
            c[0] = satir_1[0]+satir_2[0]
            c[1] = satir_1[1]+satir_2[1]
            c[2] = satir_1[2]+satir_2[2]
            c_s[0] = sonuc[0]+sonuc[1]
    elif ucuncu ==3 or ucuncu == 5:
        a = ek_denklem_3
        a_s = ek_denklem_3_s
        if besinci == 3 or besinci == 5:
            b = ek_denklem_5
            b_s = ek_denklem_5_s
        elif dorduncu == 3 or dorduncu == 3:
            b = ek_denklem_4
            b_s = ek_denklem_4_s
        else:
            b= satir_2
            b_s[0] = sonuc[1]
            c[0] = satir_1[0]+satir_3[0]
            c[1] = satir_1[1]+satir_3[1]
            c[2] = satir_1[2]+satir_3[2]
            c_s[0] = sonuc[0]+sonuc[2]
    elif dorduncu ==3 or dorduncu == 5:
        a = ek_denklem_4
        a_s = ek_denklem_4_s
        if besinci ==3 or besinci ==5:
            b= ek_denklem_5
            b_s = ek_denklem_5_s
        else:
            b=satir_1
            b_s[0] =sonuc[0]
            c=satir_2
            c_s[0] = sonuc[1]
    elif besinci == 3 or besinci ==5:
        a = ek_denklem_5
        a_s = ek_denklem_5_s
        b = satir_1
        b_s = satir_1_s
        c[0] = satir_2[0]+satir_3[0]
        c[1] = satir_2[1]+satir_3[1]
        c[2] = satir_2[2]+satir_3[2]
        c_s[0] = sonuc[1]+ sonuc[2]
    else:
        a = satir_1
        a_s[0] = sonuc[0]
        b = satir_2
        b_s[0] = sonuc[1]
        c = satir_3
        c_s[0] = sonuc[2]
    m = np.matrix([a,
                   b,
                   c])
    n = m.I
    j = np.matrix([a_s,
                   b_s,
                   c_s])
    f = n * j
    aaaaa=tk.Label(frame2,text="%s,i_loop_1,%s"%(a,a_s))
    aaaaa.grid(row=0,column=0)
    bbbbb = tk.Label(frame2, text="%s,i_loop_2,%s" % (b, b_s))
    bbbbb.grid(row=1,column=0)
    ccccc = tk.Label(frame2, text="%s,i_loop_3,%s" % (c, c_s))
    ccccc.grid(row=2,column=0)
    cevap1 = tk.Label(frame2, text="eleman1 akimi:%s"%(f[0]))
    cevap1.grid(row=3,column=0)
    cevap2 = tk.Label(frame2, text="eleman2 akimi:%s"%(f[0]-f[1]))
    cevap2.grid(row=4,column=0)
    cevap3 = tk.Label(frame2, text="eleman3 akimi:%s"%(f[2]-f[0]))
    cevap3.grid(row=5, column=0)
    cevap4 = tk.Label(frame2, text="eleman4 akimi:%s"%(f[2]))
    cevap4.grid(row=6, column=0)
    cevap5 = tk.Label(frame2, text="eleman5 akimi:%s"%(f[2]-f[1]))
    cevap5.grid(row=7, column=0)
    cevap6 = tk.Label(frame2, text="eleman6 akimi:%s"%(f[1]))
    cevap6.grid(row=8, column=0)

            
def deger_alma():
    for i in range(3):
        satir_1[i]=0
        satir_2[i]=0
        satir_3[i]=0
        sonuc[i]=0
        ek_denklem_1[i]=0
        ek_denklem_1_s[0]=0
        ek_denklem_2[i]=0
        ek_denklem_2_s[0]=0
        ek_denklem_3[i]=0
        ek_denklem_3_s[0]=0
        ek_denklem_4[i]=0
        ek_denklem_4_s[0]=0
        ek_denklem_5[i]=0
        ek_denklem_5_s[0]=0
        ek_denklem_6[i]=0
        ek_denklem_6_s[0]=0
    if birinci == 1:
        satir_1[0] += spin_deger[1].get()
        if spin_veri[1].get() != "-":
            print("eleman1 hatali")
    elif birinci == 2:
        sonuc[0] -= spin_deger[1].get()
        if spin_veri[1].get() != "-":
            print("eleman1 hatali")
    elif birinci == 3:
        ek_denklem_1[0] += 1
        ek_denklem_1_s[0] += spin_deger[1].get()
        if spin_veri[1].get() != "-":
            print("eleman1 hatali")
    elif birinci == 5:
        ek_denklem_1[0] += 1
        if spin_veri[1].get() == "-":
            print("eleman1 hatali")
        elif spin_veri[1].get() == "i2":
            ek_denklem_1[0] -= spin_deger[1].get()
            ek_denklem_1[1] += spin_deger[1].get()
        elif spin_veri[1].get() == "i3":
            ek_denklem_1[2] -= spin_deger[1].get()
            ek_denklem_1[0] += spin_deger[1].get()
        elif spin_veri[1].get() == "i4":
            ek_denklem_1[2] += spin_deger[1].get()
        elif spin_veri[1].get() == "i5":
            ek_denklem_1[2] -= spin_deger[1].get()
            ek_denklem_1[1] += spin_deger[1].get()
        elif spin_veri[1].get() == "i6":
            ek_denklem_1[1] -= spin_deger[1].get()
    elif birinci == 4:
        if spin_veri[1].get() == "i2":
            satir_1[0] += spin_deger[1].get()
            satir_1[1] -= spin_deger[1].get()
        if spin_veri[1].get() == "i3":
            satir_1[2] += spin_deger[1].get()
            satir_1[0] -= spin_deger[1].get()
        if spin_veri[1].get() == "i4":
            satir_1[2] -= spin_deger[1].get()
        if spin_veri[1].get() == "i5":
            satir_1[2] += spin_deger[1].get()
            satir_1[1] -= spin_deger[1].get()
        if spin_veri[1].get() == "i6":
            satir_1[1] += spin_deger[1].get()
    if ikinci == 1:
        satir_1[0] += spin_deger[2].get()
        satir_1[1] -= spin_deger[2].get()
        satir_2[0] -= spin_deger[2].get()
        satir_2[1] += spin_deger[2].get()
        if spin_veri[2].get() != "-":
            print("eleman2 hatali")
    elif ikinci == 2:
        sonuc[0] -= spin_deger[2].get()
        sonuc[1] += spin_deger[2].get()
        if spin_veri[2].get() != "-":
            print("eleman2 hatali")
    elif ikinci == 3:
        ek_denklem_2[0] += 1
        ek_denklem_2[1] -= 1
        ek_denklem_2_s[0] += spin_deger[2].get()
        if spin_veri[2].get() != "-":
            print("eleman2 hatali")
    elif ikinci == 5:
        if spin_veri[2] == "-":
            print("eleman2 hatali")
            ek_denklem_2[0] += 1
            ek_denklem_2[1] -= 1
        elif spin_veri[2].get() == "i1":
            ek_denklem_2[0] -= spin_deger[2].get()
        elif spin_veri[2].get() == "i3":
            ek_denklem_2[2] -= spin_deger[2].get()
            ek_denklem_2[0] += spin_deger[2].get()
        elif spin_veri[2].get() == "i4":
            ek_denklem_2[2] += spin_deger[2].get()
        elif spin_veri[2].get() == "i5":
            ek_denklem_2[2] -= spin_deger[2].get()
            ek_denklem_2[1] += spin_deger[2].get()
        elif spin_veri[2].get() == "i6":
            ek_denklem_2[1] -= spin_deger[2].get()
    elif ikinci == 4:
        if spin_veri[2].get() == "i1":
            satir_1[0] += spin_deger[2].get()
            satir_2[0] -= spin_deger[2].get()
        if spin_veri[2].get() == "i3":
            satir_1[2] += spin_deger[2].get()
            satir_2[2] -= spin_deger[2].get()
            satir_1[0] -= spin_deger[2].get()
            satir_2[0] += spin_deger[2].get()
        if spin_veri[2].get() == "i4":
            satir_1[2] -= spin_deger[2].get()
            satir_2[2] += spin_deger[2].get()
        if spin_veri[2].get() == "i5":
            satir_1[2] += spin_deger[2].get()
            satir_1[1] -= spin_deger[2].get()
            satir_2[2] -= spin_deger[2].get()
            satir_2[1] += spin_deger[2].get()
        if spin_veri[2].get() == "i6":
            satir_1[1] += spin_deger[2].get()
            satir_2[1] -= spin_deger[2].get()
    if ucuncu == 1:
        satir_1[0] += spin_deger[3].get()
        satir_1[2] -= spin_deger[3].get()
        satir_3[0] -= spin_deger[3].get()
        satir_3[2] += spin_deger[3].get()
        if spin_veri[3].get() != "-":
            print("eleman3 hatali")
    elif ucuncu == 2:
        sonuc[0] += spin_deger[3].get()
        sonuc[2] -= spin_deger[3].get()
        if spin_veri[3].get() != "-":
            print("eleman3 hatali")
    elif ucuncu == 3:
        ek_denklem_3[0] -= 1
        ek_denklem_3[2] += 1
        ek_denklem_3_s[0] += spin_deger[3].get()
        if spin_veri[3].get() != "-":
            print("eleman3 hatali")
    elif ucuncu == 5:
        ek_denklem_3[2] += 1
        ek_denklem_3[0] -= 1
        if spin_veri[3].get() == "-":
            print("eleman3 hatali")
        elif spin_veri[3].get() == "i1":
            ek_denklem_3[0] -= spin_deger[3].get()
        elif spin_veri[3].get() == "i2":
            ek_denklem_3[0] -= spin_deger[3].get()
            ek_denklem_3[1] += spin_deger[3].get()
        elif spin_veri[3].get() == "i4":
            ek_denklem_3[2] += spin_deger[3].get()
        elif spin_veri[3].get() == "i5":
            ek_denklem_3[2] -= spin_deger[3].get()
            ek_denklem_3[1] += spin_deger[3].get()
        elif spin_veri[3].get() == "i6":
            ek_denklem_3[1] -= spin_deger[3].get()
    elif ucuncu == 4:
        if spin_veri[3].get() == "i1":
            satir_1[0] -= spin_deger[3].get()
            satir_3[0] += spin_deger[3].get()
        if spin_veri[3].get() == "i2":
            satir_1[0] -= spin_deger[3].get()
            satir_1[1] += spin_deger[3].get()
            satir_3[0] += spin_deger[3].get()
            satir_3[1] -= spin_deger[3].get()
        if spin_veri[3].get() == "i4":
            satir_1[2] += spin_deger[3].get()
            satir_3[2] -= spin_deger[3].get()
        if spin_veri[3].get() == "i5":
            satir_1[2] -= spin_deger[3].get()
            satir_1[1] += spin_deger[3].get()
            satir_3[2] += spin_deger[3].get()
            satir_3[1] -= spin_deger[3].get()
        if spin_veri[3].get() == "i6":
            satir_1[1] -= spin_deger[3].get()
            satir_3[1] += spin_deger[3].get()
    if dorduncu == 1:
        satir_3[2] += spin_deger[4].get()
        if spin_veri[4].get() != "-":
            print("eleman4 hatali")
    elif dorduncu == 2:
        sonuc[2] += spin_deger[4].get()
        if spin_veri[4].get() != "-":
            print("eleman4 hatali")
    elif dorduncu == 3:
        ek_denklem_4[2] -= 1
        ek_denklem_4_s[0] += spin_deger[4].get()
        if spin_veri[4].get() != "-":
            print("eleman4 hatali")
    elif dorduncu == 5:
        ek_denklem_4[2] -= 1
        if spin_veri[4].get() == "-":
            print("eleman4 hatali")
        elif spin_veri[4].get() == "i1":
            ek_denklem_4[0] -= spin_deger[4].get()
        elif spin_veri[4].get() == "i2":
            ek_denklem_4[0] -= spin_deger[4].get()
            ek_denklem_4[1] += spin_deger[4].get()
        elif spin_veri[4].get() == "i3":
            ek_denklem_4[2] -= spin_deger[4].get()
            ek_denklem_4[0] += spin_deger[4].get()
        elif spin_veri[4].get() == "i5":
            ek_denklem_4[2] -= spin_deger[4].get()
            ek_denklem_4[1] += spin_deger[4].get()
        elif spin_veri[4].get() == "i6":
            ek_denklem_4[1] -= spin_deger[4].get()
    elif dorduncu == 4:
        if spin_veri[4].get() == "i1":
            satir_3[0] -= spin_deger[4].get()
        if spin_veri[4].get() == "i2":
            satir_3[0] -= spin_deger[4].get()
            satir_3[1] += spin_deger[4].get()
        if spin_veri[4].get() == "i3":
            satir_3[2] -= spin_deger[4].get()
            satir_3[0] += spin_deger[4].get()
        if spin_veri[4].get() == "i5":
            satir_3[2] -= spin_deger[4].get()
            satir_3[1] += spin_deger[4].get()
        if spin_veri[4].get() == "i6":
            satir_3[1] -= spin_deger[4].get()
    if besinci == 1:
        satir_3[2] += spin_deger[5].get()
        satir_3[1] -= spin_deger[5].get()
        satir_2[2] -= spin_deger[5].get()
        satir_2[1] += spin_deger[5].get()
        if spin_veri[5].get() != "-":
            print("eleman5 hatali")
    elif besinci == 2:
        sonuc[2] -= spin_deger[5].get()
        sonuc[1] += spin_deger[5].get()
        if spin_veri[5].get() != "-":
            print("eleman5 hatali")
    elif besinci == 3:
        ek_denklem_5[1] -= 1
        ek_denklem_5[2] += 1
        ek_denklem_5_s[0] += spin_deger[5].get()
        if spin_veri[5].get() != "-":
            print("eleman5 hatali")
    elif besinci == 5:
        ek_denklem_5[2] += 1
        ek_denklem_5[1] -= 1
        if spin_veri[5].get() == "-":
            print("eleman5 hatali")
        elif spin_veri[5].get() == "i1":
            ek_denklem_5[0] -= spin_deger[5].get()
        elif spin_veri[5].get() == "i2":
            ek_denklem_5[0] -= spin_deger[5].get()
            ek_denklem_5[1] += spin_deger[5].get()
        elif spin_veri[5].get() == "i3":
            ek_denklem_5[2] -= spin_deger[5].get()
            ek_denklem_5[0] += spin_deger[5].get()
        elif spin_veri[5].get() == "i4":
            ek_denklem_5[2] += spin_deger[5].get()
        elif spin_veri[5].get() == "i6":
            ek_denklem_5[1] -= spin_deger[5].get()
    elif besinci == 4:
        if spin_veri[5].get() == "i1":
            satir_2[0] -= spin_deger[5].get()
            satir_3[0] += spin_deger[5].get()
        if spin_veri[5].get() == "i2":
            satir_2[0] -= spin_deger[5].get()
            satir_2[1] += spin_deger[5].get()
            satir_3[0] += spin_deger[5].get()
            satir_3[1] -= spin_deger[5].get()
        if spin_veri[5].get() == "i3":
            satir_2[2] -= spin_deger[5].get()
            satir_2[0] += spin_deger[5].get()
            satir_3[2] += spin_deger[5].get()
            satir_3[0] -= spin_deger[5].get()
        if spin_veri[5].get() == "i4":
            satir_2[2] += spin_deger[5].get()
            satir_3[2] -= spin_deger[5].get()
        if spin_veri[5].get() == "i6":
            satir_2[1] -= spin_deger[5].get()
            satir_3[1] += spin_deger[5].get()
    if altinci == 1:
        satir_2[1] += spin_deger[6].get()
        if spin_veri[6].get() != "-":
            print("eleman6 hatali")
    elif altinci == 2:
        sonuc[1] += spin_deger[6].get()
        if spin_veri[6].get() != "-":
            print("eleman6 hatali")
    elif altinci == 3:
        ek_denklem_6[1] += 1
        ek_denklem_6_s[0] += spin_deger[6].get()
        if spin_veri[6].get() != "-":
            print("eleman6 hatali")
    elif altinci == 5:
        ek_denklem_6[1] += 1
        if spin_veri[6].get() == "-":
            print("eleman6 hatali")
        elif spin_veri[6].get() == "i1":
            ek_denklem_6[0] -= spin_deger[6].get()
        elif spin_veri[6].get() == "i2":
            ek_denklem_6[0] -= spin_deger[6].get()
            ek_denklem_6[1] += spin_deger[6].get()
        elif spin_veri[6].get() == "i3":
            ek_denklem_6[2] -= spin_deger[6].get()
            ek_denklem_6[0] += spin_deger[6].get()
        elif spin_veri[6].get() == "i4":
            ek_denklem_6[2] += spin_deger[6].get()
        elif spin_veri[6].get() == "i5":
            ek_denklem_6[2] -= spin_deger[6].get()
            ek_denklem_6[1] += spin_deger[6].get()
    elif altinci == 4:
        if spin_veri[6].get() == "i1":
            satir_2[0] += spin_deger[6].get()
        if spin_veri[6].get() == "i2":
            satir_2[0] += spin_deger[6].get()
            satir_2[1] -= spin_deger[6].get()
        if spin_veri[6].get() == "i3":
            satir_2[2] += spin_deger[6].get()
            satir_2[0] -= spin_deger[6].get()
        if spin_veri[6].get() == "i5":
            satir_2[2] += spin_deger[6].get()
            satir_2[1] -= spin_deger[6].get()
        if spin_veri[6].get() == "i1":
            satir_2[1] += spin_deger[6].get()
def devre_olustur():
    i=1
    buton[i] = tk.Menubutton(frame1,image=img[15],bg="red")
    buton[i].menu = tk.Menu (buton[i], tearoff=0)
    buton[i]["menu"]= buton[i].menu
    buton[i].menu.add_command(image=img3,command= lambda:func1(1,1,1))
    buton[i].menu.add_command(image=img[14],command= lambda:func2(1,2,1))
    buton[i].menu.add_command(image=img[6],command= lambda:func3(1,3,1))
    buton[i].menu.add_command(image=img[3],command= lambda:func4(1,4,1))
    buton[i].menu.add_command(image=img[1],command= lambda:func5(1,5,1))
    buton[i].grid(row=0,column=2)
    spinbox1=tk.Spinbox(frame11,from_=-10,to=10,textvariable=spin_deger[1],width=1)
    spinbox1.pack(side = tk.LEFT)
    spinbox11=tk.Spinbox(frame11,values=("-","i2","i3","i4","i5","i6"),textvariable=spin_veri[1],width=2)
    spinbox11.pack(side = tk.LEFT)
    i=2
    buton[i] = tk.Menubutton(frame1,image=img2,bg="red")
    buton[i].menu = tk.Menu (buton[i], tearoff=0)
    buton[i]["menu"]= buton[i].menu
    buton[i].menu.add_command(image=img3,command= lambda:func1(2,1,2))
    buton[i].menu.add_command(image=img[14],command= lambda:func2(2,2,2))
    buton[i].menu.add_command(image=img[6],command= lambda:func3(2,3,2))
    buton[i].menu.add_command(image=img[3],command= lambda:func4(2,4,2))
    buton[i].menu.add_command(image=img[1],command= lambda:func5(2,5,2))
    buton[i].grid(row=2,column=4)
    spinbox2=tk.Spinbox(frame12,from_=-10,to=10,textvariable=spin_deger[2],width=2)
    spinbox2.pack(side = tk.LEFT)
    spinbox22=tk.Spinbox(frame12,values=("-","i1","i3","i4","i5","i6"),textvariable=spin_veri[2],width=2)
    spinbox22.pack(side = tk.LEFT)
    i=3
    buton[i] = tk.Menubutton(frame1,image=img[15],bg="red")
    buton[i].menu = tk.Menu (buton[i], tearoff=0)
    buton[i]["menu"]= buton[i].menu
    buton[i].menu.add_command(image=img3,command= lambda:func1(3,1,3))
    buton[i].menu.add_command(image=img[14],command= lambda:func2(3,2,3))
    buton[i].menu.add_command(image=img[6],command= lambda:func3(3,3,3))
    buton[i].menu.add_command(image=img[3],command= lambda:func4(3,4,3))
    buton[i].menu.add_command(image=img[1],command= lambda:func5(3,5,3))
    buton[i].grid(row=4,column=2)
    spinbox3=tk.Spinbox(frame13,from_=-10,to=10,textvariable=spin_deger[3],width=2)
    spinbox3.pack(side = tk.LEFT)
    spinbox33=tk.Spinbox(frame13,values=("-","i1","i2","i4","i5","i6"),textvariable=spin_veri[3],width=2)
    spinbox33.pack(side = tk.LEFT)
    i=4
    buton[i] = tk.Menubutton(frame1,image=img[15],bg="red")
    buton[i].menu = tk.Menu (buton[i], tearoff=0)
    buton[i]["menu"]= buton[i].menu
    buton[i].menu.add_command(image=img3,command= lambda:func1(4,1,4))
    buton[i].menu.add_command(image=img[14],command= lambda:func2(4,2,4))
    buton[i].menu.add_command(image=img[6],command= lambda:func3(4,3,4))
    buton[i].menu.add_command(image=img[3],command= lambda:func4(4,4,4))
    buton[i].menu.add_command(image=img[1],command= lambda:func5(4,5,4))
    buton[i].grid(row=8,column=4)
    spinbox4=tk.Spinbox(frame14,from_=-10,to=10,textvariable=spin_deger[4],width=2)
    spinbox4.pack(side = tk.LEFT)
    spinbox44=tk.Spinbox(frame14,values=("-","i1","i2","i3","i5","i6"),textvariable=spin_veri[4],width=2)
    spinbox44.pack(side = tk.LEFT)
    i=5
    buton[i] = tk.Menubutton(frame1,image=img[15],bg="red")
    buton[i].menu = tk.Menu (buton[i], tearoff=0)
    buton[i]["menu"]= buton[i].menu
    buton[i].menu.add_command(image=img3,command= lambda:func1(5,1,5))
    buton[i].menu.add_command(image=img[14],command= lambda:func2(5,2,5))
    buton[i].menu.add_command(image=img[6],command= lambda:func3(5,3,5))
    buton[i].menu.add_command(image=img[3],command= lambda:func4(5,4,5))
    buton[i].menu.add_command(image=img[1],command= lambda:func5(5,5,5))
    buton[i].grid(row=4,column=6)
    spinbox5=tk.Spinbox(frame15,from_=-10,to=10,textvariable=spin_deger[5],width=2)
    spinbox5.pack(side = tk.LEFT)
    spinbox55=tk.Spinbox(frame15,values=("-","i1","i2","i3","i4","i6"),textvariable=spin_veri[5],width=2)
    spinbox55.pack(side = tk.LEFT)
    i=6
    buton[i] = tk.Menubutton(frame1,image=img[15],bg="red")
    buton[i].menu = tk.Menu (buton[i], tearoff=0)
    buton[i]["menu"]= buton[i].menu
    buton[i].menu.add_command(image=img3,command= lambda:func1(6,1,6))
    buton[i].menu.add_command(image=img[14],command= lambda:func2(6,2,6))
    buton[i].menu.add_command(image=img[6],command= lambda:func3(6,3,6))
    buton[i].menu.add_command(image=img[4],command= lambda:func4(6,4,6))
    buton[i].menu.add_command(image=img[1],command= lambda:func5(6,5,6))
    buton[i].grid(row=0,column=6)
    spinbox6=tk.Spinbox(frame16,from_=-10,to=10,textvariable=spin_deger[6],width=2)
    spinbox6.pack(side = tk.LEFT)
    spinbox66=tk.Spinbox(frame16,values=("-","i1","i2","i3","i4","i5"),textvariable=spin_veri[6],width=2)
    spinbox66.pack(side = tk.LEFT)
devre_olustur()
def kontrol():
    deger_alma()
kontrol=tk.Button(frame2,text="deger al",command=kontrol)
kontrol.grid(row=9,column=1)
kontrol2= tk.Button(frame2,text="coz",command=matris)
kontrol2.grid(row=10,column=1)

root.mainloop()
