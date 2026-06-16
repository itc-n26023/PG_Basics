list=["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]

#for文でenumerate関数を使ってインデックス値(i)と要素(item)を取得する
for i, item in enumerate(list):
    print("{},{}".format(i, item))
