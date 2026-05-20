import json
import os
from src.core.models import Podcast

class PodcastService:
    def __init__(self, json_path="data/podcasts.json"):
        self.json_path = json_path

    def _load_data(self):
        """JSON dosyasından verileri okur."""
        if not os.path.exists(self.json_path):
            return []
        with open(self.json_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def _save_data(self, data):
        """Verileri JSON dosyasına kaydeder."""
        with open(self.json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_all_podcasts(self):
        """Tüm podcast'leri nesne listesi olarak döndürür."""
        data = self._load_data()
        podcasts = []
        for p in data:
            podcasts.append(Podcast(
                baslik=p.get("baslik"),
                sanatci=p.get("sanatci"),
                ses_yolu=p.get("ses_yolu"),
                sure=p.get("sure", "00:00"),
                kategori=p.get("kategori", "Genel")
            ))
        return podcasts

    def add_podcast(self, baslik, sanatci, ses_yolu, sure="00:00", kategori="Genel"):
        """Yeni bir podcast ekler ve JSON'a kaydeder."""
        data = self._load_data()
        yeni_podcast = {
            "baslik": baslik,
            "sanatci": sanatci,
            "ses_yolu": ses_yolu,
            "sure": sure,
            "kategori": kategori
        }
        data.append(yeni_podcast)
        self._save_data(data)
        return True