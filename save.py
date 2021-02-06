from PIL import Image
import numpy as np

def saveAsImage(array, filename):
    img = Image.fromarray(array)
    img.save(filename)
     

def readAsNpArray(filepath):
    img = Image.open(filepath)
    array = np.array(img)
    return (array) 