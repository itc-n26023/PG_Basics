# 計算の元になる2つの数字のリスト（list1 と list2）を用意
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# 足し算した結果を貯めていくための、中身が空っぽのリスト「added」を用意
added = []

# list1 から数字を1つずつ取り出して i に入れる
for i in list1:
    # 外側の i が1回決まるたびに、list2 から数字を1つずつ取り出して j に入れる
    for j in list2:
        # i と j を足し算した結果を、リスト added の後ろに追加（append）していく
        added.append(i + j)

# すべての組み合わせの足し算が終わったら、完成したリスト added を表示print(added)
