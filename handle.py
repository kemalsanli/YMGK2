import crypto
import xor
import kaydet
import hash
import os
import cv2



def ymgk2xor(path,ServerHash):
    #Seçilen görseli okuduk.
    gorsel = cv2.imread(path)
    #Seçilen Dosyanın Hash'ini alıyor.
    hashFile = hash.hashIt(path)

    #Klasör kontrolü yoksa oluşturuluyor.
    if  os.path.exists('key') == False:
        os.mkdir('key')

    if  os.path.exists('temp') == False:
            os.mkdir('temp')

    #Gelen hash değeri key klasörürün altında var ise koşulumuzu çalıştırdık.
    if  os.path.exists(('key/{}.png'.format(hashFile))):

        #Keyi okuduk xor yaptık ve kaydettik
        key = cv2.imread(('key/{}.png'.format(hashFile)))
        sifresiz = xor.xor(gorsel, key)

        kaydet.kaydet(sifresiz,'temp/sifresiz.png')
        #İsimiz bitince key'i sildik.
        os.remove(('key/{}.png'.format(hashFile)))


    #Key olmadığı durumlarda ise..
    else:
        #Hash'i olasılıkları artırmak adına biraz uzattık.
        populatedHash=hash.populateHash(ServerHash)
        #Hexten uint8'e çevirdik
        gelendeger=xor.hexToUint8(populatedHash)
        #Anahtar oluşturmak için ip3'teki gerekli eylemleri tamamladık.
        keySource = crypto.randomsayi(gelendeger)
        #Gelen değeri aldık anahtar oluşturduk, anahtar oluştururken boyutlarını almak için orijinal görseli de dahil ettik.
        anahtar = xor.anahtarOlustur(gorsel, keySource)

        #Xorladık ve dönen değeri pillow ile diziden .png uzantılı bir dosyaya çevirip kaydettik.
        sifrelenmis = xor.xor(gorsel, anahtar)

        kaydet.kaydet(sifrelenmis,'temp/sifreli.png')
        sifreliHash = hash.hashIt('temp/sifreli.png')
        kaydet.kaydet(anahtar,('key/{}.png'.format(sifreliHash)))
