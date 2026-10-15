# ArmPilot - Geliştirme ve öğrenme raporu

Proje sahibi: Arda TEKGÖZ | Başlangıç: 15 Ekim 2026 | Durum: ARM-01 R2 tamamlandı; R3 planı onaylandı; ARM-02 haftaya başlayacak

Bu belge çalışma boyunca güncellenecek teknik raporun kaynağıdır. Yapılmamış uygulamalar ve ölçümler sonuç olarak yazılmaz. Tamamlanan aşamalarda amaç, yöntem, karar gerekçeleri, sonuçlar ve sınırlamalar biriktirilir.

## 1. Amaç ve teslimatlar

Güncel R1 hedefi: Kendi imal edilecek 6 eksenli kol için masaüstü ArmPilot uygulaması; 3B robot gösterimi, XYZ + uç yönelimi hedefi, hareket planlama, simülasyon önizlemesi ve kullanıcı eylemiyle fiziksel yürütme. Önce donanımsız v0.1, ardından fiziksel ölçümle değerlendirilecek v1.0 hedeflenir. Önceki üç eklemli/yalnız konum kapsamı kullanıcının 15 Ekim açıklamasıyla değişmiştir.

Öğrenme hedefi: Arda'nın gereksinimleri gerekçelendirmesi, kritik hesap ve kodları kendisinin uygulaması, beklenen sonuçlarla gerçek sonuçları karşılaştırması ve katkısını açıklayabilmesi.

## 2. Başlangıç kaynağı ve plan

Kaynak: Kullanıcının sağladığı **ArmPilot Proje Raporu ve Yol Haritası**, 12 Ekim 2026, 16 sayfa. Özellikle s. 1-3 genel kapsam, s. 4 ARM-01, s. 16 kayıt şablonu başlangıçta temel alınmıştır. Kaynak dosya yerel olarak incelenmiştir; bu depoya eklenmemiştir ve değiştirilmemiştir. Aşağıdaki tablo eski kapsamın tarihsel tahminidir. Güncel ürün hedefi ve görev içeriklerine etkisi `docs/yol-haritasi-revizyonu.md` içinde kayıtlıdır. Kullanıcı onaylı R3 görevleri `docs/arm-gorevleri-r3.md`, güncel PDF `output/pdf/arm-rapor-r3.pdf` içindedir; web kartları aynı R3 plan verisinden güncellenir.

| Aşama | İş paketleri | Başlangıç tahmini |
| --- | --- | --- |
| Kapsam ve temel | ARM-01-02 | 8 saat |
| Kinematik | ARM-03-06 | 26 saat |
| Kullanılabilir yazılım | ARM-07-10 | 22 saat |
| Fiziksel tasarım | ARM-11-14 | 22 saat |
| Kontrol ve montaj | ARM-15-18 | 26 saat |
| Fiziksel demo ve kapanış | ARM-19-23 | 30 saat |
| Kontrollü devam | ARM-24 | 4 saat |

Eski kapsamın toplam ilk tahmini 138 saat, ilk yazılım teslimatı tahmini 56 saattir. Bu değerler altı eksenli kapsam için geçersizdir. R3'te geçici toplam 242 saat, donanımsız yazılım kapısına kadar 112 saat öngörülür; bunlar ölçülmüş süre veya taahhüt değildir. ARM-02 ve ARM-04 sonunda yeniden tahmin edilir. Ön koşullar ve kanıtlar ilerlemeyi belirler. Donanım alımı yük/bütçe değerlendirmesine, tüm kol devreye alma ise tek eklem doğrulamasına bağlıdır.

## 3. Karar günlüğü

| Tarih | Karar | Dayanak / durum |
| --- | --- | --- |
| 2026-10-15 | ArmPilot bağımsız bir public GitHub reposunda ilerleyecek. | Kullanıcının doğrudan tercihi. |
| 2026-10-15 | Küçük uygulama, açıklama, inceleme ve rapor sırasıyla danışmanlık yöntemi uygulanacak. | Kullanıcı NeuroKinematics'teki kapsam büyümesinin yaparak öğrenmesini zorlaştırdığını belirtti. |
| 2026-10-15 | Kol sıfırdan imal edilecek; motor ve STM32 kartı henüz mevcut değil. | Kullanıcının beyanı. ARM-01 donanım gerektirmiyor. |
| 2026-10-15 | Masaüstü arayüzüne XYZ hedefi mm girilecek; önce simülasyon, sonra fiziksel kol hedeflenecek. Ulaşılamayan hedefte hata gösterilecek ve hedef hareket başlatmayacak. | Arda'nın kendi kullanım senaryosu; ARM-01 ve ARM-08 ile uyumlu. |
| 2026-10-15 | Yol haritasıyla uyum izlenecek; değişiklik önerileri açıkça belirtilecek ve gerekçesi kaydedilecek. | Kullanıcının doğrudan talebi. İlk senaryo değişiklik gerektirmiyordu; sonraki 6 eksen talebi R1 değişikliğini doğurdu. |
| 2026-10-15 | Ürün 6 eksenli kendi kolumuz için 3B gösterim, planlama, simülasyon önizlemesi ve fiziksel yürütme uygulaması olarak yeniden tanımlandı. | Kullanıcının açık kapsam değişikliği. Fotoğraflar görsel referans; kendi kolunun doğrulanmış mekanik tasarımı değil. |
| 2026-10-15 | v1.0'da XYZ + uç yönelimi hedefi; başlangıçta hazır yönelim seçenekleri kullanılabilir. | Kullanıcının doğrudan yanıtı. |
| 2026-10-15 | Isı haritası, çizimden takım yolu, lazer ve kamera/otonomi sonraki sürüm fikirleri olarak kaydedildi. | Kullanıcının gelecek vizyonu; v1.0 kabulüne eklenmedi. |
| 2026-10-15 | ROS 2 + MoveIt 2 + ros2_control, özgün ArmPilot arayüzü/görüntülemesi ve geliştirme için RViz önerildi. | AI danışman önerisi; resmî kaynaklar revizyon belgesinde. Kurulum/sürüm seçimi yapılmadı. |
| 2026-10-15 | Hazır baskı tasarımı veya benzer hazır tasarım kullanılacak; UR5 eklem yerleşimi referans alınacak. | Kullanıcının son tercihi, ilk sıfırdan tasarım beyanını güncelliyor. Kesin model henüz seçilmedi. |
| 2026-10-15 | J4 açıklaması UR5 için düzeltildi: wrist_1_joint, ekseni J2-J3'e paralel; uzun önkolun boyuna dönüşü değil. J5-J6 komşu eksen ilişkileri resmî robot tanımından doğrulandı. | Önceki genel mimari anlatımı UR5'e uygulanamazdı. Kaynaklı görsel ve hesap: docs/references/README.md. |
| 2026-10-15 | Somut baskı adayı WE-R2.4 / LoboCNC, MakerWorld 95279 / profil 318707 olarak belirtildi. Tam CAD montajı bugün gerekli görülmedi. | Kullanıcı bağlantıyı sağladı ve STL/SLDPRT parçaları bulunduğunu belirtti. Model sayfası UR3 esinli tasarım diyor; gerçek dosya/eksen doğrulaması henüz yok. |
| 2026-10-15 | Elle çizim ölçütü CAD montaj görüntüsü + AI açıklayıcı şeması ve açık katkı kaydıyla değiştirildi. | Kullanıcı CAD görüntüsünü sağlayıp şemayı AI'ın hazırlayarak açıklamasını açıkça istedi. R2 kaydı; özgün görev PDF'i/site kartı bu oturumda değiştirilmedi. |
| 2026-10-15 | Yaklaşık 400 mm erişim, 100 g toplam harici uç yükü, 5°/s ve 10°/s² tasarım profili; 10 mm / 5° fiziksel hata hedefleri. | AI danışman önerisi; üretici kapasitesi veya ölçüm sonucu değil. ARM-03/11/20'de gözden geçirilecek. |

## 4. ARM-01 oturumu - 15 Ekim 2026

**Kapanış sonucu (R2):** Bir sayfalık kapsam PDF'i, Arda'nın CAD montaj ekran görüntüsü, AI tarafından hesaplanmış/açıklanmış WE-R2.4 eksen şeması, gerekçeli sayısal tasarım varsayımları ve yol haritası değişiklik kaydı. Git kapanış kaydı main dalındaki ARM-01 commit'idir.

**İlk planlanan çalışma:** Aşağıdaki 4 saat dağılımı R1 öncesi başlangıç önerisidir; kapsam görüşmesiyle eklenen süre henüz ölçülmedi. Gerçekleşen süre olarak kaydedilmez.

| İş | Tahmin | Çıktı |
| --- | --- | --- |
| Kullanım senaryosu ve giriş/çıkış/hata davranışı | 40 dk | Arda'nın kendi cümleleriyle senaryo |
| Görev uzayı, serbestlik derecesi ve elle kol şeması | 50 dk | Etiketli çizim ve kısa açıklama |
| Çalışma alanı, erişim, yük ve hız varsayımları | 50 dk | Değer, birim ve gerekçe tablosu |
| Sürüm sözleşmesi ve kabul incelemesi | 40 dk | Son kapsam belgesi |
| Teknik rapor, katkı ve kanıt kaydı | 35 dk | Oturum kaydı |
| Git fark incelemesi, commit ve push | 25 dk | Yerel ve uzak commit doğrulaması |

### Katkı ve gerçekleşenler

- Arda: İlk senaryoyu kendi cümleleriyle yazdı. Konumu "ucun XYZ'de nerede olduğu", yönelimi "hangi yöne baktığı" olarak doğru açıkladı. Altı eksenli kol, özgün görüntüleme/planlama uygulaması ve fiziksel yürütme hedefini netleştirdi; XYZ + yönelim seçimini yaptı. WE-R2.4 bağlantısını sağladı ve CAD montajını açıp ekran görüntüsünü paylaştı. Özgün mekanik tasarım veya bütün CAD mate'lerini kendisinin kurduğu iddia edilmedi.
- AI: Senaryoyu düzenledi, mimari/yol haritası revizyonu hazırladı; kaynaklı UR5 ve WE-R2.4 eksen şemalarını hesaplayıp açıklamalarını yazdı. Sayısal tasarım önerilerini ve moment/hız örneklerini gerekçelendirdi. Tek sayfalık PDF'i üretip render ederek inceledi; kaynak ve katkı ayrımını kaydetti. Arda'nın bağımsız hesap veya çizimi olarak sunulmadı.
- Altyapı: Public `https://github.com/ArdaTekgoz/ArmPilot` reposu ve yerel `main` dalı kuruldu. Kapanış commit'inde kapsam, rapor, kaynaklar ve kanıtlar birlikte saklanır; commit kimliği `git log` üzerinden izlenir.
- Aktif çalışma süresi: **3 saat**, kullanıcı tahmini; kronometre ölçümü değildir. İlk 4 saat önerisine göre 1 saat daha kısa; revize kapsam için verimlilik çıkarımı yapılmaz.
- Kullanıcının kendi cümleleriyle doğru açıkladığı konu: Uç konumu ile yönelim ayrımı. Altı eklem/eksen açıklaması henüz değerlendirilmedi.
- Ölçüm veya deney sonucu: Henüz yok.

### Kullanım senaryosu incelemesi

Beklenen: Kullanıcı, girdi/birim, geçerli hedef sonucu ve ulaşılamayan hedef davranışının tanımlanması.

Gerçekleşen: Dört unsur Arda tarafından yazıldı ve `docs/arm-01-kapsam.md` içine işlendi. Belge incelemesi düzeyinde bu alt adım tamamlandı; çalışan arayüz veya hareket testi yapılmadı. Yazılımda açı ve zamanlı simülasyon çıktısı, fiziksel sürümde gerçek hareket ve ayrı ölçüm değerlendirmesi korunuyor.

Netleştirme: "Hareket etmemeli" ifadesi, reddedilen hedefin yeni hareket başlatmaması olarak kaydedildi. Devam eden hareketin durdurulması/yeni hedefin kabulü henüz kararlaştırılmadı. Bu konu mevcut ARM-08-09 ve ARM-13/19 arayüz-kontrol çalışmalarında netleştirilecek; yeni iş paketi eklenmedi ve yol haritası değiştirilmedi.

Bu inceleme ilk senaryoya aittir. Sonraki altı eksen ve XYZ+yönelim talebiyle R1 revizyonu açılmıştır; güncel sözleşme `docs/arm-01-kapsam.md`, etki/görev eşlemesi `docs/yol-haritasi-revizyonu.md` içindedir. Planlama/çarpışma kontrolleri, özgün 3B görüntüleme ve konumun yanında yönelim ölçümü yeni planın açık değişiklikleridir. Eski tam çözücüyü kendin yazma yaklaşımı, küçük kişisel öğrenme örnekleri + hazır planlayıcıyı doğrulayarak kullanma önerisiyle değişmiştir.

### UR5 referans şeması incelemesi

Arda J1-J6 eksen ve dönüşlerini, özellikle bilek eklemlerini gösteren örnek istedi. AI resmî UR5 Xacro ve ideal kinematik dönüşümlerini inceleyip tam kol + bilek ayrıntılı şema oluşturdu. Eksenler yerel çerçeveden taban çerçevesine taşındı; paralellik/diklik ilişkileri sayısal olarak doğrulandı. Bu görsel öğretici referanstır, Arda'nın çizimi olarak kabul edilmedi. Kullanıcı baskı tasarımı seçimine geçtiğinden özgün CAD yerine kaynak tasarım/uyarlama katkısı ayrı raporlanacak. Şema ve kaynaklar `docs/references/README.md` içinde.

### WE-R2.4 aday incelemesi

Kullanıcı MakerWorld bağlantısını verdi ve gerekirse bugün CAD montajı yapabileceğini söyledi. AI modelin kendi açıklamasını tarayıcıdan okudu; UR3 esinli altı step motor/redüktör ünitesi yaklaşımını ve ayrı aktüatör bağlantısını kaydetti. Ayrıca bir proje ekibinin yayımladığı ROS 2 / ESP32 uygulaması ve robot tanımı bulundu. Bunlar teknik referans olarak kaydedildi; kod/donanım seçimi yapılmadı. Dosya envanteri, SLDPRT içeriği ve tam eksen zinciri doğrulanmadı. Tam CAD montajı ARM-01'e yeni ön koşul yapılmadı. İnceleme ve kaynaklar: `docs/references/we-r24-candidate.md`.

### ARM-01 kapanış durumu

- [x] Bir sayfalık son kapsam PDF'inde giriş, çıkış ve sürüm dışı işler var; sayfa sayısı ve görsel düzen kontrol edildi.
- [x] 10 mm konum ve 5° yönelim hatasının tasarım hedefi olduğu, garanti olmadığı açık yazıldı.
- [x] R2 kanıtı: CAD montaj görüntüsü + AI J1-J6 eksen şeması; flanş/TCP ayrımı açıklama belgesinde.
- [x] Çalışma alanı, erişim, uç kütlesi, hız/ivme değerleri birimleri ve gerekçeleriyle taslak olarak kayıtlı.
- [x] Arda konum/yönelim farkını kendi sözleriyle doğru açıkladı.
- [x] Konum/yönelim için hedefler ve 10 poz x 3 tekrar ölçüm yaklaşımı taslak olarak kayıtlı.
- [x] Kullanıcı tahmini süre, kişisel katkı ve AI yardımı güncellendi.

**Öğrenme sınırı:** Altı eklemin bağımsız açıklaması, FK/IK hesabı ve kod uygulaması henüz sınanmadı. Kullanıcının son isteğiyle ARM-01'de AI açıklaması sunuldu; ek el çizimi veya sınav ön koşulu konmadı. Sonraki kinematik görevlerde kişisel uygulama korunur.

**Doğrulama sınırı:** Referans Xacro/YAML zinciriyle çizilen eksenlerin paralellik/dikliği hesapla kontrol edildi. Kullanıcının yerel CAD boyutları, bütün montaj ilişkileri, yük kapasitesi ve fiziksel konum/yönelim doğruluğu doğrulanmadı. İlk aday incelemesindeki eksen zinciri belirsizliği, yayımlanmış referans zinciri için çözüldü; kullanıcı CAD'iyle eşleştirme ARM-03'te kalıyor.

**Açık iş / sıradaki adım:** ARM-02'de Python birim disiplini ve ROS 2/MoveIt ortam uyumluluğu; ARM-03'te gerçek CAD geometri eşleştirmesi. Donanım satın alma/üretim ve fiziksel başarı ileri aşamalardadır. ARM-01 belge aşaması tamamlandı.

## 5. Sonraki oturumlar için kayıt biçimi

Her oturum: tarih ve görev kodu; amaç/beklenen davranış; yöntem; karar ve gerekçesi; Arda'nın uygulaması; AI/kütüphane yardımı; beklenen/gerçekleşen sonuç; kanıt yolu; gerçek süre; açıklanabilen konu; açık sorun ve sonraki adım.

## 6. R3 plan ve çalışma haritası güncellemesi - 15 Ekim 2026

**Yetki ve amaç:** Arda, yol haritası incelemesinde sunulan sekiz değişikliği onayladı ve kendi çalışma haritasındaki görevlerle raporun birlikte güncellenmesini istedi. Kapsam değişikliği sessizce yapılmadı. Tam değişiklik tablosu `docs/yol-haritasi-revizyonu.md` başındaki R3 kaydında.

**Yapılan iş:** 24 görevin amaç, adım, ön koşul, kabul, kanıt, öğrenme ve donanım bekleme davranışları yenilendi. ARM-02 iki alt oturuma ayrıldı; robot tanımı ve MoveIt yapılandırması açık kabul oldu. ArmPilot'un kendi masaüstü/3B görünümü, XYZ+yönelim, plan/önizleme/yürütme, erken mock kontrolcü, gerçek protokol köprüsü ve bağımsız poz ölçümleri zincire işlendi. ARM-09'daki mock denemesi ARM-10'dan önce; ARM-14 gerçek protokol hata testidir. Görev kodları ARM-01–24 olarak korundu.

**Katkı:** Arda ürün hedefini, öğrenme yöntemini, kapsam değişikliğini ve site/rapor güncellemesini onayladı. AI onaylı plan metinlerini, doküman/PDF üretimini ve site entegrasyonunu hazırladı. Arda'nın öğrenme kodlarını yazdığı, ortam kurduğu veya fiziksel deney yaptığı iddia edilmedi.

**Süre:** ARM-01 için daha önce verilen 3 saat kullanıcı tahmini korunur. Bu plan güncellemesinin ek insan çalışma süresi henüz ölçülmedi; toplam süreye uydurma değer eklenmedi.

**Güncel plan:** `docs/arm-roadmap-r3.json` yapılandırılmış kaynak; görev kartları, R3 PDF ve site ArmPilot verisi onunla eşleştirilir. Diğer iki projenin görev/rapor içeriği korunur. Site tarayıcı kayıtlarında eski kabul işaretleri yeni ölçütlere doğrudan taşınmaz; not/süre ve önceki durum arşivde korunur. İlerlemiş revize kartların yeni kabulü tekrar doğrulanır. Sunucudan kişisel ilerleme okunmadı ve tamamlanma uydurulmadı.

**Sıradaki çalışma:** ARM-02 haftaya. Önce Arda'nın birim dönüşümleri ve Python/Git küçük örneği; sonra resmî sürüm uyumluluğu ve ROS/MoveIt/UI ortam denemesi. Bugün ARM-02 uygulamasına geçilmedi.

**Yayın ve doğrulama sonucu:** Mevcut çalışma haritası https://arda-mekatronik-calisma-haritasi.decent-cloud-1314.chatgpt.site/ üzerinde **site sürümü 2**, kaynak commit'i `a11ba5bd888d8ee2804774e128c8a8323a9d021c` ile yayınlandı; Sites sonucu `succeeded`. Erişim kitlesi değişmedi. 24 görev ve bağımlılık döngüsüzlüğü, 242 saat toplamı, JSON/site/PDF eşleşmesi, diğer iki projenin içerik ve PDF'lerinin korunması doğrulandı. R3 PDF'in 28 sayfası render edilip incelendi. Tarayıcıda görev/not/süre/tamamlama akışı, sayfa yenilemede kalıcılık ve rapor kartı kontrol edildi; eski kayıt taşıma testleri geçti. Kanıt ve tekrar komutları: `evidence/roadmap-r3/README.md`. Bu kontroller robot yazılımı veya fiziksel başarı testi değildir.
