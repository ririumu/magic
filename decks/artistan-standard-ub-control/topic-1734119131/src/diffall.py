# 読み込み
import pandas as pd
df1 = pd.read_csv("data/mylist.txt",  names=['q', 'name', 'side'], sep='\t')
df2 = pd.read_csv("data/reflist.txt", names=['q', 'name', 'side'], sep='\t')

# 枚数注目のためメインとサイドを合算
df20 =  df2.groupby('name', as_index=False)['q'].sum()
df10 =  df1.groupby('name', as_index=False)['q'].sum()

# マージを実行
df30 = pd.merge(df10, df20, on="name", how="outer").sort_values(by="name")
df30 = df30.fillna(0).astype(int, errors="ignore")

# 枚数差分計算
df30['q_diff'] = df30['q_y'] - df30['q_x']
result = df30[["name", "q_diff"]].query('q_diff != 0').sort_values(by='q_diff', ascending=False).reset_index(drop=True)

# 出力
print(result.to_string(index=False))
