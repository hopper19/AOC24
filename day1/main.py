import pandas as pd
from collections import Counter

file_path = 'input.txt'

df = pd.read_csv(file_path, sep=r'\s+', header=None, names=['left', 'right'], dtype=int)
# total distance
print(sum(abs(a - b) for a, b in zip(sorted(df['left']), sorted(df['right']))))
# similarity score
print(sum(num * Counter(df['right'])[num] for num in df['left']))
