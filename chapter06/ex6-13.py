# 7つの単語がバラバラに収納された「リスト」
words = ["The", "fox", "jumped", "over", "the", "fence", "."]

# 「""（空っぽの文字）」にしてドッキング（隙間なくギチギチになる）
one = "".join(words)
# 合体した結果を表示
print(one)

# 今度は「" "（半角スペース1つ）」にしてドッキング
one = " ".join(words)
# 合体した結果を表示
print(one)
