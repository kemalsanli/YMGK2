from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import crypto
import xor
import save
import hash
import os
import cv2
import openFile

root = tk.Tk()
root.title('YMGK2 XOR')
root.eval('tk::PlaceWindow . center')
root.iconphoto(False, tk.PhotoImage(file='icon.png'))

#default hash value
SHASH = '4f54e67cb598e8219158647e4f54e67cb598e8219158647e6340af13ab3b07b48f2501226d2f516f0be110584f54e67cb598e8219158647e6340af13ab3b07b48f2501226d2f516f0be110586340af13ab3b07b48f2501226d2f516f0be11058'


openFile.clearConsole()
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
        image = cv2.imread(path)
        hashFile = hash.hashIt(path)

        if  os.path.exists('key') == False:
            os.mkdir('key')

        if  os.path.exists('temp') == False:
                os.mkdir('temp')
        if  os.path.exists(('key/{}.png'.format(hashFile))):
            key = cv2.imread(('key/{}.png'.format(hashFile)))
            decryptedImage = xor.xor(image, key)

            save.saveAsImage(decryptedImage, 'temp/result.png')
            os.remove(('key/{}.png'.format(hashFile)))
        else:
            #Hash'i olasılıkları artırmak adına biraz uzattık.
            populatedHash=hash.populateHash(SHASH)
            #Hexten uint8'e çevirdik
            uint8Hash=xor.hexToUint8(populatedHash)
            #Gelen değeri aldık anahtar oluşturduk, anahtar oluştururken boyutlarını almak için orijinal görseli de dahil ettik.
            keySource = crypto.rng(uint8Hash)

            key = xor.createNewKey(image, keySource)
            encryptedImage = xor.xor(image, key)

            save.saveAsImage(encryptedImage, 'temp/result.png')
            encryptedImagesHash = hash.hashIt('temp/result.png')
            save.saveAsImage(key, ('key/{}.png'.format(encryptedImagesHash)))

        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        openFile.clearConsole()
        print("                                                                         Kemal")
        print("                                                                           Was")
        print("                                                                          Here")
        edged = cv2.imread('temp/result.png')


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

panelA = None
panelB = None
btn = Button(root, text="Lütfen bir resim dosyası seçin.", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

root.mainloop()
openFile.clearConsole()
