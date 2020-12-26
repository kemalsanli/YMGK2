from PIL import Image

def kaydet(array, filename):
    img = Image.fromarray(array)
    img.save(filename)
     

def oku(filepath):
    img = Image.open(filepath)
    array = np.array(img)
    return (array) 