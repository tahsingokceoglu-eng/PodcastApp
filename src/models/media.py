# src/models/media.py

# 1. SINIF (Base/Ana Sınıf)
class Media:
    def __init__(self, title, creator):
        # ENCAPSULATION (Kapsülleme): Değişkenlerin başına çift alt çizgi (__) koyarak gizli (private) yapıyoruz[cite: 14].
        self.__title = title
        self.__creator = creator

    # Gizli değişkenlere erişmek için Getter metotları
    def get_title(self):
        return self.__title

    def get_creator(self):
        return self.__creator

    # POLYMORPHISM (Çok Biçimlilik) için alt sınıflarda ezilecek (override edilecek) temel metot[cite: 12].
    def get_details(self):
        return f"{self.__title} by {self.__creator}"

# 2. SINIF (Alt Sınıf) - INHERITANCE (Kalıtım): Media sınıfından miras alıyor[cite: 12].
class Song(Media):
    def __init__(self, title, creator, duration):
        super().__init__(title, creator) # Üst sınıfın özelliklerini çekiyoruz
        self.duration = duration

    # POLYMORPHISM: Üst sınıftaki metodu kendi ihtiyacına göre eziyor[cite: 12].
    def get_details(self):
        return f"🎵 Şarkı: {self.get_title()} - Sanatçı: {self.get_creator()} ({self.duration} dk)"

# 3. SINIF (Alt Sınıf) - INHERITANCE (Kalıtım)[cite: 12].
class Podcast(Media):
    def __init__(self, title, creator, episode_number):
        super().__init__(title, creator)
        self.episode_number = episode_number

    # POLYMORPHISM: Aynı metot ismi ama farklı çıktı[cite: 12].
    def get_details(self):
        return f"🎙️ Podcast: {self.get_title()} - Sunucu: {self.get_creator()} (Bölüm: {self.episode_number})"