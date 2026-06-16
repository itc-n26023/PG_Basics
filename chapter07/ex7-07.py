# 元データとなる2つのリスト（tv と coms）を用意
tv = ["GOT", "Narcos", "Vice"]	
coms = ["Arrested Development", "friends", "Always Sunny"]

# まとめたデータを入れるための、中身が空っぽのリスト「all_shows」を用意
all_shows = []

# 【1つ目のループ】tv のリストから1つずつデータを取り出す
for show in tv:
    show = show.upper()       
    all_shows.append(show)

# 【2つ目のループ】coms のリストからも1つずつデータを取り出す
for show in coms:
    show = show.upper()       
    all_shows.append(show)    

# 5. 完成した、すべて大文字の合体リストを表示
print(all_shows)
