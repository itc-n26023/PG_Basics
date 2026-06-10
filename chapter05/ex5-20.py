# 1. ビル・ゲイツさんの特徴が入った「辞書 { }」を作る
# キー（見出し）: "Bill Gates" ── バリュー（中身）: "charitable"（慈善活動家）
bill = {"Bill Gates": "charitable"}

# 2. 「"Bill Gates" という見出し（キー）は辞書に登録されていますか？」と尋ねる
print("Bill Gates" in bill)       

# 3. 「"Bill Doors"（ビル・ドアーズ）という見出しは登録されていませんよね？」と尋ねる
print("Bill Doors" not in bill)   
