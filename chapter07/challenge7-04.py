#リストに数値を任意の数だけセットする
list=[3,7,15,22,45]

#while文で処理を繰り返す(無限ループ)
while True:
    user_input=input("数字を入力してください'q'で終了")

    #"q"が入力されたらwhileのループを終了する
    if user_input=="q":
        print("ゲームを終了します")
        break

#例外処理(try-except)を使って、入力された文字をチェックする
    try:
        num=int(user_input)

    #入力された値がリストにあれば正解
        if num in list:
            print("正解！")

    #なければ不正解
        else:
            print("不正解")

    except ValueError:
        print("数字か'q'を入力してください")
