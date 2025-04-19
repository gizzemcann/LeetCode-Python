weather = [
    {"id": 1, "recordDate": "2020-01-01", "temperature": 10},
    {"id": 2, "recordDate": "2020-01-02", "temperature": 25},
    {"id": 3, "recordDate": "2020-01-03", "temperature": 20},
    {"id": 4, "recordDate": "2020-01-04", "temperature": 30},
]
from datetime import datetime, timedelta

# Verileri tarih tipine çevir
for day in weather:
    day["recordDate"] = datetime.strptime(day["recordDate"], "%Y-%m-%d")

# Listeyi tarihe göre sırala
weather.sort(key=lambda x: x["recordDate"])

# Sonuçları saklayacağımız liste
rising_dates = []

# Her günü önceki günle karşılaştır
for i in range(1, len(weather)):
    today = weather[i]
    yesterday = weather[i - 1]
    
    # Eğer gün farkı 1 ve sıcaklık arttıysa
    if (today["recordDate"] - yesterday["recordDate"]).days == 1:
        if today["temperature"] > yesterday["temperature"]:
            # Tarihi string'e çevirip ekle
            rising_dates.append(today["recordDate"].strftime("%Y-%m-%d"))

print(rising_dates)