# Yol haritası revizyonu - güncel R3

## R3 - Kullanıcı onaylı plan ve yayın eşitlemesi

15 Ekim 2026: Kullanıcı incelemede sunulan **sekiz revizyonu onayladı** ve çalışma haritasındaki ArmPilot görevleriyle raporun birlikte güncellenmesini istedi. Aşağıdaki R1/R2 bölümleri karar geçmişidir; oradaki "henüz güncellenmedi" veya "öneri" ifadeleri yazıldıkları zamana aittir. Güncel görev sözleşmesi [24 ayrıntılı R3 görev kartı](arm-gorevleri-r3.md), makine tarafından okunabilir kaynağı [R3 plan verisi](arm-roadmap-r3.json), paylaşılabilir rapor [R3 PDF](../output/pdf/arm-rapor-r3.pdf) içindedir.

| Onaylanan düzeltme | Uygulanan karşılığı |
| --- | --- |
| ARM-02 tek güne sıkışmayacak | Python/birim disiplini (~4 saat) ve ROS/MoveIt/UI ortam denemesi (~8 saat) ayrı alt oturumlar; ARM-02 haftaya başlar. |
| ARM-03–06 model/planlama eksiklerini kapat | Gerçek CAD ölçüleri, altı eklem, TCP, URDF/Xacro, SRDF, IK ve planlama yapılandırması; kişisel 2R FK/IK örnekleri korunur. |
| ARM-07 kendi ürün görünümünü teslim et | Kendi masaüstü penceresi, 3B kamera, eksen/TCP ve joint_states; RViz karşılaştırma aracıdır. |
| ARM-08 poz ve kullanıcı akışını tamamla | XYZ+yönelim, Planla → Önizle → Yürüt, simülasyon/fiziksel mod, plan/sahne/model/başlangıç geçerliliği. |
| ARM-09 gerçek planlama tanımını yap | Sabit modellenmiş sahnede çarpışma denetimli noktadan noktaya plan ve zamanlı yörünge; kişisel kübik örneği ayrı. |
| Mock kontrolcü v0.1'den önce gelsin | ARM-09 içine erken mock kontrolcü alt oturumu; ARM-10 bunu bekler. ARM-14 gerçek protokol emülatörü ve hata testleri olarak kalır. |
| ARM-13–20 donanım/ölçüm zincirini somutlaştır | Trajectory action → kontrolcü/köprü → STM32 → altı eklem; ölçülen/komutlanan/tahmin edilen durum, kalibrasyon, bağımsız konum/yönelim ölçümü. |
| Süre/bağımlılık ve belge eşleşmesini yenile | Geçici 242 saat, ARM-10'a kadar 112 saat; 24 kod korunur. ARM-12/13, ARM-11 sonrasında bağımsız yürüyebilir; ARM-15 iki kolun kanıtını bekler. |

**Tahminin sınırı:** 242 saat ilk planlama varsayımıdır; taahhüt veya ölçülmüş iş yükü değildir. Haftada 4 saatle yaklaşık 61 hafta, %25 pay senaryosuyla 76 hafta kapasite karşılığıdır; tedarik ve yeniden çalışma kesin bitiş tarihini belirsiz bırakır. ARM-02 ve ARM-04 sonunda yeniden tahmin edilir. ARM-01 için eski 4 saat tahmini korunur, gerçekleşen 3 saat kullanıcı tahmini ayrıca tutulur. Uzun görevler birden fazla haftalık oturuma bölünür.

**Kabul ve kayıt bütünlüğü:** Web görev kodları korunur. Eski tarayıcı kayıtlarının notları ve gerçek süreleri silinmez; önceki durum ve kabul kutuları revizyon arşivine alınır. Önceden ilerleme bulunan bir kartın değişen kabul kutuları yeniden doğrulanır; eski tamamlanma yeni kapsam için otomatik başarı sayılmaz. Bu işlem gerçek kullanıcı verileri okunarak veya ilerleme uydurularak yapılmaz; tarayıcıdaki kayıt açılışında uygulanır.

**Sürüm ayrımı:** Bugün plan/rapor/site güncellemesi yapılır. ARM-01 R2 kapanışı korunur; ARM-02 kurulumu veya öğrenme kodları başlamış sayılmaz. Orijinal 12 Ekim PDF'i tarihsel kaynak olarak değiştirilmez; yeni R3 raporu ayrı üretilir ve sitedeki ArmPilot rapor indirmesi güncel sürüme bağlanır.

## R1 - Altı eksenli ArmPilot (karar geçmişi)

Tarih: 15 Ekim 2026. Durum: Kullanıcının ürün hedefi güncellendi; aşağıdaki teknik mimari ve iş paketi içerikleri danışman önerisidir. Kurulum/uygulama yapılmış değildir.

## Değişiklik ve nedeni

Arda, ürünün kendi imal edeceği 6 eksenli kol için RViz benzeri kullanım sunan masaüstü uygulaması olmasını istedi: 3B gösterim, basit hareket ve hareket planlama, simülasyon önizlemesi, robota aktarım ve fiziksel test. Ek yanıtta v1.0 için XYZ + uç yönelimi seçimini belirtti; ilk arayüz hazır yönelimler sunabilir.

Bu talep, 12 Ekim tarihli başlangıç planındaki üç eklemli/yalnız konum kapsamının yerini alır. Eski plan tarihsel başlangıç kaynağıdır; güncel gereksinimle çelişen maddeleri uygulanmayacak. Mevcut PDF ve kullanıcının web sitesindeki görev kartları değiştirilmedi. Bu belge, o yol haritasını güncellemek için değişiklik kaydıdır.

15 Ekim ek netleştirme: Kullanıcı kolu tamamen sıfırdan tasarlamak yerine hazır baskı tasarımı veya benzer bir tasarım kullanacak; UR5 eklem yerleşimini referans istiyor. ARM-12, seçilen tasarımın lisans/kaynak kaydı, aktüatöre uyarlama, eksen/ölçü kontrolü ve baskı-montaj doğrulaması olarak ele alınacak. Kaynak tasarım kullanıcının özgün CAD tasarımı olarak sunulmayacak. Bu tercih, v1.0 işlevlerini değiştirmiyor; mekanik uygulama yöntemini netleştiriyor. Kesin model bağlantısı henüz verilmedi.

Sonraki kullanıcı yanıtında somut aday bağlantısı verildi: **WE-R2.4 (LoboCNC), MakerWorld 95279 / profil 318707**. Bu adayın UR3 esinli olduğu model açıklamasından görüldü; UR5 ile birebir sayısal eşleşme kabul edilmedi. Bağlantı ve doğrulama sınırları `docs/references/we-r24-candidate.md` içinde. Tam CAD montajı ARM-01'e eklenmedi; ARM-03'te gereken geometrik inceleme ile ARM-12'de detaylı uyarlama/montaj ayrımı korunuyor.

## R2 - ARM-01 kapanış netleştirmesi

15 Ekim 2026 kullanıcı talebi: Şemayı AI hazırlayıp açıklayacak; Arda montajlı CAD ekran görüntüsü sağladı. Böylece ARM-01'in elle çizim kanıtı, **CAD görüntüsü + kaynaklı AI açıklayıcı şeması + açık katkı kaydı** ile değiştirildi. Arda'nın kendisinin çizdiği veya bağımsız hesap yaptığı iddia edilmez. Kullanıcı ek bir el çizimi/mini sınav için bekletilmez; kinematik öğrenme uygulamaları sonraki görevlerde korunur.

ARM-01 için sayısal tasarım önerileri: yaklaşık 400 mm erişim, 100 g toplam harici uç kütlesi, 5°/s eklem hızı ve 10°/s² ivme; 10 mm konum ve 5° yönelim hata hedefi. Kaynaklardan doğrulanmış kapasite değil, gözden geçirilecek varsayımlardır. Aday görev kutusu ve gerekçeler `docs/arm-01-tasarim-varsayimlari.md` içinde. Bu belge aşaması tamamlandı; geometri, aktüatör yeterliliği ve fiziksel başarı henüz doğrulanmadı.

## Önerilen mimari ve öğrenme sınırı

| Bileşen | Görev / katkı |
| --- | --- |
| ArmPilot | Arda'nın arayüzü, 3B gösterimi, hedef girişi, plan/önizleme/yürütme akışı ve kayıtları. Kapsam tek robot. |
| Robot tanımı | Kendi robotumuzun link, eklem ekseni, limit ve çarpışma geometrisi; URDF/Xacro + planlama yapılandırması önerilir. |
| ROS 2 | Robot yazılım bileşenleri arasındaki mesaj, servis ve eylem haberleşmesi. |
| MoveIt 2 | Yapılandırılmış FK/IK, planlama sahnesi, çarpışma denetimi, yörünge işleme ve yürütme entegrasyonu. Kütüphane katkısı açık kaydedilecek. |
| ros2_control ve kontrolcü | Önerilen zamanlı eklem yürütme/donanım arayüzü. Uygun sürücü/STM32 köprüsü aktüatör ve haberleşme seçimine bağlıdır; doğrudan hazır uyum varsayılmaz. |
| RViz | Geliştirmede robot tanımı, plan ve durum karşılaştırması. ArmPilot'un kendi kullanıcı arayüzü/görüntülemesi ayrı iş paketidir. |

Arda küçük düzlemsel FK/IK ve zaman ölçekleme örneklerini kendisi uygulayacak; bunlar öğrenme ve karşılaştırma çalışmalarıdır. Üründeki altı eksenli IK/planlayıcı hazır bir bileşen olabilir. Bütün çözücünün Arda tarafından yazıldığı veya motorun dahili kontrolünün kendi PID'si olduğu iddia edilmeyecek. FK tarafında dönüşüm zinciri kademeli öğrenilecek ve robot modeliyle karşılaştırılacak.

İlk simülasyon teslimatında kinematik önizleme ve sahne/model çarpışma kontrolleri hedeflenir. Dinamik simülatör zorunluluğu önerilmemektedir; tork/esneme/temas doğrulaması ayrı gereksinimdir. ROS/Ubuntu dağıtımı, arayüz teknolojisi ve Windows ile birlikte çalışma biçimi ARM-02'de uyumluluk denemesiyle seçilecek. Bugün işletim sistemi kurulumu yapılmayacak.

## İş paketi eşlemesi - önerilen yeni içerik

Görev kodları izlenebilirlik için korunur. Üç eksenli örnekler ürün mimarisi yerine küçük öğrenme çalışması olarak kullanılır. Her görevin ayrıntılı kabul tablosu göreve başlamadan yazılacak; bu eşleme tamamlandı kanıtı değildir.

| Kod | R1 içeriği / kapanış kanıtı |
| --- | --- |
| ARM-01 | 6 eksenli ürün senaryosu, konum+yönelim sözleşmesi, taslak boyut/yük/hız, CAD görüntüsü + AI J1-J6 açıklayıcı şeması ve açık katkı kaydı, ölçülebilir başarı hedefleri. R2 kullanıcı talebiyle kapanış kanıtı değişti. |
| ARM-02 | Bağımsız depo ve Python birim örnekleri; ROS 2/MoveIt çalışma ortamı uyumluluk denemesi ve yeniden kurulum notları. Gerekirse birden fazla oturuma böl. |
| ARM-03 | Altı eklemin eksenleri/sıfırları, link geometrisi, TCP ve hedef referansı; ilk URDF/Xacro tanımı. |
| ARM-04 | Arda'nın FK öğrenme örnekleri ve kademeli dönüşüm zinciri; altı eklemli modelin bilinen duruşlarla karşılaştırması. |
| ARM-05 | Arda'nın 2R analitik IK öğrenme örneği; ürün için 6 eksenli IK yapılandırması ve FK ile geri doğrulama. Çözüm/başarısızlık örnekleri. |
| ARM-06 | Konum+yönelim erişimi, eklem sınırları, tekillik yakınları, öz çarpışma ve masa/taban modeli; beklenen/gerçekleşen örnek tablosu. |
| ARM-07 | ArmPilot'a ait ilk 3B görüntüleme; aynı robot tanımı, TCP, hedef, planlanan ve mevcut durum. RViz ile karşılaştırma. |
| ARM-08 | XYZ+yönelim arayüzü, model/plan kimliği ve hata mesajları; planlama/önizleme/fiziksel yürütme eylemlerini ayır. |
| ARM-09 | Kendi zaman ölçekleme öğrenme örneği; MoveIt ile noktadan noktaya planlama, hız/ivme ve çarpışma kontrolleri, önizleme ve reddetme örnekleri. |
| ARM-10 | Kendi 6 eksenli modelimizle ArmPilot v0.1 demosu; temiz kurulum, başarılı/reddedilen hedefler ve kayıtlar. Referans robot demosu tek başına bu teslimatı kapatmaz. |
| ARM-11 | Altı eklem ve bilek dahil kütle/moment/bütçe, aktüatör-geri besleme karşılaştırması; yük, konum/yönelim toleransı ve ölçüm yöntemini gözden geçir. |
| ARM-12 | Seçilen hazır baskı/CAD tasarımının kaynak-lisans kaydı; aktüatör/yataklama/kablo/bilek uyarlaması, kupon, eksen mesafesi ve montaj doğrulaması. |
| ARM-13 | Güç, kontrolcü ve protokol; ROS 2 yürütme arayüzü ile donanım arasındaki köprü, gerçek/komut durumu ve kesinti davranışı. |
| ARM-14 | Sahte donanım/kontrolcüyle altı eklemli yörünge akışı; gecikme, kopma, eski plan, geçersiz hedef ve başlangıç durumu uyuşmazlığı örnekleri. |
| ARM-15 | Tek eklemde düşük yükle ölçümlü devreye alma; komut ve gerçek açı ayrımı. |
| ARM-16 | Tek eklem kontrol/kalibrasyon doğrulaması; kullanılan kontrol katkısının açıklanması. |
| ARM-17 | Altı eklemin mekanik montajı ve tek tek kontrolü; ölçülen geometriyle model güncelleme. |
| ARM-18 | Altı sıfır/limit ve TCP kalibrasyonu; başlangıç prosedürü ve tekrar ölçümleri. |
| ARM-19 | Önizlenmiş planın fiziksel altı eklemde kademeli yürütülmesi; durum, durdurma ve kesinti sonuçları. Plan başlangıcı güncel durumla eşleşmeli. |
| ARM-20 | 10 hedef poz x 3 tekrar; XYZ konum hatası ve yönelim hatası ayrı, ölçüm yöntemi/çözünürlük/belirsizlik belgeli. Konum ve yönelim toleranslarıyla karşılaştırma. |
| ARM-21 | Gözleme dayalı bir değişiklik; aynı hedef poz setiyle önce/sonra karşılaştırma. |
| ARM-22 | Model, yazılım, donanım, kalibrasyon ve arıza/kurulum belgelerini eşleştirme. |
| ARM-23 | ArmPilot arayüzünden önizlemeye, fiziksel harekete ve ölçüme demo; Arda/AI/kütüphane katkı ayrımı. |
| ARM-24 | v1.0 kabul kapanışı; sonraki sürüm için tek ayrı işlev önerisi. |

## Sürüm dışı fikirler ve takvim etkisi

Isı haritası, çizimden takım yolu, lazer kesici ve kamerayla otonomi sonraki sürüm listesine kaydedildi. Gelecek takım yolu çalışması, noktadan noktaya harekete ek olarak Kartezyen yol ve proses gereksinimleri doğurur; bugünkü kabul ölçütü değildir.

Eski 138 saat toplamı ve 56 saat yazılım teslimatı tahmini R1'e taşınmaz. Altı eksen, robot tanımı, planlama entegrasyonu, özgün arayüz ve fiziksel bilek ek çalışma gerektirir. Güncel tahminler ARM-01 kapsamı ve ARM-02 uyumluluk denemesi netleşince yeniden çıkarılacak; yeni bitiş tarihi verilmedi.

## Resmî teknik dayanaklar

- [MoveIt ile RViz'de planlama/önizleme](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html): RViz görselleştirme, MoveIt planlama eklentisi ve ayrı plan/yürütme işlemleri.
- [MoveIt kontrolcü yapılandırması](https://moveit.picknik.ai/main/doc/examples/controller_configuration/controller_configuration_tutorial.html): FollowJointTrajectory ve kontrolcü entegrasyonu; sahte donanımla kinematik simülasyon.
- [MoveIt resmî SSS](https://moveit.ai/documentation/faqs/): ROS 2 ilişkisi ve desteklenen Linux ortamı için başlangıç bilgisi. Kesin dağıtım/sürüm ARM-02'de ayrıca doğrulanacak.
