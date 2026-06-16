#peopleという変数に｢キャラクター名(キー)｣と｢番組名(値)｣をペアにして辞書として入れる
people={"G.Bluth II": "A.Development",
        "Barney": "HIMYM",
        "Dennis": "always Sunny",
}
#辞書peopleをそのままfor文にかけるとキーだけが1つずつ取り出される
for character in people:
    print(character)
