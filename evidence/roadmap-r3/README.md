# R3 plan ve yayın kanıtı - 15 Ekim 2026

Kullanıcı sekiz revizyonu ve mevcut site/rapor güncellemesini onayladı. Bu klasör plan yayınının kanıtıdır; ARM-02 uygulama başarısı değildir.

- Mevcut site: https://arda-mekatronik-calisma-haritasi.decent-cloud-1314.chatgpt.site/
- Yayınlanan site sürümü: **2**; Sites yanıtı **succeeded**.
- Site kaynak commit'i: `a11ba5bd888d8ee2804774e128c8a8323a9d021c`.
- Yapılandırılmış R3 kaynak: `docs/arm-roadmap-r3.json`; 24 görev, 242 saat geçici kapsam, ARM-10'a kadar 112 saat.
- `site-arm02-r3.png`: Yayın sonrası canlı ARM-02 kartı. Boş kişisel tarayıcı kaydındaki durumlar proje kabul kanıtı değildir; ARM-01'in repo kapanışı `65142f1` ile ayrı kayıtlıdır.
- R3 PDF: 28 sayfa; tüm sayfalar render edildi ve yerleşim incelendi. Her görev tek sayfayla eşleştirildi.

Doğrulama:

1. 24 tekil görev; ön koşullar önceki görevlere bağlı ve döngü yok. Görev/aşama/toplam saatler eşleşiyor.
2. Site ArmPilot nesnesi, repo JSON'u ve siteden indirilecek PDF repo PDF'iyle eşleşiyor.
3. İlk site commit'i `e33880af128cd6800e24e7312301dd403d45b38c` ile karşılaştırmada AMR/SortLine görev nesneleri ve PDF dosyaları değişmedi.
4. Site JavaScript sözdizimi ve `checks/arm-revision.test.mjs` geçti: eski kabul indisleri arşivleniyor, not/süre korunuyor, eski tamamlanma yeni kapsamı otomatik onaylamıyor, tekrar açılışta yeniden taşıma olmuyor.
5. Yerel tarayıcıda ARM-01 kutu/not/süre/tamamlama akışı denendi; ARM-02 uygun hale geldi ve sayfa yenilendiğinde kayıt korundu. Bu test localhost kaydıdır; canlı siteye test ilerlemesi yazılmadı.
6. Canlı ARM-02 kartının yeni içeriği yayın sonrasında görüldü; yerel tarayıcı konsolunda uygulama hatası görülmedi. Sites yayın sonucu başarıyı doğruladı.

Yayın hazırlığında WSL `bash` yolu ve GNU tar'ın `C:` yorumlaması sorunları çıktı. Yalnız paketleme sürecinde kurulu Git Bash yolu ve `TAR_OPTIONS=--force-local` kullanılarak çözüldü; sistem ayarı veya site işlevi değiştirilmedi. Kaynak helper'ı aynı site kimliğini kullanarak commit/push/paketleme yaptı. Mevcut erişim kitlesi korundu.

Yeniden kontrol: `python docs/references/verify_roadmap.py --site tmp/site-roadmap`. Markdown eşitleme: `python docs/references/sync_roadmap.py`; PDF üretme: `python docs/references/build_roadmap_pdf.py`. Bunlar dokümantasyon araçlarıdır; robot uygulaması değildir.
