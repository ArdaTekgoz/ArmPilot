# ArmPilot çalışma düzeni

Bu proje, Arda'nın uygulayarak robotik ve yazılım öğrenmesi için geliştiriliyor.

- Danışman gibi ilerle: kısa açıklama ve gerekçe ver, tek küçük uygulama iste, sonucu incele ve geri bildirim ver.
- Arda'nın kullanım senaryosunu, tasarım gerekçelerini ve öğrenme için seçilen FK/IK/yörünge uygulamalarını onun yerine tamamlayıp teslim etme. Ürün içinde kullanılan hazır çözücü/planlayıcı ile Arda'nın yazdığı öğrenme örneğini ayır. İskelet, açıklama ve hata incelemesiyle destekle.
- Kullanıcının güncel talimatları bu çalışma düzeninden önceliklidir. Altyapı ve rutin dokümantasyon işlerini yetki kapsamında yap; her adım için onay isteme.
- Aktif iş paketi ve açık işler için README.md ile docs/rapor.md dosyalarını oku. Kabul kanıtı olmadan tamamlandı yazma.
- Güncel kullanıcı hedefi: Kendi imal edeceği 6 eksenli kol için masaüstü ArmPilot arayüzü, 3B gösterim, XYZ + uç yönelimi hedefi, hareket planlama/önizleme ve ardından fiziksel yürütme. Önceki 3 eksenli/yalnız XYZ kapsamı 15 Ekim 2026 kullanıcı talebiyle değişti; eski sınırlamayı yeniden dayatma.
- Değişiklik kaydı ve görev eşlemesi docs/yol-haritasi-revizyonu.md içindedir. ROS 2 + MoveIt 2 + ros2_control mimarisi danışman önerisidir; kurulum ve sürüm seçimi henüz yapılmadı.
- Mekanik tercih güncellendi: Hazır baskı alınacak veya benzer hazır tasarım kullanılacak; somut aday WE-R2.4, yerel CAD geometrisi henüz doğrulanmadı. UR5'te J2-J3-J4 paralel; J4 önkolun boyuna dönüşü değildir. Doğrulanmış eksen referansı docs/references/README.md içindedir.
- Kullanıcının somut baskı adayı WE-R2.4 (LoboCNC), MakerWorld 95279 / profil 318707. İnceleme: docs/references/we-r24-candidate.md. Tasarımcı UR3 esinli olduğunu söylüyor; UR5 sayısal geometrisini bu modele taşımayın. CAD dosya/eksen uyumu henüz doğrulanmadı; ARM-01 için tam CAD montajını şart koşmayın.
- ARM-01 R2: Kullanıcı elle çizim yerine AI'ın şema hazırlayıp açıklamasını istedi; CAD montaj görüntüsü + AI şeması kanıt olarak kabul edildi. Tekrar el çizimi veya ek sınavı kapanış ön koşulu yapmayın. Bağımsız eklem/hareket açıklaması henüz sınanmadı; bunu başarı diye yazmayın. Sayısal tasarım hedefleri docs/arm-01-kapsam.md ve gerekçeleri docs/arm-01-tasarim-varsayimlari.md içindedir; bunlar ölçülmüş kapasite değildir.
- Isı haritası, çizimden takım yolu, lazer ve kamerayla otonomi sonraki sürüm fikirleridir. v1.0'a sessizce ekleme.
- Yazılım v0.1, fiziksel v1 ve yalnız tasarım varsayımı olan değerleri açıkça ayır.
- NeuroKinematics bağımsız projedir; dosyalarına müdahale etme ve mevcut büyük kod tabanını buraya taşıma.
- Her oturumda karar, gerekçe, Arda/AI katkısı, doğrulama, kanıt ve gerçek süreyi rapora ekle. Bilinmeyenleri uydurma.
- Haftalık iş paketleri bitiş ölçütleriyle kapanır. Donanım yokken fiziksel başarı veya ölçüm iddiası yazma.
- Başlangıç raporundaki yol haritasıyla uyumu koru. Kapsam, görev sırası veya kabul ölçütü değişikliği önerdiğinde bunu açıkça değişiklik önerisi olarak belirt ve gerekçesini kaydet; yol haritasını sessizce değiştirme.
- R3 kullanıcı onaylıdır: docs/arm-roadmap-r3.json ve docs/arm-gorevleri-r3.md güncel görev kaynağıdır. 242 saat/112 saat yazılım bütçesi geçici tahmindir, ARM-02/04 sonunda yenilenir. ARM-02 haftaya iki alt oturumla başlar; eski 3DOF/138 saat görevlerini geri getirme. Diğer iki projenin içeriklerine müdahale etme.
- ARM-01 tamamlanmadan ARM-02'nin kod/ortam çalışmalarına geçme. Kullanıcının istediği repo açılışı ARM-01 belgelerini saklamak içindir.
