import pandas as pd
df = pd.read_csv('stud.csv')
print('-'*57)
print(df)
print('-'*57)

df_marks = pd.DataFrame(df)

sort_df = df_marks.sort_values(by='Возраст')
print(sort_df)
print('-'*57)

