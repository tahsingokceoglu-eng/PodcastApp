from src.core.models import OynatmaListesi

class PlaylistManager:
    def __init__(self):
        # Geçici olarak listeleri hafızada tutuyoruz (İstersen ileride JSON'a bağlayabiliriz)
        self.playlists = {}

    def liste_olustur(self, liste_adi):
        """Yeni bir boş oynatma listesi oluşturur."""
        if liste_adi not in self.playlists:
            self.playlists[liste_adi] = OynatmaListesi(liste_adi)
            return True, f"'{liste_adi}' listesi başarıyla oluşturuldu."
        return False, "Bu isimde bir liste zaten var."

    def listeye_podcast_ekle(self, liste_adi, podcast_objesi):
        """Belirtilen listeye bir podcast nesnesi ekler."""
        if liste_adi in self.playlists:
            self.playlists[liste_adi].podcast_ekle(podcast_objesi)
            return True, f"'{podcast_objesi.baslik}' listeye eklendi."
        return False, "Oynatma listesi bulunamadı."

    def tum_listeleri_getir(self):
        """Oluşturulan tüm oynatma listelerini döndürür."""
        return self.playlists