import pandas as pd
df = pd.read_csv('stud.csv')
print(df)

def plus(s):
    if s == '-':
        df['Возраст'] -= 1
    return 'Все готово'

print(plus(input("Нажмите - чтобы уменьшить возраст на 1: ")))

c=input('Хотите посмотреть изменения нажмите -:')
if c=='-':
    df = pd.read_csv('stud.csv')
    print(df.to_string(index=False))