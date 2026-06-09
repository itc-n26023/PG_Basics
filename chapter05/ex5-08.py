# 3つの色が入ったリスト
colors=["blue","green","yellow"]

# 最初の状態をそのまま画面に表示する
print(colors)

# リストの一番最後のデータを取り出して、変数itemに引っ越しさせる
# このとき、元のcolorsのリストからはyelloが消え去る
item=colors.pop()

# 取り出されたデータ(item)を表示する
print(item)

# yellowが抜けた後の、現在のリストの中身を表示
print(colors)


