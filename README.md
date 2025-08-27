## 🎭 Opera & Bale Analizi Sonuçları

Bu projede, TÜİK’ten aldığım verilerle yerli ve yabancı eserlerin seyirci sayılarındaki dalgalanmaları ve bu değişimlerin diğer faktörlerle ilişkisini inceledim. Verileri analiz etmek için Python’da NumPy, Pandas ve Matplotlib kullandım. Tabloların tek tek analizi aşağıdadır:

### 📌 Tablo1: Seyirci Trendleri
- 2003-2004’te yabancı eserler rekor kırdı (400K+ seyirci).  
- Pandemi (2020-2021) büyük düşüşe yol açtı, 2021 sonrası toparlanma başladı.  
- Yerli eserler 2008’den sonra yükselişe geçti, 2012-2013’de zirve yaptı.  

### 📌 Tablo2: Oynanan Eser Sayıları
- Yabancı eser sayısı genel olarak daha yüksek.  
- Yerli eserler 2007-2008’de en yoğun dönemini yaşadı (140+ eser).  
- 2020-2021’de büyük düşüş; 2023-2024’te yerli eser sayısı yeniden öne geçti.  

### 📌 Tablo3: Yerli Eser Sayısı ↔ Seyirci Sayısı
- **Pozitif Korelasyon:** r = 0.56  
- Eser sayısı arttıkça seyirci sayısında genel bir artış eğilimi var.  
- **Sınırlılık:** En yüksek seyirci sayısı her zaman en çok eser sayısı ile gerçekleşmiyor; kalite ve diğer faktörler etkili.

### 📌 Tablo4: Yabancı Eser Sayısı ↔ Seyirci Sayısı
- Zayıf Korelasyon: r = 0.10  
- Yabancı eser sayısının seyirciyi kayda değer şekilde etkilemediği görülüyor.  
- Aykırı Değerler: Bazı sezonlarda eser sayısı az ama seyirci sayısı yüksek, bu da popülarite ve kalite faktörlerini gösteriyor.

### 📌 Tablo5: Koltuk Sayısı ↔ Seyirci Sayısı
- Yerli eserlerde zayıf pozitif ilişki (r=0.33).  
- Yabancı eserlerde çok zayıf negatif ilişki (r=−0.18).  
- Seyirci ilgisi, kapasiteden çok eserin popülaritesine bağlı.

---

## ❗ Sonuç
- Yerli eserlerde nicelik (eser sayısı) kısmen önemli bir faktör.  
- Yabancı eserlerde seyirci sayısını belirleyen asıl faktör, eserlerin popülaritesi ve kalitesidir, eser sayısı veya salon kapasitesi değil.
