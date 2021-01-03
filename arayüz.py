from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os
import emine
import fatih
import kaydet
import hash
import os
import cv2
import dosyaac

root = tk.Tk()
root.title('YMGK2')
root.geometry("200x100")
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)


gelendeger=[207,192,0,74,230,6,155,195,0,118,210,155,250,83,184,194,112,220,68,126,12,7,185,255,89,234,249,47,216,148,125,165,111,120,199,249,219,61,78,88,18,11,169,206,23,125,40,42,75,43,183,72,144,38,77,183,162,189,171,214,208,144,248,169]

dosyaac.Clear_Console()
print("                     Resim dosyası seçin.")
print("                      _________________")
print("                     | | ___________ |o|")
print("                     | | ___________ | |")
print("                     | | ___________ | |")
print("                     | | ___________ | |")
print("                     | |_____________| |")
print("                     |     _______     |")
print("                     |    |       |   ||")
print("                     | KD |       |   V|")
print("                     |____|_______|____|")
print("                                                                         Kemal")




def browsefunc():
    
    
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Resim Seçin",filetypes = (("Resim Dosyaları",".png .jpg .jpeg"),("Tüm Dosyalar",".*")))
    label1.config(text='{}'.format(os.path.basename(root.filename)))
    b1.config(text="Yeniden Seç")
    dosyaac.Clear_Console()
   
    path = root.filename
    gorsel = cv2.imread(path)
    hashFile = hash.hashIt(path)


    if  os.path.exists('key') == False:
        os.mkdir('key')
        
    if  os.path.exists('temp') == False:
            os.mkdir('temp')
    if  os.path.exists(('key/{}.png'.format(hashFile))):
        key = cv2.imread(('key/{}.png'.format(hashFile)))
        sifresiz = fatih.xor(gorsel,key)
        
        kaydet.kaydet(sifresiz,'temp/sonuc.png')
        #İsimiz bitince key'i sildik.
        os.remove(('key/{}.png'.format(hashFile)))
    else:
        keySource = emine.randomsayi(gelendeger)

        anahtar = fatih.anahtarOlustur(gorsel, keySource)
        sifrelenmis = fatih.xor(gorsel, anahtar)
        
        kaydet.kaydet(sifrelenmis,'temp/sonuc.png')
        sifreliHash = hash.hashIt('temp/sonuc.png')
        kaydet.kaydet(anahtar,('key/{}.png'.format(sifreliHash)))
    filename='temp/sonuc.png'
    dosyaac.Open_file(filename)
    
b1=tk.Button(root,text="Dosya Seç",font=40,command=browsefunc)
spaceLabel = tk.Label(root, text= "                     ")
label1 = tk.Label(root, text= "Lütfen bir resim dosyası seçin.")
spaceLabel.pack()
label1.pack()
b1.pack()


root.mainloop()