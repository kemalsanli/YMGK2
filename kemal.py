import emine
import fatih
import kaydet
import hash
import os
import cv2

gelendeger=[207,192,0,74,230,6,155,195,0,118,210,155,250,83,184,194,112,220,68,126,12,7,185,255,89,234,249,47,216,148,125,165,111,120,199,249,219,61,78,88,18,11,169,206,23,125,40,42,75,43,183,72,144,38,77,183,162,189,171,214,208,144,248,169]

#Dosya yolu, bunu sabit yapabiliriz isterseniz.
path = "koala.jpeg"

#Gelen dosyayı okuduk hashini aldık
#demo = cv2.imread("koala.jpeg")
#demo = cv2.imread("temp/data/sifreli.png")
gorsel = cv2.imread(path)
hashFile = hash.hashIt(path)


if  os.path.exists('key') == False:
    os.mkdir('key')
    
if  os.path.exists('temp') == False:
        os.mkdir('temp')

#Gelen hash değeri key klasörürün altında var ise koşulumuzu çalıştırdık.
if  os.path.exists(('key/{}.png'.format(hashFile))):
    
    #Keyi okuduk xor yaptık ve kaydettik
    key = cv2.imread(('key/{}.png'.format(hashFile)))
    sifresiz = fatih.xor(gorsel,key)
    
    kaydet.kaydet(sifresiz,'temp/sifresiz.png')
    #İsimiz bitince key'i sildik.
    os.remove(('key/{}.png'.format(hashFile)))

    
#Key olmadığı durumlarda ise..
else:

    #Gelen değeri aldık anahtar oluşturduk, anahtar oluştururken boyutlarını almak için orijinal görseli de dahil ettik.
    keySource = emine.randomsayi(gelendeger)

    anahtar = fatih.anahtarOlustur(gorsel, keySource)

    #Xorladık ve dönen değeri pillow ile diziden .png uzantılı bir dosyaya çevirip kaydettik.
    sifrelenmis = fatih.xor(gorsel, anahtar)
    
    kaydet.kaydet(sifrelenmis,'temp/sifreli.png')
    sifreliHash = hash.hashIt('temp/sifreli.png')
    kaydet.kaydet(anahtar,('key/{}.png'.format(sifreliHash)))


