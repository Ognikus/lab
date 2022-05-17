import pandas as pd
df = pd.read_csv('stud.csv')
df.set_index("№", drop=True, inplace=True)
dictionary = df.to_dict(orient="index")

column_order = ["ФИО", "Возраст", "Группа"]
d = {}
for k in dictionary:
    d[k] = [dictionary[k][column_name] for column_name in column_order]
print(d)
sorted_tuple = sorted(d.items(), key=lambda x: x[1][1])
print(sorted_tuple)

# df_marks = pd.DataFrame(df)
# sort_df = df_marks.sort_values(by='Возраст')
# print(sort_df)

# for k in sorted(d.keys()):
#     print(k, ':', d[k])