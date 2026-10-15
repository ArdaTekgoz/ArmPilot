# ArmPilot R3 - Onaylı görev kartları

15 Ekim 2026. Kullanıcı sekiz revizyonu ve web/PDF eşitlemesini onayladı. ARM-01 R2 tamamlandı; ARM-02 haftaya başlar.

24 görev, 242 saat geçici ana kapsam; yazılım kapısı ARM-10’a kadar 112 saat. R3 süreleri ilk planlama varsayımıdır; taahhüt değildir. ARM-02 ve ARM-04 sonunda yeniden tahmin et. Haftada 4 saat; dört saatten uzun görevler birden fazla oturumdur. %25 pay yalnız senaryodur; tedarik ve başarısız denemeler dahil kesin bitiş tarihi verilmez.

Bu plan tamamlanmış uygulama kanıtı değildir. 4 saatlik haftalık kapasite korunur; her görev bir hafta demek değildir.

## Aşama bütçeleri

| Aşama | Saat |
| --- | ---: |
| A — Kapsam ve temel | 16 |
| B — Kinematik ve robot modeli | 42 |
| C — ArmPilot ve planlama | 54 |
| D — Donanım tasarımı | 44 |
| E — Kontrol ve montaj | 42 |
| F — Fiziksel demo ve kapanış | 40 |
| G — Kontrollü devam | 4 |

## ARM-01 - Kullanım senaryosu ve altı eksenli sürüm sözleşmesi

**Tahmin:** 4 saat | **Ön koşul:** Yok | **Donanım:** Gerekmez

Altı eksenli masaüstü ArmPilot ürününü, öğrenme amacını ve v0.1/v1.0 sınırlarını ölçülebilir biçimde tanımla. R2 belge kapanışı 15 Ekim 2026 tarihinde yapıldı.

**Uygulama:**

1. XYZ (mm) + uç yönelimi hedefi, 3B görüntüleme, Planla → Önizle → Yürüt akışını tanımla.
2. WE-R2.4 adayını, J1-J6 eksenlerini ve flanş/TCP ayrımını CAD görüntüsü ve kaynaklı AI şemasıyla açıkla. Kullanıcı talebiyle elle çizim yerine bu kanıt kabul edildi.
3. Yaklaşık 400 mm erişim, 100 g toplam harici uç kütlesi, 5°/s ve 10°/s² değerlerini doğrulanmamış tasarım varsayımı olarak kaydet.
4. Isı haritası, lazer, kamera otonomisi, gripper sürme ve çizimden takım yolunu sonraki sürümlere ayır; Arda/AI katkısını belirt.

**Kabul:**

- [ ] Bir sayfalık kapsamda giriş, çıktı, hata davranışı, v0.1/v1.0 ve sürüm dışı işler bulunuyor.
- [ ] 10 mm konum ve 5° yönelim hatasının garanti değil tasarım hedefi olduğu yazılı; fiziksel değerlendirme 10 poz × 3 tekrar olarak taslaklandı.
- [ ] CAD görüntüsü, AI eksen şeması, kaynaklar ve açık katkı kaydı depoda; 3 saat aktif çalışma kullanıcı tahmini olarak kayıtlı.

**Kanıt:** docs/arm-01-kapsam.md, output/pdf/arm-01-kapsam.pdf, evidence/ARM-01 ve 65142f1 kapanış commit’i.

**Beceri:** Gereksinim yazımı, konum/yönelim ve serbestlik derecesi; bağımsız altı eksen açıklaması henüz sınanmadı.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-02 - Python temeli ve ROS 2/MoveIt ortam uyumluluğu

**Tahmin:** 12 saat | **Ön koşul:** ARM-01 | **Donanım:** Gerekmez

ARM-02’ye haftaya başla. Öğrenme örneğiyle ürün ortamını iki ayrı alt oturumda doğrula; tek dört saatlik güne sıkıştırma.

**Uygulama:**

1. Oturum A (~4 saat): bağımsız Python ortamı, Git çalışma döngüsü, mm↔m ve derece↔radyan dönüşümlerini Arda yazsın; küçük giriş/çıktı örnekleri çalışsın.
2. Oturum B (~8 saat; gerekirse böl): güncel resmî destek tablosundan OS/ROS 2/MoveIt 2/ros2_control eşleşmesini seç; Windows ile çalışma yolunu gerekçelendir.
3. Bir referans modelde joint_states al, planlama isteği gönder ve sahte kontrolcüde tek yörünge sonucunu gözle. Bu yalnız ortam denemesidir; kendi kolumuzun kabulü değildir.
4. ArmPilot UI/3B teknoloji adayını, ROS köprüsünü ve paket sürümlerini kısa uyumluluk denemesiyle seç; temiz tekrar için komutları kaydet.

**Kabul:**

- [ ] Arda birim dönüşümlerini kendi yazdığı örnekle açıklar; beklenen/gerçekleşen sonuçlar kayıtlı.
- [ ] Seçilen OS, dağıtım ve paket sürümleri ile planlama/durum/eylem haberleşmesi denemesi yeniden üretilebiliyor.
- [ ] UI/3B katmanı ve ROS bağlantı kararı gerekçeli; başarısız denemeler ve kalan riskler kayıtlı.

**Kanıt:** Ortam kurulum notu, sürüm listesi, birim örnekleri ve referans robot deneme kaydı.

**Beceri:** Python birimleri, sanal ortam, Git ve ROS topic/service/action ayrımı.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-03 - WE-R2.4 geometrisini ve altı eklemli robot tanımını çıkar

**Tahmin:** 12 saat | **Ön koşul:** ARM-02 | **Donanım:** Gerekmez

Yerel CAD’i robot tanımının tek geometri kaynağı yap; UR5 sayısal boyutlarını kopyalama.

**Uygulama:**

1. Kaynak tasarımın sürümünü/lisansını kaydet; J1-J6 merkezleri, yerel eksenler, sıfır duruşu ve mesafeleri CAD’den ölç.
2. base_link, altı döner eklem, flanş ve sabit TCP çerçevesi için tablo hazırla; CAD birimleri ile ROS metre/radyanı açıkça dönüştür.
3. URDF/Xacro, basitleştirilmiş görsel/çarpışma geometrileri ve geçici limitleri oluştur; robot_state_publisher ile göster.

**Kabul:**

- [ ] Altı eklem ve TCP zinciri ölçü tablosuyla izlenebilir; tek tek pozitif eklem hareketi CAD eksenleriyle karşılaştırıldı.
- [ ] URDF yükleniyor; bağlantısız link veya birim hatası yok; 400 mm erişim ve aday görev kutusu geometriye göre yeniden değerlendirildi.

**Kanıt:** CAD ölçü tablosu, model sürümü, URDF/Xacro ve altı tek-eklem ekran kaydı.

**Beceri:** Referans çerçevesi, TCP, yerel eksen ve CAD→robot modeli dönüşümü.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-04 - Kendi FK örneğini yaz ve robot modeliyle karşılaştır

**Tahmin:** 10 saat | **Ön koşul:** ARM-03 | **Donanım:** Gerekmez

İleri kinematiği öğren; kütüphane çıktısını anlamadan kullanma.

**Uygulama:**

1. Arda önce 2R düzlemsel FK’yi elle ve Python ile hesaplasın; sıfır ve dik açı örnekleri seçsin.
2. Homojen dönüşüm çarpımını adım adım altı eklem zincirine bağla; TCP ofsetini ekle.
3. En az beş bilinen duruşta kendi zincirinin konum/yönelimini robot tanımı/RViz çıktısıyla karşılaştır.

**Kabul:**

- [ ] 2R örnek Arda’nın kodu ve açıklamasıyla kayıtlı; özel duruş sonuçları beklenenle uyumlu.
- [ ] Beş 6R duruşta konum ve dönme matrisi farkı raporlandı; sayısal tolerans seçildi ve açıklanıyor.

**Kanıt:** FK öğrenme kodu, elle çözüm/hesap notu ve karşılaştırma tablosu.

**Beceri:** FK, dönüşüm zinciri, dönme matrisi ve TCP ofseti.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-05 - 2R IK öğren ve altı eksenli ürün çözücüsünü yapılandır

**Tahmin:** 10 saat | **Ön koşul:** ARM-04 | **Donanım:** Gerekmez

Öğrenme için kendi analitik IK örneğin ile üründeki hazır 6R çözücüyü ayır.

**Uygulama:**

1. Arda 2R analitik IK için iki dirsek çözümünü ve erişilemeyen noktayı uygulasın.
2. MoveIt Setup Assistant ile altı eklemli planning group, base/tip, home duruşu, SRDF ve IK eklentisini yapılandır.
3. XYZ+yönelim pozlarına IK üret; her çözümü FK ve eklem limitleriyle geri doğrula; çoklu çözüm seçiminde başlangıç duruşunu kullan.

**Kabul:**

- [ ] Arda’nın 2R örneğinde iki dal ve erişilemeyen hedef davranışı çalışıyor.
- [ ] Kendi robotumuzun SRDF/IK yapılandırması yükleniyor; en az beş başarılı poz ve iki başarısız örnek kayıtlı.
- [ ] Hazır çözücü katkısı açık; FK geri doğrulama toleransları yazılı.

**Kanıt:** 2R IK kodu, MoveIt config ve başarılı/başarısız poz tablosu.

**Beceri:** IK çokluluğu, sayısal çözücü, seed ve yapılandırma doğrulaması.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-06 - Poz erişimi, limitler ve planlama sahnesini doğrula

**Tahmin:** 10 saat | **Ön koşul:** ARM-05 | **Donanım:** Gerekmez

XYZ’ye erişmenin tek başına istenen yönelimle geçerli bir poz anlamına gelmediğini göster.

**Uygulama:**

1. Eklem limitleri, model öz çarpışmaları ve sabit masa/taban engellerini MoveIt sahnesine ekle; devre dışı çiftleri gerekçelendir.
2. Geçerli poz, erişim dışı poz, aynı XYZ’de olanaksız yönelim, limit ihlali ve tekillik yakınını örnekle.
3. Geometrik erişilememe, IK zaman aşımı ve geçerli yol bulunamamasını farklı sonuçlar olarak kaydet.

**Kabul:**

- [ ] Beklenen/gerçekleşen sonuç tablosunda en az sekiz örnek var; geçersiz hedef yeni hareket başlatmıyor.
- [ ] URDF+SRDF+joint_limits+kinematics+planning pipeline yapılandırması kendi modelimizle çalışıyor.
- [ ] Sabit sahne ve model kontrollerinin dinamik ortam güvenliği veya tüm uzay için erişim garantisi olmadığı açık.

**Kanıt:** Poz doğrulama tablosu, planlama sahnesi ve sürümlü MoveIt yapılandırması.

**Beceri:** Poz uzayı, çarpışma, limit, tekillik ve hata sınıfları.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-07 - ArmPilot’un kendi 3B masaüstü görünümünü oluştur

**Tahmin:** 16 saat | **Ön koşul:** ARM-06 | **Donanım:** Gerekmez

Ürün olarak kendi pencerende robotu görüntüle; RViz geliştirme karşılaştırması olsun.

**Uygulama:**

1. ARM-02’de seçilen UI/3B katmanında model yükleme, kamera döndürme/yakınlaştırma ve eksen görünümünü kur.
2. base, flanş ve TCP’yi göster; joint_states verisiyle altı eklemi güncelle.
3. Mevcut durum, hedef ve planlanan hareketi görsel olarak ayır; bağlantı ve veri tazeliğini göster; RViz ile aynı duruşu karşılaştır.

**Kabul:**

- [ ] Ayrı ArmPilot penceresinde kendi modelimiz açılıyor, kamera kontrol ediliyor ve altı eklem durum verisiyle güncelleniyor.
- [ ] TCP/eksenler ve mevcut/planlanan durum ayırt ediliyor; eski veri sessizce canlı durum gibi gösterilmiyor.

**Kanıt:** ArmPilot pencere videosu ve aynı duruşun RViz karşılaştırması.

**Beceri:** Masaüstü arayüz, sahne grafiği, dönüşümler ve durum görselleştirme.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-08 - XYZ+yönelim ve Planla–Önizle–Yürüt akışını kur

**Tahmin:** 12 saat | **Ön koşul:** ARM-07 | **Donanım:** Gerekmez

Hedef girişi ile fiziksel hareket yetkisini açık kullanıcı eylemleriyle ayır.

**Uygulama:**

1. XYZ’yi mm, yönelimi isimli ve sayısal tanımı kayıtlı hazır seçeneklerle al; base/TCP referansını göster.
2. Planla, Önizle ve Yürüt işlemlerini; simülasyon/fiziksel modunu, bağlantıyı ve hata durumlarını tasarla.
3. Hedef, model, sahne veya başlangıç durumu değişince planı geçersiz kıl. Hareket sırasında yeni hedefi reddet; kontrollü iptal/durmayı ayrı eylem olarak tanımla.

**Kabul:**

- [ ] Geçersiz giriş/poz anlaşılır hata veriyor ve yeni hareket başlatmıyor; planlama yürütme çağrısını kendiliğinden yapmıyor.
- [ ] Yalnız güncel ve önizlenmiş plan açık Yürüt eylemiyle gönderilebiliyor; fiziksel yürütme gerçek köprü doğrulanana kadar kilitli.
- [ ] Plan kimliği, model/sahne sürümü, başlangıç durumu ve aktif mod kullanıcıya izlenebilir.

**Kanıt:** Durum geçiş tablosu ve başarılı/reddedilen arayüz akış videosu.

**Beceri:** Girdi doğrulama, durum makinesi, işlem yetkisi ve plan geçerliliği.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-09 - Statik sahnede hareket planla ve sahte kontrolcüde yürüt

**Tahmin:** 18 saat | **Ön koşul:** ARM-08 | **Donanım:** Gerekmez

Donanım olmadan zamanlı altı eklemli yörüngeyi uçtan uca doğrula; v0.1’in yürütme provası burada yapılır.

**Uygulama:**

1. Alt oturum A: Arda tek eklem için kübik zaman ölçekleme örneğini yazsın; konum/hız/ivme sınırlarını yorumlasın.
2. Alt oturum B: MoveIt ile sabit modellenmiş sahnede pozdan poza çarpışma denetimli yol planla; zaman parametrelemesi ve eklem hız/ivme sınırlarını uygula.
3. Alt oturum C: FollowJointTrajectory destekli mock/fake kontrolcüye yörünge gönder, joint_states ve sonuç/iptal akışını ArmPilot’ta göster.
4. Yol bulunamaması, limit, eskimiş plan ve başlangıç durumu uyuşmazlığını dene; simülasyon modunda fiziksel cihaza çıkış olmadığını doğrula.

**Kabul:**

- [ ] Kendi kübik örneği ile ürün planlayıcısının katkısı ayrılmış; zaman damgaları artan, eklem isimleri ve hız/ivme limitleri doğrulanmış.
- [ ] Kendi 6R modelimizde mock kontrolcüyle plan→önizleme→yürütme→durum/sonuç akışı çalışıyor; iptal ve reddetme örnekleri kayıtlı.
- [ ] Model/sabit sahne çarpışma kontrolü var; dinamik engel algılama, proses takım yolu veya dinamik simülasyon iddiası yok.

**Kanıt:** Kübik öğrenme örneği, yörünge dosyası, mock yürütme videosu ve hata tablosu.

**Beceri:** Hareket planı, zaman parametrelemesi, trajectory action ve mock donanım.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-10 - ArmPilot v0.1 donanımsız teslimatını kapat

**Tahmin:** 8 saat | **Ön koşul:** ARM-09 | **Donanım:** Gerekmez

Kendi altı eksenli robotumuzla masaüstü uygulamasının yeniden üretilebilir yazılım teslimatını yap.

**Uygulama:**

1. Temiz ortam yönergesinden uygulamayı başlat; kendi modelini yükle ve XYZ+yönelimle başarılı plan/önizleme/mock yürütme göster.
2. Erişilemeyen hedef, engel nedeniyle yol yokluğu, eski plan ve kopuk/eski durum verisi örneklerini göster.
3. Kurulum, örnekler, bilinen sınırlar, Arda/AI/kütüphane katkısı ve sürüm notunu yaz; Git’te v0.1 işaretle.

**Kabul:**

- [ ] ARM-03–09 kanıtları mevcut; yalnız referans robot/RViz demosu bu kapıyı kapatmıyor.
- [ ] Kendi ArmPilot penceresinde en az üç geçerli ve üç reddedilen senaryo tekrarlanabiliyor; fiziksel başarı iddia edilmiyor.

**Kanıt:** v0.1 sürüm kaydı, temiz kurulum günlüğü, demo ve senaryo sonuçları.

**Beceri:** Entegrasyon kabulü, yeniden üretilebilirlik ve sürümleme.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-11 - Altı eklem için yük, aktüatör ve bütçe kararını ver

**Tahmin:** 10 saat | **Ön koşul:** ARM-10 | **Donanım:** Gerekmez

Donanım satın almadan önce erişim/yük/hız varsayımlarını gerçek geometri ve kütlelerle değerlendir.

**Uygulama:**

1. Hazır baskı kolunun link, motor, redüktör ve bilek kütlelerini topla; en kötü statik momentleri ve hareket payını hesapla.
2. 100 g toplam harici kütle ve yaklaşık 30 mm ağırlık merkezi varsayımını gözden geçir; gripper kütlesini dahil et.
3. Tork-hız eğrisi, redüksiyon, boşluk, sürücü, geri besleme, güç ve maliyeti karşılaştır; 10 mm/5° hedefleri için ölçüm yöntemini seç.

**Kabul:**

- [ ] Altı eklem için gerekçeli aktüatör/geri besleme tablosu, bütçe ve risk kaydı var; yalnız stall torkuyla seçim yapılmadı.
- [ ] Erişim/yük/hız/ivme ve hata hedefleri gerekçeyle korunmuş veya değişiklik önerisi olarak kaydedilmiş; satın alma listesi somut.

**Kanıt:** Moment hesabı, veri sayfaları, BOM, bütçe ve ölçüm yöntemi kararı.

**Beceri:** Yük hesabı, tork-hız, redüktör boşluğu ve ölçülebilir tasarım.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-12 - Hazır CAD tasarımını uyarlayıp baskı planını doğrula

**Tahmin:** 12 saat | **Ön koşul:** ARM-11 | **Donanım:** Gerekir

WE-R2.4 veya seçilen benzer tasarımı seçilen donanıma uydur; kaynak tasarımı özgün CAD çalışması diye sunma.

**Uygulama:**

1. Dosya sürümü/lisans/atıf kaydını tamamla; motor, yatak, redüktör, kablo geçişi ve bilek uyumunu denetle.
2. Kritik toleranslar için baskı kuponu veya tek eklem numunesi al; boşluk ve bağlantı uyumunu ölç.
3. Üretim/montaj sırasını ve ölçülecek eksen mesafelerini kaydet; değişen geometriyi robot tanımına geri işle.

**Kabul:**

- [ ] CAD ve BOM seçilen aktüatörle uyumlu; baskı kuponu/numune ölçüleri ve düzeltmeler kayıtlı.
- [ ] Kaynak tasarım, Arda’nın uyarlaması ve AI desteği ayrılmış; güncel model ile geometri farkları izlenebilir.

**Kanıt:** Atıflı CAD sürümü, uyarlama farkları, kupon fotoğrafı/ölçüleri ve baskı planı.

**Beceri:** Hazır tasarım uyarlama, imalat toleransı ve model tutarlılığı.

**Takılırsan:** Yazıcı/numune yoksa CAD inceleme ve BOM hazırlanabilir; fiziksel kupon ölçütü tamamlanmış sayılmaz. Bağımsız protokol taslağına geçilebilir.

## ARM-13 - Güç, STM32 köprüsü ve kontrol protokolünü tasarla

**Tahmin:** 12 saat | **Ön koşul:** ARM-11 | **Donanım:** Gerekmez

ROS yörünge yürütme arayüzü ile gerçek altı eklem arasında somut bir donanım sözleşmesi kur.

**Uygulama:**

1. Güç dağıtımı, sürücü/STM32 pinleri, haberleşme ve donanımdan bağımsız durdurma davranışını şemala.
2. FollowJointTrajectory → ros2_control donanım arayüzü veya eşdeğer sürücü → STM32 → altı sürücü zincirini seç ve gerekçelendir.
3. Eklem sırası/birimler, zamanlama, komut kimliği, onay, durum, hata, watchdog ve yeniden bağlantı sözleşmesini yaz.
4. Her durum alanını ölçülen, komutlanan veya tahmin edilen olarak işaretle; sensörsüz step sayacını gerçek açı diye sunma.

**Kabul:**

- [ ] Altı eklem için komut/durum mesajı, protokol sürümü, güç şeması ve kopma davranışı belirli.
- [ ] Ölçülen/komutlanan/tahmin edilen durum ayrımı açık; izinsiz veya yeniden bağlantıyla kendiliğinden hareket yok.

**Kanıt:** Elektrik/blok şeması, protokol sözleşmesi ve bridge mimari kararı.

**Beceri:** Gömülü sistem arayüzü, zamanlama ve durum verisinin kaynağı.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-14 - Gerçek köprüyü protokol emülatörüyle hata testine al

**Tahmin:** 10 saat | **Ön koşul:** ARM-09, ARM-13 | **Donanım:** Gerekmez

ARM-09’daki hazır mock kontrolcüden farklı olarak seçilen gerçek haberleşme protokolünü fiziksel kol olmadan dene.

**Uygulama:**

1. STM32/protokol emülatörüyle gerçek köprü paketlerini, altı eklem sırasını ve birimlerini doğrula.
2. Gecikmiş/kayıp/bozuk paket, kopma, watchdog, yeniden bağlanma ve eski komutu tekrar gönderme durumlarını uygula.
3. Plan/model/başlangıç durumu uyuşmazlığında yürütmenin engellendiğini ve hata sonucunun arayüze ulaştığını kaydet.

**Kabul:**

- [ ] Gerçek köprü sözleşmesiyle uçtan uca yörünge/durum/sonuç akışı çalışıyor; en az altı hata senaryosu kayıtlı.
- [ ] Kopma ve yeniden bağlantı yeni hareket başlatmıyor; emülatör sonucu fiziksel donanım başarısı olarak sunulmuyor.

**Kanıt:** Protokol emülatörü, bridge kayıtları ve hata senaryo tablosu.

**Beceri:** Protokol doğrulama, hata enjeksiyonu ve kontrollü toparlanma.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-15 - Tek eklemi düşük hızla ölçerek devreye al

**Tahmin:** 8 saat | **Ön koşul:** ARM-12, ARM-14 | **Donanım:** Gerekir

Tüm kolu hareket ettirmeden gerçek motor/sürücü/geri besleme zincirini doğrula.

**Uygulama:**

1. Sabitlenmiş tek eklemde güç ve kablo kontrolünü yap; yükü en aza indir ve durdurmayı dene.
2. Önce küçük açılar ve yaklaşık 1°/s ile yön, redüksiyon ve komut/ölçüm ilişkisini kontrol et.
3. Köprüden komut gönder; gerçek açıyı sensör veya bağımsız araçla ölç; akım/ısınma ve hata davranışını kaydet.

**Kabul:**

- [ ] Pozitif/negatif küçük hareket, durdurma ve kopma sonucu ölçülmüş; eklem yönü/ölçeği modele uyuyor.
- [ ] Komut ve gerçek açı ayrı kayıtlı; ölçüm olmadan doğruluk veya kapalı çevrim iddiası yok.

**Kanıt:** Tek eklem videosu, komut/ölçüm tablosu ve güç/ısınma notu.

**Beceri:** Devreye alma, ölçek/yön kontrolü ve bağımsız ölçüm.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-16 - Tek eklem kalibrasyon ve kontrolünü doğrula

**Tahmin:** 8 saat | **Ön koşul:** ARM-15 | **Donanım:** Gerekir

Tam montajdan önce tek eklemde tekrarlanabilir davranış elde et ve kullanılan kontrol katkısını açıkla.

**Uygulama:**

1. Sıfır/homing yöntemi, redüktör oranı, yön, limit ve hız/ivmeyi ölçüme göre kalibre et.
2. Aynı açıya iki yönden yaklaşmayı tekrarla; hata, tekrarlanabilirlik, boşluk ve sürüklenmeyi ayır.
3. Hazır sürücünün kontrolüyle Arda’nın yazdığı izleme/kontrol kodunu ayır; ölçüm gerekçesi varsa ayar değiştir.

**Kabul:**

- [ ] Tek eklem için önceden belirlenmiş açı toleransı ve tekrar koşulu sağlanmış veya açık sorun olarak raporlanmış; çözümsüzken tüm kol devreye alınmıyor.
- [ ] Kalibrasyon parametreleri, önce/sonra sonuç ve gerçek kontrol katkısı kayıtlı.

**Kanıt:** Kalibrasyon dosyası, tekrar ölçümleri ve kontrol katkısı notu.

**Beceri:** Kalibrasyon, boşluk, tekrarlanabilirlik ve kontrol katmanları.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-17 - Altı eklemli kolu monte et ve modelini güncelle

**Tahmin:** 16 saat | **Ön koşul:** ARM-16 | **Donanım:** Gerekir

Doğrulanmış tek eklem yaklaşımını tüm kola kontrollü biçimde taşı.

**Uygulama:**

1. Kaynak tasarıma uygun montajı, kablo paylarını, yatak/dişli boşluklarını ve taban sabitlemesini kontrol et.
2. Enerji verilecek eklemleri tek tek seç; diğerlerini destekle; her eklemde yön, ölçek ve durdurmayı dene.
3. Gerçek eksen mesafelerini, kütleleri ve limitleri ölç; URDF/çarpışma modeline farkları geri işle.

**Kabul:**

- [ ] J1-J6 tek tek kontrol edilmiş; mekanik/kablo çakışmaları ve limitler kayıtlı.
- [ ] Fiziksel montaj sürümü ve robot tanımı aynı geometriyi temsil ediyor; tüm kol eşzamanlı hareketi henüz kabul sayılmıyor.

**Kanıt:** Montaj fotoğrafları, altı eklem kontrol tablosu ve model fark kaydı.

**Beceri:** Montaj, sistematik kontrol ve fiziksel model eşleştirme.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-18 - Altı eklem sıfırını, limitleri ve TCP’yi kalibre et

**Tahmin:** 10 saat | **Ön koşul:** ARM-17 | **Donanım:** Gerekir

Planlayıcının başlangıç pozunu fiziksel kola bağla.

**Uygulama:**

1. Her eklem için homing/sıfır/ofset/limit prosedürünü uygula ve tekrar başlatma davranışını ölç.
2. Flanş→TCP dönüşümünü belirle; seçilen sabit takımın yönelim çerçevesini tanımla.
3. Kayıtlı durumu yalnız güncel referans ve geri besleme varsa yürütmeye hazır say; kalibrasyon değişince eski planları geçersiz kıl.

**Kabul:**

- [ ] Altı eklem kalibrasyonu ve TCP dönüşümü sürümlü; en az üç yeniden başlatma/homing tekrarı kayıtlı.
- [ ] Başlangıç durumu, veri kaynağı ve tazelik eşiği belirli; geçersiz kalibrasyonda yürütme kapalı.

**Kanıt:** Kalibrasyon dosyası, TCP yöntemi ve tekrar tablosu.

**Beceri:** Homing, ofset, takım çerçevesi ve kalibrasyon izlenebilirliği.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-19 - Önizlenen planı gerçek altı eklemde yürüt

**Tahmin:** 12 saat | **Ön koşul:** ARM-10, ARM-14, ARM-18 | **Donanım:** Gerekir

ArmPilot’un açık yürütme eylemini doğrulanmış fiziksel zincire bağla.

**Uygulama:**

1. Önce düşük hız ve küçük hareketlerle altı eklemi birlikte dene; simülasyon ve fiziksel modu görünür biçimde ayır.
2. Aynı model/sahne/kalibrasyon sürümündeki güncel başlangıçtan plan üret; önizlemeden sonra kullanıcı Yürüt eylemiyle gönder.
3. Gerçek/tahmin edilen durum, durdurma, haberleşme kopması ve yeniden başlatmayı kayıt altına al; hız artışını ölçümle gerekçelendir.

**Kabul:**

- [ ] En az üç fiziksel pozdan poza hareket önizlenen plan kimliğiyle izlenebiliyor; hedef değiştirmek eski planı yürütmüyor.
- [ ] Başlangıç uyuşmazlığı ve kesinti hareketi engelliyor/sonlandırıyor; sonuçlar arayüzde görülüyor, otomatik yeniden hareket yok.

**Kanıt:** Plan kimlikli fiziksel demo, yörünge/durum kayıtları ve hata denemeleri.

**Beceri:** Yürütme entegrasyonu, durum izleme ve kademeli doğrulama.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-20 - 10 poz × 3 tekrarda konum ve yönelimi ölç

**Tahmin:** 10 saat | **Ön koşul:** ARM-19 | **Donanım:** Gerekir

Fiziksel v1.0 tasarım hedeflerini bağımsız ölçümle değerlendir.

**Uygulama:**

1. Doğrulanmış çalışma alanından on hedef poz ve her biri için üç tekrar seç; yük, yaklaşım yönü ve hızı sabitle.
2. XYZ’yi bağımsız ölç; yönelimi bilinen takım/ölçüm düzeniyle değerlendir. Sensör/ölçüm çözünürlüğü ve belirsizliğini yaz.
3. Konum hatasını normla, yönelim hatasını bağıl dönmenin açısıyla hesapla; en büyük hata ve dağılımı 10 mm/5° hedefleriyle ayrı karşılaştır.

**Kabul:**

- [ ] 30 denemenin hedef/ölçülen pozları, ham verileri ve ölçüm yöntemi kayıtlı; komut değerleri gerçek ölçüm yerine geçmiyor.
- [ ] Geçerli kabul hedefleriyle konum ve yönelim ayrı değerlendirilmiş; hedef sağlanmadıysa başarı iddiası veya sessiz tolerans genişletme yok.

**Kanıt:** Ham veri, ölçüm düzeneği fotoğrafı, hata grafikleri ve kabul tablosu.

**Beceri:** Poz hatası, doğruluk/tekrarlanabilirlik ve ölçüm belirsizliği.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-21 - Ölçüme dayalı tek iyileştirmeyi karşılaştır

**Tahmin:** 6 saat | **Ön koşul:** ARM-20 | **Donanım:** Gerekir

Gözlenen bir hatanın nedenini test ederek iyileştir; yeni özellik ekleme.

**Uygulama:**

1. ARM-20’den baskın sorunu seç ve tek hipotez yaz; kalibrasyon, mekanik boşluk veya profil gibi bir değişken seç.
2. Değişikliği ve beklenen etkisini kaydet; aynı on poz/üç tekrar, yük ve ölçüm yöntemiyle yeniden dene.
3. Önce/sonra sonuçlarını ve yan etkileri değerlendir; faydasız değişikliği geri al veya sınırlamayı açıkla.

**Kabul:**

- [ ] Aynı koşullarla karşılaştırılabilir önce/sonra veri var; iyileşme yoksa da dürüst sonuç yazılı.
- [ ] v1.0 kabulü yeniden değerlendirilmiş; çözümsüz hedef ihlalleri sonraki belgelere taşınmış.

**Kanıt:** Hipotez/değişiklik kaydı ve karşılaştırmalı ölçüm.

**Beceri:** Deney tasarımı ve kanıta dayalı iyileştirme.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-22 - Kurulum, model ve öğrenme raporunu tamamla

**Tahmin:** 6 saat | **Ön koşul:** ARM-21 | **Donanım:** Gerekmez

Sistemi ve kişisel katkıyı bir başkasının izleyebileceği biçimde belgeye dönüştür.

**Uygulama:**

1. Yazılım/donanım sürümleri, BOM, model, kalibrasyon ve protokol kimliklerini eşleştir.
2. Kurulum, başlangıç, plan/önizleme/yürütme, durdurma ve sık hatalar için yönergeler yaz.
3. Arda’nın yazdığı öğrenme kodlarını, ürün entegrasyonunu, AI yardımını ve hazır CAD/kütüphaneleri ayrı kaynaklandır.

**Kabul:**

- [ ] Kurulum ve örnek senaryo yönergesi denenmiş; önemli parametreler/kalibrasyon sürümleri izlenebilir.
- [ ] Rapor ölçüm sonuçlarını ve sınırlamaları içeriyor; yapılmayan işler veya hazır çözümler özgün başarı diye sunulmuyor.

**Kanıt:** Güncel teknik/öğrenme raporu, kurulum yönergesi ve kaynak/katkı tablosu.

**Beceri:** Teknik raporlama, yeniden üretilebilirlik ve katkı açıklama.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-23 - ArmPilot’tan fiziksel ölçüme kadar demo hazırla

**Tahmin:** 6 saat | **Ön koşul:** ARM-22 | **Donanım:** Gerekir

Ürün davranışını ve öğrendiklerini somut bir demo ile anlat.

**Uygulama:**

1. Kendi masaüstü uygulamasında model görüntüleme, XYZ+yönelim girişi, plan ve önizlemeyi göster.
2. Geçerli hedefi açık yürütme eylemiyle fiziksel kola gönder; bir reddedilen hedefte yeni hareket olmadığını göster.
3. Fiziksel ölçüm sonucunu, bilinen sınırları ve kişisel katkını açıkla; sürüm/model kimliklerini videoya veya notuna ekle.

**Kabul:**

- [ ] Demo ArmPilot penceresinden fiziksel kola ve bağımsız ölçüme uzanıyor; yalnız RViz videosu değil.
- [ ] Başarı ve reddetme örneği ile Arda’nın FK/IK/entegrasyon açıklaması var; ölçülmemiş kapasite iddiası yok.

**Kanıt:** Demo videosu, senaryo listesi ve portföy özeti.

**Beceri:** Teknik sunum, sistem davranışı ve kişisel katkıyı açıklama.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## ARM-24 - v1.0 kabulünü kapat ve sonraki tek adımı seç

**Tahmin:** 4 saat | **Ön koşul:** ARM-23 | **Donanım:** Gerekmez

Ana sürümü kanıtıyla kapat; gelecek vizyonu kontrolsüz kapsam artışına dönüştürme.

**Uygulama:**

1. ARM-01 sözleşmesi ve varsa onaylı hedef değişikliklerini gerçek ölçümlerle karşılaştır; eksik kabul varsa önce düzelt.
2. v1.0 sürüm notu, bilinen sınırlar, arşiv ve commit/tag kaydını tamamla; karşılanmayan hedefi tamamlandı diye etiketleme.
3. Isı haritası, kamera otonomisi, lazer veya çizimden takım yolundan yalnız birini ayrı sonraki sürüm önerisi olarak gerekçelendir; uygulamaya başlama.

**Kabul:**

- [ ] v1.0 kabul tablosu, yazılım ve fiziksel kanıtlar eşleştirilmiş; açık zorunlu eksik yok.
- [ ] Sonraki işlev ayrı kapsam/onay bekleyen öneri; ana v1.0 içinde kamera/lazer/otonomi iddiası yok.

**Kanıt:** v1.0 sürüm kaydı, kabul matrisi ve sonraki sürüm önerisi.

**Beceri:** Kabul kapanışı, sürüm sınırı ve kapsam yönetimi.

**Takılırsan:** En küçük başarısız örneği ve beklenen/gerçekleşen sonucu kaydet. Eksik ön koşulu kapatmadan bağımlı göreve geçme.

## Kaynaklar

- [WE-R2.4 kaynak tasarım - LoboCNC](https://makerworld.com/tr/models/95279-we-r2-4-six-axis-robot-arm?from=search#profileId-318707)
- [MoveIt 2 mimari ve yürütme](https://moveit.picknik.ai/main/doc/concepts/move_group.html)
- [MoveIt Setup Assistant - URDF/SRDF](https://moveit.picknik.ai/main/doc/examples/setup_assistant/setup_assistant_tutorial.html)
- [MoveIt kontrolcü yapılandırması](https://moveit.picknik.ai/main/doc/examples/controller_configuration/controller_configuration_tutorial.html)
- [ROS 2 resmî belgeler](https://docs.ros.org/)
- [ros2_control resmî belgeler](https://control.ros.org/)
