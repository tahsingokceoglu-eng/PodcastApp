# 🎙️ Podcast ve Müzik Kütüphanesi 

**Ders:** BGT 132 - Yazılım Geliştirme Teknolojileri (Final Projesi)  
**Geliştirici:** Tahsin  

---

## 📌 Proje Amacı
Bu proje, BGT 132 dersi kapsamında geliştirilmiş, Nesne Yönelimli Programlama (OOP) ve MVC benzeri modüler mimari kullanılarak oluşturulmuş dinamik bir ses dosyası (podcast/müzik) yönetim ve oynatma web uygulamasıdır. Kullanıcıların dijital kütüphanelerindeki ses dosyalarını listeleyebildiği, anlık arama yapabildiği ve web tarayıcısı üzerinden kesintisiz müzik dinleyebildiği bir sistem tasarlamak hedeflenmiştir.

---

## 🚀 Proje Özellikleri ve Nasıl Çalışır?

Proje, arka planda **Python (Flask)** ve ön yüzde **HTML/CSS/JS** teknolojilerini kullanır. Uygulamanın temel çalışma mantığı şu şekildedir:

1. **Dinamik Veri Yönetimi:** Ses dosyaları ve listeler, arka planda oluşturulan Python sınıfları (Class) aracılığıyla nesnelere dönüştürülür.
2. **Anlık Arama (Client-Side):** Sayfayı yenilemeye gerek kalmadan, JavaScript kullanılarak podcast başlığı veya sanatçı adına göre anlık (real-time) filtreleme yapılır.
3. **Kesintisiz Oynatıcı:** Ekranın alt kısmına sabitlenmiş modern bir Audio Player sayesinde, kullanıcılar sitede gezinirken dinleme deneyimi kesintiye uğramaz. Tıklanan ses dosyaları anında oynatıcıya yüklenir ve ses dalgası animasyonları tetiklenir.
4. **Hata Yönetimi (Flash Messages):** Yeni podcast ekleme veya indirme işlemlerinde kullanıcıya başarılı/başarısız durum bildirimleri Flask'ın `flash` yapısıyla anlık olarak gösterilir.

---

## 🧩 Nesne Yönelimli Programlama (OOP) Yaklaşımı

Proje, spagetti koddan kaçınmak ve sürdürülebilirliği artırmak için tamamen **OOP prensiplerine** uygun tasarlanmıştır:

* **Sınıflar (Classes) ve Kapsülleme (Encapsulation):** `Podcast`, `SesDosyasi` veya `PodcastListesi` gibi sınıflar oluşturularak, her ses dosyasının özellikleri (başlık, sanatçı, süre, dosya yolu) bu nesneler içinde güvenle tutulur.
* **Modüler Yapı (MVC Mantığı):** * `core/app.py`: Yönlendirmeleri (Routing) ve Controller görevini üstlenir.
  * `models/`: Veri yapılarını ve sınıfları (Model) barındırır.
  * `ui/index.html`: Kullanıcı arayüzünü (View) oluşturur.

---

## 📂 Proje Klasör Yapısı

```text
PodcastApp/
│
├── src/
│   ├── core/
│   │   └── app.py                # Ana Flask uygulaması ve Route'lar
│   ├── models/
│   │   └── media.py              # OOP Sınıflarının bulunduğu veri modeli
│   ├── modules/
│   │   └── playlist_manager.py   # Liste yönetim fonksiyonları
│   ├── services/
│   │   └── podcast_service.py    # İndirme ve ekleme servisleri
│   └── ui/
│       └── index.html            # Dinamik Jinja2 HTML şablonu
│
├── 
│                    
│
└── README.md                     # Proje dokümantasyonu
pip install Flask
python src/core/app.py
* Running on http://127.0.0.1:5000