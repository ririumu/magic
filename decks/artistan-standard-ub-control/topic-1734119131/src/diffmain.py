# 読み込み
import pandas as pd
df1 = pd.read_csv("data/mylist.txt",  names=['q', 'name', 'side'], sep='\t')
df2 = pd.read_csv("data/reflist.txt", names=['q', 'name', 'side'], sep='\t')

# リファレンスのメインのみに注目
df2main = df2.query('side != True')

# マージ実行
df20main =  df2main.groupby('name', as_index=False)['q'].sum()
df10 = df1.groupby('name', as_index=False)['q'].sum()
df40 = pd.merge(df10, df20main, on="name", how="outer").sort_values(by="name")
df40 = df40.fillna(0).astype(int, errors="ignore")

# 枚数差分計算
df40['q_diff'] = df40['q_y'] - df40['q_x']
result = df40[["name", "q_diff"]].query('q_diff != 0').sort_values(by='q_diff', ascending=False).reset_index(drop=True)

# 出力
print(result.to_string(index=False))
