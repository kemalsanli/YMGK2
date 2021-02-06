import crypto
import xor
import save
import hash
import os



def ymgk2xor(imagePath, generatedHash):
    #Seçilen görseli okuduk.
    image = cv2.imread(imagePath)
    #Seçilen Dosyanın Hash'ini alıyor.
    hashFile = hash.hashIt(imagePath)

    #Klasör kontrolü yoksa oluşturuluyor.
    if  os.path.exists('key') == False:
        os.mkdir('key')

    if  os.path.exists('temp') == False:
            os.mkdir('temp')

    #Gelen hash değeri key klasörürün altında var ise koşulumuzu çalıştırdık.
    if  os.path.exists(('key/{}.png'.format(hashFile))):

        #Keyi okuduk xor yaptık ve kaydettik
        key = cv2.imread(('key/{}.png'.format(hashFile)))
        decryptedImage = xor.xor(image, key)

        save.saveAsImage(decryptedImage, 'temp/decryptedImage.png')
        #İsimiz bitince key'i sildik.
        os.remove(('key/{}.png'.format(hashFile)))


    #Key olmadığı durumlarda ise..
    else:
        #Hash'i olasılıkları artırmak adına biraz uzattık.
        populatedHash=hash.populateHash(generatedHash)
        #Hexten uint8'e çevirdik
        uint8Hash=xor.hexToUint8(populatedHash)
        #Anahtar oluşturmak için ip3'teki gerekli eylemleri tamamladık.
        keySource = crypto.rng(uint8Hash)
        #Gelen değeri aldık anahtar oluşturduk, anahtar oluştururken boyutlarını almak için orijinal görseli de dahil ettik.
        key = xor.createNewKey(image, keySource)

        #Xorladık ve dönen değeri pillow ile diziden .png uzantılı bir dosyaya çevirip kaydettik.
        encryptedImage = xor.xor(image, key)

        save.saveAsImage(encryptedImage, 'temp/encryptedImage.png')
        encryptedImageHash = hash.hashIt('temp/encryptedImage.png')
        save.saveAsImage(key, ('key/{}.png'.format(encryptedImageHash)))
