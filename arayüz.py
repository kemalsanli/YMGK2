from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import os
import crypto
import xor
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
root.iconphoto(False, tk.PhotoImage(file='icon.png'))

SHASH = '4f54e67cb598e8219158647e4f54e67cb598e8219158647e6340af13ab3b07b48f2501226d2f516f0be110584f54e67cb598e8219158647e6340af13ab3b07b48f2501226d2f516f0be110586340af13ab3b07b48f2501226d2f516f0be11058'


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
            sifresiz = xor.xor(gorsel, key)

            kaydet.kaydet(sifresiz,'temp/sonuc.png')
            os.remove(('key/{}.png'.format(hashFile)))
        else:
            #Hash'i olasılıkları artırmak adına biraz uzattık.
            populatedHash=hash.populateHash(SHASH)
            #Hexten decimale çevirdik
            gelendeger=xor.hexToUint8(populatedHash)
            #Gelen değeri aldık anahtar oluşturduk, anahtar oluştururken boyutlarını almak için orijinal görseli de dahil ettik.
            keySource = crypto.randomsayi(gelendeger)

            anahtar = xor.anahtarOlustur(gorsel, keySource)
            sifrelenmis = xor.xor(gorsel, anahtar)

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
dosyaac.Clear_Console()
