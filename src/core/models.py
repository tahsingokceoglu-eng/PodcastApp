class OynatmaListesi:
    def __init__(self, liste_adi):
        self.liste_adi = liste_adi
        self.podcastler = []

    def podcast_ekle(self, podcast):
        self.podcastler.append(podcast)

class Podcast:
    def __init__(self, baslik, sanatci, ses_yolu, sure="00:00", kategori="Genel"):
        self.baslik = baslik
        self.sanatci = sanatci
        self.ses_yolu = ses_yolu
        self.sure = sure
        self.kategori = kategori