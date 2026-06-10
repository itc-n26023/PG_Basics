# 作家（キー）と誕生日（バリュー）が入った「辞書 { }」を作る
bday = {
    "Hemingway": "7.21.1899",
    "Fitzgerald": "9.24.1896"
}

# その辞書を、丸ごと「リスト [ ]」の中に突っ込む
my_list = [bday]
print(my_list)   # 出力: 辞書が [ ] で囲まれて表示される

# 今度はその辞書を、丸ごと「タプル ( )」の中に突っ込む
my_tuple = (bday, )
print(my_tuple)  
