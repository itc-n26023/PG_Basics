# 3つの小説が入った「タプル ( )」を作る
dys = ("1984", "Brave New World", "Fahrenheit 451")

# 2番目の部屋の中身を覗き見して表示する
# 部屋番号の指定は、リストと同じように四角カッコ [ ] を使う
print(dys[2])                   

# 「"1984" はタプルの中に入っていますか？」と尋ねる
print("1984" in dys)             

# 「"Handmaid's Tale" は入っていませんよね？」と尋ねる
print("Handmaid's Tale" not in dys) 
