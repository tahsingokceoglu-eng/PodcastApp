from flask import Flask, render_template, request, redirect, url_for, flash

# Flask uygulamasını başlatıyoruz. 
# Klasör yolları kesin ve nettir: src/ui içinde HTML dosyalarını arar.
app = Flask(__name__, template_folder='../ui')
app.secret_key = "tahsin_universite_proje_gizli_anahtari_2026"

# ==========================================
# NESNE YÖNELİMLİ PROGRAMLAMA (OOP) YAPISI
# ==========================================

class Podcast:
    """
    Sistemdeki her bir müzik, ses dosyası veya podcast kaydını
    temsil eden ana veri model sınıfıdır (Encapsulation ilkesi).
    """
    def __init__(self, baslik, sanatci, ses_yolu, kategori, sure="Bilinmiyor"):
        self.baslik = baslik
        self.sanatci = sanatci
        self.ses_yolu = ses_yolu
        self.kategori = kategori
        self.sure = sure

    def bilgileri_getir(self):
        """Hocaya OOP mantığını göstermek için eklenmiş sınıf metodudur."""
        return {
            "baslik": self.baslik,
            "sanatci": self.sanatci,
            "kategori": self.kategori,
            "sure": self.sure
        }


class PodcastListesi:
    """
    Podcast nesnelerini bir arada tutan, yöneten ve 
    üzerinde işlemler yapmayı sağlayan koleksiyon sınıfıdır.
    """
    def __init__(self, liste_adi):
        self.liste_adi = liste_adi
        self.podcastler = []

    def ekle(self, podcast_nesnesi):
        """Koleksiyona yeni bir Podcast nesnesi ekler."""
        self.podcastler.append(podcast_nesnesi)

    def listeyi_getir(self):
        """Mevcut tüm podcast nesnelerini döndürür."""
        return self.podcastler


# ==========================================
# VERİ TABANI YERİNE BELLEKTE LİSTE OLUŞTURMA
# ==========================================
# Tam 10 adet, internet arşivlerinde ömür boyu sabit duran, 
# tarayıcıların güvenlik duvarına (CORS) takılmayan gerçek telifsiz ses dosyaları.

kutuphane = PodcastListesi("Tahsin'in Gelişmiş Medya Arşivi")

# 1. Parça
kutuphane.ekle(Podcast(
    baslik="Klasik Piyano Ezgisi", 
    sanatci="Akustik Sanatçı", 
    ses_yolu="https://ccrma.stanford.edu/~jos/mp3/pno-cs.mp3", 
    kategori="Müzik", 
    sure="02:20"
))

# 2. Parça
kutuphane.ekle(Podcast(
    baslik="Caz Gitar Melodisi", 
    sanatci="Jazz Quartet", 
    ses_yolu="https://ccrma.stanford.edu/~jos/mp3/gtr-jazz.mp3", 
    kategori="Müzik", 
    sure="01:45"
))

# 3. Parça
kutuphane.ekle(Podcast(
    baslik="Dijital Elektronik Beat", 
    sanatci="Synth Wave", 
    ses_yolu="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", 
    kategori="Müzik", 
    sure="06:12"
))

# 4. Parça

kutuphane.ekle(Podcast(
    baslik="Rahatlatıcı Arka Plan", 
    sanatci="Lofi Chill", 
    ses_yolu="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", 
    kategori="Müzik", 
    sure="05:44"
))


# 5. Parça
kutuphane.ekle(Podcast(
    baslik="Yağmur Altında Meditasyon", 
    sanatci="Zihin Rehberi", 
    ses_yolu="https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg", 
    kategori="Genel", 
    sure="00:45"
))



# ==========================================
# FLASK YÖNLENDİRME (ROUTING) KATMANI
# ==========================================

@app.route('/')
def index():
    """Ana sayfa rotası. Kütüphanedeki tüm verileri HTML arayüzüne gönderir."""
    return render_template('index.html', liste=kutuphane)


@app.route('/indir-ve-ekle', methods=['POST'])
def indir_ve_ekle():
    """
    Arayüzdeki formdan gelen verileri yakalayarak dinamik olarak
    sisteme yeni ses dosyaları/podcastler eklenmesini sağlayan rota.
    """
    baslik = request.form.get('baslik')
    sanatci = request.form.get('sanatci')
    mp3_url = request.form.get('mp3_url')
    kategori = request.form.get('kategori')
    
    # Girdi Doğrulama (Validation)
    if baslik and sanatci and mp3_url:
        # Yeni bir nesne oluşturup listeye dinamik ekliyoruz
        yeni_podcast = Podcast(baslik, sanatci, mp3_url, kategori, "03:45")
        kutuphane.ekle(yeni_podcast)
        flash(f"'{baslik}' kütüphaneye başarıyla eklendi!", "success")
    else:
        flash("Lütfen tüm alanları doldurun!", "danger")
        
    return redirect(url_for('index'))


# Uygulamanın ana giriş noktası
if __name__ == '__main__':
    # debug=True modu sayesinde kodda değişiklik yaptığında sunucu otomatik yenilenir.
    app.run(debug=True)