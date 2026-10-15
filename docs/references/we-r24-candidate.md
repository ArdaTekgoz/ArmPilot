# Mekanik aday: WE-R2.4 - ilk inceleme

Tarih: 15 Ekim 2026 | Durum: Arda'nın baskı almayı düşündüğü aday; nihai mekanik/donanım seçimi değildir.

## Kaynak ve doğrulanan bilgiler

- Kullanıcının verdiği [MakerWorld WE-R2.4 bağlantısı](https://makerworld.com/tr/models/95279-we-r2-4-six-axis-robot-arm?from=search#profileId-318707). Model ve baskı profili kimliği: 95279 / 318707. Yazar sayfada LoboCNC olarak görünüyor.
- Model açıklaması tarayıcıdan okundu. Tasarımcı modeli UR3'ün yaklaşık yüzde 80 ölçekli biçiminden kabaca esinlenen altı eksenli bir tasarım olarak tanımlıyor. Bu ifade UR5 boyutlarının doğrudan ölçeklenmesini veya tüm eksen/ofsetlerin aynı olmasını doğrulamaz.
- Mekanik yaklaşım: Her eklemde step motor + bileşik planet redüktör aktüatörü. Açıklamada tabandaki ilk iki eklem için iki büyük, dirsek için bir orta ve bilek için üç küçük aktüatör belirtiliyor. [Aktüatör tasarımı](https://www.printables.com/model/132262-robot-actuators) ayrı bağlantı olarak veriliyor.
- Özgün kontrolcü örneği Pololu Tic T500 ve özel firmware kullanıyor. Bu, ArmPilot için kontrolcü veya motor satın alma kararı değildir.
- Kullanıcı STL/SLDPRT parçaları bulunduğunu belirtti. Dosya envanteri ve montaj dosyası mevcudiyeti henüz doğrulanmadı; MakerWorld dosya seçenekleri oturum açma ekranına yönlendirdi. Bu incelemede CAD veya baskı dosyası indirilmedi, açılmadı, ölçülmedi.
- Sayfada CC BY-NC-SA 4.0 lisans etiketi görüntülendi; kaynak/sürüm ve ilgili dosyaların kullanım koşulları model içeriği depoya alınmadan ayrıca kaydedilecek. Burada yalnız bağlantı ve inceleme notu saklanıyor.

## Mevcut ROS 2 çalışması

[mathias31415/diy_robotics](https://github.com/mathias31415/diy_robotics), WE-R2.4'ün fiziksel kurulumu, ROS 2 ve ESP32 ile yürütülmesi için proje ekibinin yayımladığı çalışmadır. ArmPilot'un STM32 ile uyumunu veya bizim donanımımızın hazır çalışacağını kanıtlamaz.

Bu çalışmanın [robot tanımı](https://github.com/RobinWolf/diy_robotarm_wer24_description), değişiklik yapılmış bir WE-R2.4 için geometri, Xacro ve çarpışma modeli içerdiğini açıklıyor. [Kinematik yapılandırması](https://github.com/RobinWolf/diy_robotarm_wer24_description/blob/main/config/default_kinematics.yaml) CAD'den çıkarılmış eklem konum/yönelimleri sunuyor. Proje ekibi kendi uyarlamalarını belirttiği için bu sayısal değerler MakerWorld paketinin doğrulanmış ölçüleri olarak alınmadı. Bu oturumda Xacro eklem zincirinin tamamı kontrol edilmedi; birebir eksen eşlemesi açık iş olarak kaldı.

ARM-01 kapanış güncellemesi: Kullanıcı CAD montaj görüntüsünü sağladı ve şemayı AI'ın hazırlamasını istedi. Yayımlanmış [Xacro eklem zinciri](https://github.com/RobinWolf/diy_robotarm_wer24_description/blob/main/urdf/diy_robotarm_macro.urdf.xacro) daha sonra incelendi; altı yerel eksenin `+Z` olarak tanımlandığı zincir, yapılandırma dönüşümleriyle birleştirilip [WE-R2.4 şemasına](wer24-joint-axes-reference.png) dönüştürüldü. Bu referans için J2-J3-J4 paralelliği ve komşu bilek eksenlerinin dikliği sayısal olarak kontrol edildi. Kullanıcının CAD paketiyle boyutsal/sıfır yönü eşleştirmesi hâlâ yapılmadı. Önceki paragraf ilk incelemenin durumunu kaydeder.

UR5 referans şeması öğretici olarak korunuyor. WE-R2.4'e ait gerçek geometrik model, seçilen dosya sürümü ve daha sonra gerçek montaj üzerinden doğrulanacak. Hazır ROS çalışması ileride karşılaştırma/inceleme kaynağıdır; mevcut büyük kod tabanı ArmPilot'a aktarılmadı.

## Bugün gereken ve sonraki aşama

**ARM-01:** Adayı ve kaynak bağlantısını kaydetmek, J1-J6 çizimini yapmak, erişim/yük/hız ve hata hedeflerini taslak olarak gerekçelendirmek. Tam CAD montajı gerekmez. Sadece dosyalar zaten eldeyse üst seviye montaj dosyası (.SLDASM/.STEP) var mı diye kısa envanter kontrolü isteğe bağlı yapılabilir.

**ARM-03:** Gerekirse hafif bir kinematik montajla eklem eksenleri, link/ofset boyları, sıfır duruşu ve TCP referansını belirlemek; STL parçalarını eklem sonrası hareket eden link gruplarına ayırmak. Ürün modelinde UR5 ölçülerini kullanmamak.

**ARM-11/12:** Gerçek parça/aktüatör sürümlerini, yük ve bütçeyi değerlendirmek; gerekli detaylı CAD uyarlaması, baskı kuponu ve montaj doğrulaması. Ana gövde dosyalarının bütün redüktör/aktüatör dosyalarını içerdiği varsayılmayacak.
