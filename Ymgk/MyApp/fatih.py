import cv2
from . import hash
from . import kaydet
import numpy as np
from PIL import Image

def anahtarOlustur(gelen):
    key = np.random.choice(gelen,size=(r, c,t)) 
    mylist = []

    for i in key:
        arr = np.array(i, dtype=np.uint8)
        mylist.append(arr)
    fth = np.array(mylist)
    return fth

def xor(gorsel, anahtar):
    r, c ,t= gorsel.shape
    return cv2.bitwise_xor(gorsel, anahtar)

def resim(gelen,demo):
    #gelen=[107,116,61,144,204,8,62,225,191,177,84,158,51,46,207,216,15,231,107,69,37,37,198,18,246,254,37,234,71,77,245,134]
    
    r, c ,t= demo.shape

    #key2 = np.random.choice([1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1],size=(r, c)) # Generate random key image
    key2 = np.random.choice(gelen,size=(r, c,t)) # Generate random key image
    mylist = []

    for i in key2:
        arr = np.array(i, dtype=np.uint8)
        mylist.append(arr)
    fth = np.array(mylist)


    #key2=np.dtype(np.uint8)


    encryption = cv2.bitwise_xor(demo, fth) # encryption
    decryption = cv2.bitwise_xor(encryption, fth) # decryption
 
    cv2.imshow("Sifrelenmis", encryption) # Display ciphertext image
    cv2.imshow("Acilmis", decryption) # Display the decrypted image
    
    kaydet.kaydet(encryption,'testrgba.png')
    print(hash.hashIt('testrgba.png'))
    

    cv2.waitKey(-1)
    cv2.destroyAllWindows()

