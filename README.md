# YMGK2

YMGK2 son kullanıcılardan en az girdiyi alarak en çok güvenliği sağlamaya çalışan bir kriptoloji pratiğidir.

Bu konsept uygulamanın sunucular üzerinde çalışan sürümü [YMGK2-DJANGO-API](https://github.com/kemalsanli/YMGK2-DJANGO-API)'da github üzerinde mevcuttur.

Bu konsept uygulamanın multiplatform istemci uygulaması [bilmiyorum](https://github.com/kemalsanli/bilmiyorum)'da github üzerinde mevcuttur.

## Açıklama



## Başlarken

### Gereklilikler

* Python 3+
* pip


### Kurulum Gereksinimleri

* Curl kullanılabilir olmalıdır.

### Kurulum

* Pip kurulumu için gerekli olan get-pip.py dosyasını indirin.

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
* Sonrasında pip kurulumunu başlatın. 

```
python get-pip.py
```
* Gerekli kütüphaneleri yükleyin. 

```
pip install opencv-python Pillow numpy
```

* Uygulamayı çalıştırmak için komut satırı üzerinde dosyaların bulunduğu klasöre gelip verilen komutu çalıştırın. 

```
python arayüz.py
```
* Artık uygulamyı kullanmaya hazırsınız. 


## Yardım

Henüz herhangi bir sorunla karşılaşmadık.
```
...ama siz yine de sorun yaşarsanız bi kapatıp açın
```

## Kullanım

Arayüz için, uygulama üzerinde şifreleme ve açma işlemlerinizden sonra temp klasörü altında sonuc.png çıktısı oluşur her seferinde temizlemenize gerek yoktur çünkü yeni sonuçlar sonuc.png üzerine yazılır. Eğer şifrelenmiş görseli iletmek istiyorsanız uygulamayı tekrar kullanmadan sonuc.png'nin farklı isimdeki bir kopyasını oluşturunuz aksi takdirde görselin üzerine yeni şifrelediğiniz görsel yazılacak ve şifrelenmiş görseli kaybedeceksiniz.

Key klasörü bitwise şifrelemede kullanılan anahtarları içerir, şifresi açılan bir görselin anahtarı otomatik olarak silinecektir.

Her görsel şifrelemenizde tek kullanımlık bir anahtar üretilir, bu yüzden aynı görseli tekrar tekrar kullansanız da her defasında farklı anahtarlar üretilir.

Şifrelenmiş görseller bitwise şekilde xor'landığı için lütfen görsellerin aynı hash değerlerini korumasına özen gösterin, eğer aynı görsel olmazsa bitwise_xor bu şifrelemeyi açamaz.

## Arayüz

![Arayüz 1](https://github.com/kemalsanli/YMGK2/blob/main/aray%C3%BCz%201.png?raw=true)

![Arayüz 2](https://github.com/kemalsanli/YMGK2/blob/main/aray%C3%BCz%202.png?raw=true)

![Arayüz 3](https://github.com/kemalsanli/YMGK2/blob/main/aray%C3%BCz%203.png?raw=true)



## Ekip

Projeyi oluşturan ekip.

 ### Gerçekleştirme
 
 Kemal SANLI  
 [@kemalsanli](https://github.com/kemalsanli)

 Fatih ULUDAĞ  
 [@fatih-uludag](https://github.com/fatih-uludag)
 
 Haşim DELİL  
 [@hasimdelil](https://github.com/hasimdelil)

 Batuhan HARMANŞAH  
 [@batuhanharmansah](https://github.com/batuhanharmansah)
 
 Turan ÇAYMAZ  
 [@turancaymaz](https://github.com/turancaymaz)
 
 Emine SAĞIROĞLU
 
 Halil İbrahim YANIK
 
 ### Döküman
 
 Furkan ERDOĞAN  
 [@Hawkyshun](https://github.com/Hawkyshun)
 
 Seda YUMRUTEPE
 
 Gül ÖNAL
 
 Kübra YILMAZKAR
 
 Ali METİN
 


## Sürüm Geçmişi

* 1.0
    * Yayınlandı.

## Katılım
Pull Requestlere her zaman açığız.

## Teşekkürler
[opencv](https://github.com/opencv/opencv)

## Lisans
[MIT](https://github.com/kemalsanli/YMGK2/blob/main/LICENSE)
