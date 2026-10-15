# ArmPilot

Kendi imal edilecek 6 eksenli robot kolunu görüntülemek, XYZ ve uç yönelimi hedefleri için hareket planlamak, hareketi simülasyonda önizlemek ve fiziksel kolda yürütüp ölçmek için masaüstü uygulaması.

Proje sahibi: Arda TEKGÖZ. Geliştirme yöntemi: danışman desteğiyle uygulayarak öğrenme.

## Güncel durum

- Tamamlanan iş paketi: **ARM-01 - Kullanım senaryosu ve sürüm sözleşmesi (R2)**.
- Sonuç: Bir sayfalık kapsam PDF'i, sayısal tasarım varsayımları, kaynaklı eklem şeması ve kullanıcının CAD montaj kanıtı. Kullanıcı isteğiyle elle çizim ölçütü bu kanıtlarla değiştirildi.
- Sıradaki iş: **ARM-02 - Çalışma düzeni ve ortam uyumluluğu**; henüz başlanmadı.
- **R3 planı kullanıcı onaylıdır:** 24 görev, geçici 242 saat (ARM-10 yazılım kapısına kadar 112 saat). ARM-02 haftaya iki alt oturumla başlayacak; süreler ARM-02/04 sonrasında yeniden tahmin edilecek.
- Robot kolu, motor ve STM32 kartı henüz mevcut değil. Hazır baskı için somut aday LoboCNC'nin WE-R2.4 tasarımıdır; kesin dosya sürümü, eksen/ölçü doğrulaması ve aktüatör seçimi henüz tamamlanmadı. Motor/kart tedariki sonraki aşamalarda değerlendirilecek.
- Henüz çalıştırılabilir yazılım veya fiziksel doğrulama bulunmuyor.

## Belgeler

- [ARM-01 kapsam sözleşmesi](docs/arm-01-kapsam.md)
- [Bir sayfalık kapsam PDF'i](output/pdf/arm-01-kapsam.pdf)
- [Erişim, yük, hız ve eklem açıklamasının gerekçeleri](docs/arm-01-tasarim-varsayimlari.md)
- [Geliştirme ve öğrenme raporu](docs/rapor.md)
- [6 eksenli hedefe geçiş ve yol haritası revizyonu](docs/yol-haritasi-revizyonu.md)
- [24 ayrıntılı R3 görev kartı](docs/arm-gorevleri-r3.md)
- [Güncel proje raporu ve yol haritası PDF'i](output/pdf/arm-rapor-r3.pdf)
- [Onaylı plan verisi](docs/arm-roadmap-r3.json)
- [Canlı çalışma haritası](https://arda-mekatronik-calisma-haritasi.decent-cloud-1314.chatgpt.site/)
- [ARM-01 kanıtları](evidence/ARM-01/README.md)
- [Kaynaklı UR5 eklem eksenleri ve referans şema](docs/references/README.md)
- [WE-R2.4 mekanik aday incelemesi](docs/references/we-r24-candidate.md)

## ARM-01 geçici tasarım hedefleri

Yaklaşık 400 mm flanş erişimi; aday görev kutusu X=150-250, Y=-100...100, Z=150-250 mm; flanşa bağlı toplam 100 g harici kütle; eklem başına 5°/s ve 10°/s². Fiziksel konum/yönelim hedefleri 10 mm / 5° olarak önerildi. Bunlar AI danışman önerisidir; üreticinin kapasitesi veya ölçülmüş sonuç değildir. ARM-03, ARM-11 ve ARM-20'de gözden geçirilecek. Aktif çalışma süresi kullanıcı tahminiyle 3 saattir.

## Sürüm sınırları

Yazılım v0.1, kendi kol modelimizle hedef girişi ve hareket planının kinematik önizlemesini sunacak. v1.0 buna altı eklemli fiziksel yürütme, kalibrasyon ve bağımsız ölçümü ekleyecek. Kullanıcı v1.0'da XYZ yanında uç yönelimi seçmek istiyor; başlangıçta hazır yönelim seçenekleri kullanılabilir.

ROS 2 + MoveIt 2 + ros2_control önerilen altyapıdır; RViz geliştirme sırasında referans görselleştirici olarak kullanılabilir. ArmPilot'un kendine ait arayüzü ve görüntüleme katmanı ürünün parçasıdır. Isı haritası, kamera/otonomi ve lazer/çizimden takım yolu sonraki sürüm fikirleridir. Eski 138 saat tahmini yeni kapsamın tahmini değildir.

## Oturum yöntemi

1. Tek küçük görevin beklenen sonucunu ve gerekçesini konuş.
2. Kritik uygulamayı Arda yapsın ve kendi sözleriyle açıklasın.
3. Beklenen ve gerçekleşen sonucu karşılaştır; kanıtı kaydet.
4. Raporu gerçek katkı ve süreyle güncelle; kabul ölçütleri sağlanınca commit ve push yap.

NeuroKinematics bu projeden bağımsızdır.
