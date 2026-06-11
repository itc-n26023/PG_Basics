#input文でユーザーが入力した文字列をセット
food=input("好きな食べ物は？")

#別のinput文で文字列をセットする
reason=input("理由は？")

#print文の中でfomat()メソッドを使って2つの変数の値を{}に指定して表示
print("{}が好きな理由は{}からです。".format(food,reason))
