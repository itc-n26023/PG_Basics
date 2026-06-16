# qs というリストに、3つの質問（質問0, 質問1, 質問2）を用意
qs = [
    "What is your name?",          # qs[0]
    "What is your fav. color?",    # qs[1]
    "What is your quest?"          # qs[2]
]

# 今何番目の質問を出すかを決めるカウンター変数 n を 0 にセット
n = 0

# while True で、ユーザーが止めるまで「永遠に繰り返す」ループを開始
while True:
    print("Type q to quit")        
    
    # input() でユーザーにキーボード入力を求る
    # 最初は qs[0]（1つ目の質問）が画面に表示され、入力された文字が変数 a に入る
    a = input(qs[n])
    
    # もしユーザーが "q" と入力したら、break で無限ループを脱出して終了
    if a == "q":
        break
    
    # 次の質問に進めるために n を書き換える
    #% 3（3で割った余り）の計算を使うことで、n の値を「0 → 1 → 2 → 0 → 1...」とループさせる
    n = (n + 1) % 3
