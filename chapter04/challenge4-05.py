def f(x):
    """引数をfloat型に変換する関数
    :x: str: 変換したい文字列
    :戻り値: float型に変換された値
    """
    try:
        return float(x)
    except ValueError:
        print("エラー：数値に変換できません")

ans = f("3.14")
print(ans)

