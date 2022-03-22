import sqlite3
import serial
import tkinter as tk
import datetime
sayfa =tk.Tk()
baslik=tk.Label(text='VERİ TOPLAMA ARAYÜZÜ',font='Times 35 normal')
sayfa.geometry('800x800')
baslik.pack()
veri1=int
veri2=int
veri3=str
gercek_veri={}

def arayuzgosterme(saat,veri1,veri2,veri3):
    saat_yazimi = tk.Label(text="saat= {}".format(saat), font='Times 20')
    saat_yazimi.place(relx=0.06, rely=0.4)
    veri_1_yazimi = tk.Label(text="veri1 = {}".format(veri1), font='Times 20')
    veri_1_yazimi.place(relx=0.06, rely=0.5)
    veri_2_yazimi = tk.Label(text="veri2= {}".format(veri2), font='Times 20')
    veri_2_yazimi.place(relx=0.06, rely=0.6)
    veri_3_yazimi = tk.Label(text="veri3= {}".format(veri3), font='Times 20')
    veri_3_yazimi.place(relx=0.06, rely=0.7)

    return
def veri_ayirma(input):
    print(input)
    bolunmusinput = input.split("=")
    print(bolunmusinput)
    for j in range(0,len(bolunmusinput)-1):
        print("bolunmuş input {}".format(bolunmusinput))
        #print("-------------")
        #print(type(bolunmusinput))
        yeni_input=bolunmusinput.copy()
        print("*****************")
        print(yeni_input)
        #print(yeni_input[0])
        #print(type(yeni_input[0]))
        #print("----------")
        anahtar=yeni_input[0]
        print(anahtar)
        gercek_veri["{}".format(bolunmusinput[0])]="{}".format(bolunmusinput[1])
        print("-------------")
        print(gercek_veri)
def veritabaninagiris(saat,veri1,veri2,veri3):
    database_connect = sqlite3.connect("usbverileri.db")
    database = database_connect.cursor()
    print("checkpoint_2 ")
    database.execute(
        """CREATE TABLE IF NOT EXISTS log(tarih TEXT, veri1 TEXT, veri2 TEXT, veri3 TEXT)""")
    database.execute(
        """INSERT INTO log VALUES("{}","{}","{}","{}")""".format(saat,veri1,veri2,veri3))
    print("prosses done")
    database_connect.commit()
    database_connect.close()
    return
def destroy():
    sayfa.destroy()
veribaglantisi=serial.Serial("COM7",9600)
while 1:
        buton = tk.Button(sayfa, text="kapat", bg="lightgreen", fg="black", command=destroy)
        buton.place(relx=0.5, rely=0.5)

        saat = str(datetime.datetime.now().strftime('%H:%M:%S'))
        gelenveri = veribaglantisi.readline()
        print(gelenveri)
        print("**********************")
        print(saat)
        cevrilmisveri = gelenveri.decode('UTF-8')
        print("aracverisi = ",cevrilmisveri)
        print("**********************")
        bolunmus = cevrilmisveri.split("x")  # .split belitilen karaktere göre str dizisini böler burada x kullanıyorum çünkü noktalı işaretler hataya sebebiyet veriyor
        print(bolunmus)
        print(bool(bolunmus[0]))
        bolunmus.pop(0)
        b=len(bolunmus)
        bolunmus.pop(b-1)
        for i in range(b-1):
            print(i)
            print("veri ayırma")
            veri_ayirma(bolunmus[i])
        print(gercek_veri)
        print("checkpoint_1")
        veri_1 =gercek_veri["veri1"]
        veri_2 =gercek_veri["veri2"]
        veri_3 =gercek_veri["veri3"]
        arayuzgosterme(saat, veri_1,veri_2, veri_3)
        veritabaninagiris(saat, veri_1, veri_2, veri_3)

        print(gercek_veri)
        sayfa.update()