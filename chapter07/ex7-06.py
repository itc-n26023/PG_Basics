#3人の名前が入ったリストlを用意
l=['Alice','Bob','Charilue']

#enumerate(l)と書くことで、リストの中身と一緒に｢0,,1,,2...｣という番号を自動生成する
#for の後ろの｢i｣に番号が｢name｣に名前が同時にセットされる
for i, name in enumerate(l):
    print(i, name)
