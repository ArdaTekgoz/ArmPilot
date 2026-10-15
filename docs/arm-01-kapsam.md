# ArmPilot / ARM-01 - Kullanım senaryosu ve sürüm sözleşmesi

15 Ekim 2026 | R2 | ARM-01 kapsamı tamamlandı | Arda TEKGÖZ / AI danışman desteği

## Amaç ve kullanım

WE-R2.4 hazır baskı tasarımı aday alınarak kurulacak altı döner eklemli tek kol için masaüstü uygulaması. Kullanıcı robotu 3B görür; hedef konum ve yönelimi seçer, hareketi planlayıp kinematik önizlemesini inceler ve ayrı yürütme eylemiyle fiziksel kola uygulatır. Geçerli plan yoksa açıklayıcı hata verilir, yeni hareket başlamaz. Fiziksel sonuç bağımsız ölçülür.

## Giriş ve çıkış

Giriş: XYZ (mm), uç yönelimi (ilk arayüzde hazır seçenekler olabilir), başlangıç eklem durumu, robot modeli/limitleri ve sabit sahne. Çıkış: zamanlı altı eklem yörüngesi, 3B önizleme, yürütme durumu ve kayıt. Komut, simülasyon ve gerçek ölçüm ayrı gösterilir. Referanslar ve yönelim gösterimi ARM-03'te kesinleşir; eski plan geçersiz hedefle yeniden tetiklenmez.

## Geçici tasarım hedefleri - kapasite garantisi değildir

| Özellik | İlk tasarım değeri / sınırı |
| --- | --- |
| Yaklaşık flanş erişimi | 400 mm varsayımı; CAD maksimum erişim ölçümü değil. |
| Aday görev kutusu | X=150-250, Y=-100...100, Z=150-250 mm; taban montaj merkezi, +Z yukarı. Her nokta/yönelim garanti değil; geçerlilik kontrolü şart. |
| Uç kütlesi | Flanşa takılan toplam 100 g; aparat ve nesne dahil. İlk test harici yüksüz; ağırlık merkezi flanştan yaklaşık 30 mm içinde varsayılır. |
| Hareket profili | Eklem başına 5°/s, 10°/s²; ilk küçük tek eklem denemesi 1°/s. TCP hız sınırı değildir. |
| Fiziksel doğruluk | En büyük konum hatası 10 mm, yönelim hatası 5° hedefi; garanti değil. |

Değerler AI danışman önerisidir; ölçülmüş üretici kapasitesi değildir. Geometri ARM-03, yük/motor ve hedef profil ARM-11, fiziksel sonuç ARM-20'de gözden geçirilecek. 10 geçerli hedef poz x 3 tekrar; yük, hız, ölçüm çözünürlüğü ve belirsizlik kayıtlı olacak. Hedef tutmazsa fiziksel başarı ilan edilmez.

## Sürüm sınırları

v0.1: Kendi modele uyarlanmış 3B gösterim, konum+yönelim hedefi, noktadan noktaya planlama, eklem/hız/ivme sınırları, öz çarpışma ve tanımlı masa/taban kontrolü, önizleme ve kayıt. Dinamik yük/esneme doğrulaması değildir. Önerilen altyapı: ROS 2 + MoveIt 2 + ros2_control; seçim/kurulum ARM-02'de.

v1.0: Kalibrasyon, altı eklemli fiziksel yürütme, durum/hata geri bildirimi ve bağımsız ölçüm eklenir. Kamera/otonomi, lazer, gripper aç-kapa, çizimden takım yolu, ısı haritası, neural IK ve çoklu robot sonraki sürümlerdedir.

## Kanıt ve katkı

Arda: senaryo, konum/yönelim açıklaması, mekanik aday ve CAD montaj görüntüsü; süre tahmini 3 saat. Kullanıcı talebiyle elle çizim yerine CAD görüntüsü + AI açıklayıcı şeması kabul edildi. AI: şema, sayısal öneriler ve dokümantasyon. CAD boyutları ve fiziksel kapasite doğrulanmadı. Ayrıntılar: docs/arm-01-tasarim-varsayimlari.md; evidence/ARM-01/README.md.
