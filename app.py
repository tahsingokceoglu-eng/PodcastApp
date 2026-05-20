from flask import Flask, render_template, request, redirect, url_for, flash
from src.services.podcast_service import PodcastService
from src.services.downloader_service import DownloaderService
from src.modules.playlist_manager import PlaylistManager 

# Flask uygulamasını statik ve şablon klasörleriyle başlatıyoruz
app = Flask(__name__, static_folder="static", template_folder="src/ui")
app.secret_key = "spotify_secret_key"

# Servisleri ve Modülleri başlatıyoruz
podcast_servisi = PodcastService()
indirme_servisi = DownloaderService()
playlist_yoneticisi = PlaylistManager()

@app.route("/")
def index():
    # JSON'dan tüm dinamik podcast verilerini çekiyoruz
    sesler = podcast_servisi.get_all_podcasts()
    listeler = playlist_yoneticisi.tum_listeleri_getir()
    
    return render_template(
        "index.html", 
        podcasts=sesler, 
        playlists=listeler, 
        liste=None  # Ana sayfada varsayılan olarak genel kütüphane gösterilsin
    )

@app.route("/ekle", methods=["POST"])
def podcast_ekle():
    baslik = request.form.get("baslik")
    sanatci = request.form.get("sanatci")
    ses_yolu = request.form.get("ses_yolu")
    
    podcast_servisi.add_podcast(baslik, sanatci, ses_yolu)
    return redirect(url_for("index"))

@app.route("/indir-ve-ekle", methods=["POST"])
def indir_ve_ekle():
    mp3_url = request.form.get("mp3_url")
    baslik = request.form.get("baslik")
    sanatci = request.form.get("sanatci")
    kategori = request.form.get("kategori", "Genel")
    
    # Türkçe karakterleri temizleyerek güvenli dosya adı oluşturma
    guvenli_baslik = baslik.lower().replace(' ', '_').replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u').replace('ş', 's').replace('ö', 'o').replace('ç', 'c')
    dosya_adi = f"{guvenli_baslik}.mp3"
    
    basarili, sonuc_yolu = indirme_servisi.mp3_indir(mp3_url, dosya_adi)
    
    if basarili:
        podcast_servisi.add_podcast(baslik, sanatci, sonuc_yolu)
        flash("Podcast başarıyla indirildi ve eklendi!", "success")
    else:
        flash("İndirme sırasında bir hata oluştu.", "danger")
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)