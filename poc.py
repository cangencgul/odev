import tkinter as tk
import numpy as np
import os
import csv
ana_klasor = os.getcwd()
resim_klasoru = os.getcwd()+"\\resimler"

eleman = [] #oluşturulan her devre elemanı buraya eklenir
baglantılar = [] #elemanları baglayan linelar buraya eklenir
img_dic = {} #resimler klasorundeki resimlerin isimleri key, tkinter photo image objectleri value olarak buraya saklanır
bilgiler ={"eleman_secili_mi": None, "secili_eleman": None, "kacinci": 0}
kordinatlar = {"x":None, "y":None} # fare hareketi ile sürekli olarak değeri değişiyor

class Circuit_Element:
    def __init__(self, e_number, e_type, e_x, e_y):
        self.no = e_number
        self.type = e_type
        self.center_x = e_x
        self.center_y = e_y
class line:
    def __init__(self, first, second):
        self.first = first
        self.second = second
def chosen_element(chosen):
    kacinci = bilgiler.get("kacinci")
    canvas.itemconfig(fare_resim, image = img_dic[chosen + ".GIF"])
    bilgiler.update({"eleman_secili_mi": True, "secili_eleman": chosen + ".GIF", "kacinci": kacinci + 1})


line_cord ={"x1": None, "x2":None, "y1": None, "y2":None}
def press_left(self):
    x = kordinatlar.get("x")
    y = kordinatlar.get("y")
    for i in range(len(eleman)):
        if eleman[i].center_y - 24 < y < eleman[i].center_y + 24:
            if eleman[i].center_x < x < eleman[i].center_x + 24:
                if line_cord.get("x1") is None:
                    line_cord.update({"x1": eleman[i].center_x + 24, "y1": eleman[i].center_y})
                else:
                    x1 = line_cord.get("x1")
                    y1 = line_cord.get("y1")
                    x2 = eleman[i].center_x + 24
                    y2 = eleman[i].center_y
                    canvas.create_line(x1, y1, x2, y2, width = 2)
                    line_cord.update({"x1": None, "x2":None, "y1": None, "y2":None})

            elif eleman[i].center_x - 24 < x < eleman[i].center_x:
                if line_cord.get("x1") is None:
                    line_cord.update({"x1": eleman[i].center_x - 24, "y1": eleman[i].center_y})
                else:
                    x1 = line_cord.get("x1")
                    y1 = line_cord.get("y1")
                    x2 = eleman[i].center_x - 24
                    y2 = eleman[i].center_y
                    canvas.create_line(x1, y1, x2, y2, width = 2)
                    line_cord.update({"x1": None, "x2":None, "y1": None, "y2":None})

def press_right(self):
    x = kordinatlar.get("x")
    y = kordinatlar.get("y")
    eleman_secili_mi = bilgiler.get("eleman_secili_mi")
    if eleman_secili_mi is True:
        secili_eleman = bilgiler.get("secili_eleman")
        kacinci = bilgiler.get("kacinci")
        eleman.append(None)
        eleman[-1] = Circuit_Element(kacinci, secili_eleman, x, y)
        canvas.create_image(eleman[-1].center_x, eleman[-1].center_y, image = img_dic[eleman[-1].type])
        bilgiler.update({"eleman_secili_mi": False})
        canvas.itemconfig(fare_resim, image = img_dic["bos.gif"])

def motion(self): # fare hareketini takip ediyor ve seçili devre elemanının gösteriyor.
    kordinatlar.update({"x": self.x, "y": self.y})
    x = kordinatlar.get("x")
    y = kordinatlar.get("y")
    canvas.coords(fare_kare, x-24, y-24, x+24, y+24)
    canvas.coords(fare_resim, x, y)

def app():
    for resim in os.listdir(resim_klasoru):
        os.chdir(resim_klasoru)
        img_dic[resim] = tk.PhotoImage(file="%s"%(resim))
    
    ust_menu = tk.Menu(root) # en tepeye bos menu ekliyor
    birinci = tk.Menu(ust_menu, tearoff = 0)
    ikinci = tk.Menu(ust_menu, tearoff = 0)
    ucuncu = tk.Menu(ust_menu, tearoff = 0)
    devreler = tk.Menu(birinci, tearoff = 0)

    ust_menu.add_cascade(label="birinci", menu = birinci)
    ust_menu.add_cascade(label="kutuphane", menu = ikinci)
    
    birinci.add_cascade(label = "devreler", menu = devreler)
    birinci.add_command(label="new circuit", command = lambda: canvas.pack()) # canvas.pack devreyi çizeceğimiz bölgeyi oluşturuyor
    
    try:
        devreler.add_command(label="asenkron makine", command = asenkron_makine(canvas))
    except:
        pass

    ikinci.add_command(label = "resistor", command = lambda: chosen_element("resistor"))
    ikinci.add_command(label = "inductor", command = lambda: chosen_element("inductor"))
    ikinci.add_command(label = "capacitor", command = lambda: chosen_element("capacitor"))
    
    root.config(menu=ust_menu)
#-------------------
root = tk.Tk()

app()

canvas = tk.Canvas(root, width=750, height=220, bg="#daefa7")
fare_kare = canvas.create_rectangle(40,40,88,88, fill="#f0f8ff")
fare_resim = canvas.create_image(50,50, image = img_dic["bos.gif"])

root.bind('<Motion>', motion)
root.bind('<Button-1>', press_left)
root.bind('<Button-3>', press_right)

root.mainloop()

"""
def asenkron_makine(canvas):
    os.chdir(ana_klasor)
    with open("asenkron_makine.csv", "r", newline = "") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        for row in reader:
            asenkron_makine_elemani.append(None)
            asenkron_makine_elemani[-1] = canvas.create_image(row[0], row[1], image = img_dic["%s.GIF"%(row[2])])

def devreyi_ciz():
    os.chdir(ana_klasor)
    k = 0
    with open("excel.csv", "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        for row in reader:
            eleman.append(k)
            eleman[k] = canvas.create_image(row[0], row[1], image = img_dic["%s.GIF"%(row[2])])
            k += 1
"""
