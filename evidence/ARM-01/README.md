# ARM-01 kanıt ve katkı kaydı

15 Ekim 2026 | ARM-01 R2 belge kapanışı

## Kabul edilen kanıtlar

- [Arda'nın açtığı CAD montajı](we-r24-cad-montaj.png): Kullanıcının bu oturumda paylaştığı ekran görüntüsü değiştirilmeden kopyalandı. Orijinal hazır tasarım LoboCNC WE-R2.4'tür. Arda'nın katkısı montajı açmak/incelemek ve aday seçmektir; özgün CAD tasarımı veya tüm montaj ilişkilerini kendisinin kurduğu iddia edilmez.
- [WE-R2.4 açıklayıcı şeması](../../docs/references/wer24-joint-axes-reference.png): AI tarafından yayımlanmış bir WE-R2.4 uyarlamasının eklem parametrelerinden hesaplandı; Arda'nın el çizimi değildir. Kullanıcının CAD sürümüyle ölçü eşleştirmesi yapılmadı.
- [Kapsam sözleşmesi](../../docs/arm-01-kapsam.md) ve [tek sayfalık PDF](../../output/pdf/arm-01-kapsam.pdf).
- [Eklem açıklaması ve sayısal gerekçeler](../../docs/arm-01-tasarim-varsayimlari.md).

## Kabul ölçütünün değişmesi

Başlangıç kartı elle çizilmiş şema istiyordu. Kullanıcı çizim beklentisini anlamadığını belirterek şemayı AI'ın hazırlayıp ayrıntılı açıklamasını istedi ve kendi CAD görüntüsünü paylaştı. Bu açık talep doğrultusunda kanıt ölçütü CAD görüntüsü + AI şeması + katkı açıklaması olarak değiştirildi. Orijinal görev PDF'i veya site kartı bu oturumda düzenlenmedi; değişiklik yol haritası notunda kayıtlıdır.

## Katkı ve sınırlar

Arda kullanım senaryosunu yazdı, XYZ+yönelim kontrolünü seçti, konum/yönelim ayrımını doğru açıkladı, mekanik aday bağlantısını ve CAD montaj görüntüsünü sağladı. AI kaynak araştırmasını, şema/hesap örneklerini, sayısal tasarım önerilerini ve belge üretimini yaptı. Kullanıcının aktif süre tahmini **3 saat**; kronometre ölçümü değildir.

Şema, referans geometrinin gösterimidir. CAD dosyasının ölçüleri, bütün eklem mate'leri ve fiziksel limitleri kontrol edilmedi. Bağımsız FK/IK kodu, yük deneyi, motor testi veya fiziksel doğruluk sonucu yoktur. Arda'nın bağımsız eklem açıklaması ve hesap uygulaması henüz sınanmadı; bu kayıt onu yapılmış göstermez.
