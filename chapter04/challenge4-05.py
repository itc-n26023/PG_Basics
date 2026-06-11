def f(x):
    try:
        return float(x)
    except ValueError:
        print("エラー：数値に変換できません")

ans = f("3.14")
print(ans)
