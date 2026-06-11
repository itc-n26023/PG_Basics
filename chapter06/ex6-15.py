# 元になる文章（"All animals are e	qual."）を用意
equ = "All animals are e	qual."

# .replace("見つけたい文字", "置き換えたい文字") を使う
# 文字列の中にあるすべての小文字の "a" を、"@" に一斉に変身させて上書き保存
equ = equ.replace("a", "@")

# 置き換えが終わった結果を画面に表示
print(equ)
