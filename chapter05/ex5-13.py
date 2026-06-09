# クイズの正解リストを用意
colors = ["purple", "orange", "green"]
# 画面に質問を表示してキーボードからの入力(input)、入力された文字をguess(予想)に入れる
guess = input("何色でしょうか？(入力してください) :")

# もし(if)、予想した文字が正解リストの中に入っていれば
if guess in colors:
    print("当たり！")
# 入っていなければ
else:
    print("ハズレ！また挑戦してね。")

