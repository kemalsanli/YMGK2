import cv2
import numpy as np

def createNewKey(gorsel, gelen):
    r, c ,t= gorsel.shape
    keyGen = np.random.randint(0, 256, size=(r, c, t ), dtype=np.uint8)
    key = np.random.choice(gelen,size=(r, c,t))
    mylist = []

    for i in key:
        arr = np.array(i, dtype=np.uint8)
        mylist.append(arr)
    fth = np.array(mylist)
    return cv2.bitwise_xor(fth, keyGen)

def xor(gorsel, anahtar):
    return cv2.bitwise_xor(gorsel, anahtar)

def hexToUint8(hash):
    return [int(hash[i:i+2],16) for i in range(0,len(hash),2)]
