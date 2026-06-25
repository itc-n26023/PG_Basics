# 統計のモジュールを読み込む
import statistics

# 計算するための数字のリストを用意
nums = [1, 5, 33, 12, 46, 33, 2]

# 平均値を計算して表示
print(statistics.mean(nums))

# 中央値を表示
print(statistics.median(nums))

# 最頻値を表示
print(statistics.mode(nums))
