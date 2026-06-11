# ドッキングさせたい3つの文字 "abc" を用意する
first_three = "abc"

# "abc" の1文字ずつの「間に」、"+" を挟み込んで1つの文字列に合体させる
result = "+".join(first_three)

# 合体した結果（"a+b+c"）を画面に表示
print(result)
