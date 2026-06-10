# は中身が「空っぽ」の辞書（ノート）を用意する
facts = dict()

# 「"code"（キー）」の見出しで、"fun"（バリュー）というデータを追加する
facts["code"] = "fun"
# 「"code"」って何だっけ？と辞書を引いて表示する
print(facts["code"])       


# 今度は「"Bill"」の見出しで、"Gates" というデータを追加する
facts["Bill"] = "Gates"
#「"Bill"」って誰だっけ？と辞書を引いて表示する
print(facts["Bill"])       


# 最後に「"founded"（建国）」の見出しで、1776 という数字を追加する
facts["founded"] = 1776
# 「"founded"」って何年だっけ？と辞書を引いて表示する
print(facts["founded"])    
