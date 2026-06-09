def f(x):
    """引数を2で割って整数の商を求める関数
    :x: int: 割られる数
    :戻り値: 2で割った整数の商
    """
    return x // 2

def g(x):
    """
    引数に4を掛けて積を求める関数
    :x: int: 掛けられる数
    :戻り値: 4を掛けた積
    """
    return x * 4

val = 10
ans1=f(val)
ans2=g(ans1)
print(ans2)

