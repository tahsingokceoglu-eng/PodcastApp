import os
import requests

class DownloaderService:
    def __init__(self, target_folder="static/sounds"):
        self.target_folder = target_folder
        # Eğer static/sounds klasörü yoksa otomatik oluşturur
        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)

    def mp3_indir(self, url, dosya_adi):
        """
        Verilen URL'deki MP3 dosyasını indirir ve static/sounds klasörüne kaydeder.
        """
        # Dosya adının sonuna .mp3 uzantısını garantiye alalım
        if not dosya_adi.endswith(".mp3"):
            dosya_adi += ".mp3"
            
        hedef_yol = os.path.join(self.target_folder, dosya_adi)

        try:
            # İnternetten dosyayı indiriyoruz (Stream=True büyük dosyalar için belleği yormaz)
            cevap = requests.get(url, stream=True, timeout=15)
            
            if cevap.status_code == 200:
                with open(hedef_yol, 'wb') as f:
                    for chunk in cevap.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                
                # Flask'ın static klasöründen erişebilmek için uygun web yolunu dönüyoruz
                return True, f"static/sounds/{dosya_adi}"
            else:
                return False, f"İndirme başarısız. Hata kodu: {cevap.status_code}"
                
        except Exception as e:
            return False, f"Bir hata oluştu: {str(e)}"