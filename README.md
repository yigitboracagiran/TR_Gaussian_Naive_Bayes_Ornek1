# TR_Gaussian_Naive_Bayes
Not: Excel dosyası ile Python kodunun aynı dizinde olması gerekmektedir.

1- Veri seti okunarak Data Frame’e başarıyla aktarılmıştır.

2- Veriler, %30-%70 oranında olacak şekilde test ve eğitim verisine bölünmüştür.

3- Yapılan araştırmalar sonucunda listede işlemlerin daha hızlı yapılabileceği öğrenilmiştir. Bu nedenle
Data Frame’lerde tutulan test ve eğitim verileri listeye dönüştürülmüştür.

4- Eğitim verileri sınıflarına göre ayrılmıştır ve her sınıfın hangi indekslerde bulunduğu listede
tutulmuştur.

5- Tüm nitelikler sayısal değere sahip olduğu için test verilerinin hangi sınıftan oluğu hesaplanırken
sayısal verilerde hesaplama yapılması gerekmiştir ve aşağıdaki formül kullanılmıştır:

( 1 / ( Sınıfın Standart Sapması * ( 2 * e ^ [ ( -0.5 ) * ( [ Test Verisi – Sınıfın Ortalaması ] / Sınıfın
Standart Sapması ] ^ 2 ) ) ) * ( Sınıf Kaç Adet Bulunduğu / Toplam Sınıf Sayısı )

6- Bu formülün kullanılabilmesi için sınıfların standart sapması ve ortalaması hesaplanmıştır.

7- Her test verisinin her sınıf için olasıkları hesaplanmıştır.

8- Hesaplanan olasılıklar arasında en yükseği seçilmiştir ve tahmin edilen sınıf bulunmuştur.

9- Tahmin edilen sınıf ile, test verisinin gerçek sınıfı karşılaştırılmış, doğru veya yanlış tahmin edildi bilgisi
kullanıcıya döndürülmüştür.

10- En sonunda ise doğruluk oranının yüzdesi aşağıdaki formül ile hesaplanmıştır:

Doğruluk Oranı = (Doğru Tahmin * 100 ) / (Doğru Tahmin + Yanlış Tahmin)

11- Algortimanın tamamlanması üzerine tüm veriler üzerinde hazırlanan algoritma
denenmiştir.

12- Yapılan eğitimin sonunda elde edilen doğruluk oranı %89.98530852105779 hesaplanmıştır.
