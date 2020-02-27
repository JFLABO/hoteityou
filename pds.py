import pandas as pd
import json
print("\007")
df = pd.read_csv('./data/account.csv', sep=',')
print(df.head())
#df['金額'].value_counts()
print(df['金額'].value_counts())

# groupbyメソッドは複数列に対しても行える
# groupbyメソッドで、'month', 'period'列ごとに'sales'の数を合計する
#日付ごとに集計
print(df.groupby(['日付'])['金額'].sum())

#合計を算出
print(df.groupby(['コンディション'])['金額'].sum())
#print(df.groupby(['コンディション'])['検査'].count())
# groupbyメソッドで、'week'列ごとに'soldout'の数をカウントする
#df.groupby(['コンディション'])['検査'].count()

# wetherごとにtemperatureの平均値を出す
#df.groupby(['weather'])['temperature'].mean()

#並べ替え
print(df.sort_values(by='内容', ascending=False) )
print(df.sort_values(by='内容') )

#重要度順　優先度順　期限順
#print(df.sort_index(axis=1, ascending=True))
#print(df.head())

df_ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'], 'b': ['b_1', 'b_2', 'b_3']})
df_ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'], 'c': ['c_1', 'c_2', 'c_4']})

print(df_ab)
#      a    b
# 0  a_1  b_1
# 1  a_2  b_2
# 2  a_3  b_3

print(df_ac)
#      a    c
# 0  a_1  c_1
# 1  a_2  c_2
# 2  a_4  c_4

s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"\u3042"}}'

df_s = pd.read_json(s)

print(df_s)
df_s.to_json('data/d.json')
s=df_s.to_json()
with open('data/population.json', 'w') as f:
    json.dump(s, f, ensure_ascii=False, indent=4)