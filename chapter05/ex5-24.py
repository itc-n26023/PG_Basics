# 位置情報をまとめて入れるための「空っぽのリスト（大きな箱）」を作る
locations = []

# ロサンゼルス（la）とシカゴ（chicago）の「緯度・経度」をタプルで作る
# 緯度・経度は「後から書き換わったら困る絶対に不変のデータ」なので、タプル ( ) が最適です！
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

# リストの中に、それぞれのタプルを「.append()」で追加する
locations.append(la)
locations.append(chicago)

# 合体したリストを表示する
print(locations)
