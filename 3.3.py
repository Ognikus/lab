import pandas

df = pandas.read_csv('students.csv', sep=',', encoding='utf-8')
print(df.to_string(index=False))

# def plus(s):
#     if s == '+':
#         df['Возраст'] += 1
#     return 'Все готово'
#
# print(plus(input("Нажмите + чтобы увеличить возраст на 1: ")))
#
# c=input('Хотите посмотреть изменения нажмите +:')
# if c=='+':
#     print(df)
