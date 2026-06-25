import statistics

#例題3のリストのコピー
nums = [1, 5, 33, 12, 46, 33, 2]

# stdev() で標準偏差を表示
print("標準偏差:", statistics.stdev(nums))

# variance() で分散を表示
print("分散:", statistics.variance(nums))
