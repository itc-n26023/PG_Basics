# 1. 3冊の本のタイトル（キー）と、その作者（バリュー）が入った「辞書 { }」を作る
books = {
    "Dracula": "Stoker",
    "1984": "Orwell",
    "The Trial": "Kafka"
}

# 2. del 命令を使って、辞書から「"The Trial"」のデータを部屋ごと丸ごと削除する
del books["The Trial"]

# 3. 削除された後の辞書の中身を表示する
print(books)
