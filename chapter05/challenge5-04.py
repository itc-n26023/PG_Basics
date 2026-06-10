profile={
        "好きな色":"🟣",
        "身長":"147",
        "好きな作家":"乙一"
}

key=input("調べたい項目を入力してください")

if key in profile:
    value=profile[key]
    print(value)

else:
    print("登録されていません")
