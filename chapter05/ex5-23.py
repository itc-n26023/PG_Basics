lists = []
rap = ["カニエ・ウェスト", "ジェイ・z", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists) 

# 大きなリストの0番目（ラップの塊）を取り出して、変数 rap に「もう一度」入れ直す
rap = lists[0]
print(rap)   

# 取り出した変数 rap に、新しいラッパー「ケンドリック・ラマー」を追加する
rap.append("ケンドリック・ラマー")
print(rap)   

# 3.大元の大きなリスト「lists」をもう一度表示してみる
print(lists)
