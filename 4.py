import pandas as pd
df = pd.read_csv('stud.csv', sep=',', encoding='utf-8')
print(df.to_string(index=False))

def plus(s):
    if s == '+':
        df['Возраст'] -= 1
        df.to_csv('stud.csv', sep=',', encoding='utf-8', index=False)
    return 'Все готово'

print(plus(input("Нажмите + чтобы уменьшить возраст на 1: ")))
c=input('Хотите посмотреть изменения нажмите +:')
if c=='+':
    df = pd.read_csv('stud.csv', sep=',', encoding='utf-8')
    print(df.to_string(index=False))
