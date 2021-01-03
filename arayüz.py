from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import os
import emine
import fatih
import kaydet
import hash
import os
import cv2
import dosyaac

root = tk.Tk()
root.title('YMGK2 XOR')
#root.geometry("200x100")
root.eval('tk::PlaceWindow . center')
#root.resizable(False, False)


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
print("                                                                           Was")
print("                                                                          Here")



def select_image():
    # grab a reference to the image panels
    global panelA, panelB
 
    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename(initialdir = "/",title = "Resim Seçin",filetypes = (("Resim Dosyaları",".png .jpg .jpeg"),("Tüm Dosyalar",".*")))
    # ensure a file path was selected
    if len(path) > 0:
        gorsel = cv2.imread(path)
        hashFile = hash.hashIt(path)
        image = cv2.imread(path)

        if  os.path.exists('key') == False:
            os.mkdir('key')
            
        if  os.path.exists('temp') == False:
                os.mkdir('temp')
        if  os.path.exists(('key/{}.png'.format(hashFile))):
            key = cv2.imread(('key/{}.png'.format(hashFile)))
            sifresiz = fatih.xor(gorsel,key)
            
            kaydet.kaydet(sifresiz,'temp/sonuc.png')
            os.remove(('key/{}.png'.format(hashFile)))
        else:
            keySource = emine.randomsayi(gelendeger)

            anahtar = fatih.anahtarOlustur(gorsel, keySource)
            sifrelenmis = fatih.xor(gorsel, anahtar)
            
            kaydet.kaydet(sifrelenmis,'temp/sonuc.png')
            sifreliHash = hash.hashIt('temp/sonuc.png')
            kaydet.kaydet(anahtar,('key/{}.png'.format(sifreliHash)))
        
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        dosyaac.Clear_Console()
        print("                                                                         Kemal")
        print("                                                                           Was")
        print("                                                                          Here")
        edged = cv2.imread('temp/sonuc.png')
        
 
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        edged = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)
        
        
        
 
        # convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
 
        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
 
            # while the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)
 
        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged
    btn.config(text="Yeniden Seç")      

    
# b1=tk.Button(root,text="Dosya Seç",font=40,command=browsefunc)
# spaceLabel = tk.Label(root, text= "                     ")
# label1 = tk.Label(root, text= "Lütfen bir resim dosyası seçin.")
# spaceLabel.pack()
# label1.pack()
# b1.pack()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Lütfen bir resim dosyası seçin.", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

root.mainloop()