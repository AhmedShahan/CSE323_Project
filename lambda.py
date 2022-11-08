sample = [(1, 0, 0), (4, 1, 2), (4, 5, 5), (1, 2, 1)]
sample.sort(key = lambda i:i[1],reverse=True)
print(sample)