# flight_update_script.py
import requests
import folium
from datetime import datetime

# 定義台灣區域範圍
min_lat, max_lat = 21.5, 26.5
min_lon, max_lon = 118.0, 123.0

# 取得航班資料（範例使用 OpenSky API）
url = "https://opensky-network.org/api/states/all"
try:
    response = requests.get(url, timeout=10)
    data = response.json()
except Exception as e:
    print("無法取得航班資料：", e)
    exit(1)

# 過濾台灣範圍內的航班
flights = []
if "states" in data:
    for flight in data["states"]:
        try:
            lat = flight[6]
            lon = flight[5]
            if lat and lon and (min_lat <= lat <= max_lat) and (min_lon <= lon <= max_lon):
                flights.append((flight[1], lat, lon))
        except:
            continue

# 建立地圖
map_taiwan = folium.Map(location=[23.7, 121], zoom_start=6)

# 加上航班標記
for callsign, lat, lon in flights:
    folium.Marker(
        location=[lat, lon],
        popup=f"Flight: {callsign}",
        icon=folium.Icon(color="blue", icon="plane", prefix='fa')
    ).add_to(map_taiwan)

# 加上時間標籤
title_html = f'''
     <h3 align="center" style="font-size:20px">
         台灣航班地圖（自動更新）<br>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
     </h3>
     '''
map_taiwan.get_root().html.add_child(folium.Element(title_html))

# 輸出成 HTML
map_taiwan.save("taiwan_flight_map.html")
print("✅ taiwan_flight_map.html 更新完成")
