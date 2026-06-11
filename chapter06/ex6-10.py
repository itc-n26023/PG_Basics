# input() を使うと、画面でキーボードからの入力を待ち受ける
# 入力された文字は、それぞれ what, when, where, do という変数（箱）に保存される
what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうした:")

# 4つの {}（空席）に、入力された4つの言葉を順番通りに流し込んで、1つの文章（r）を作る
r = "{}は{}に{}で{}。".format(what, when, where, do)

# 完成した文章を画面に表示する
print(r)
