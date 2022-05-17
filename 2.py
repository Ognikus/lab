import csv
with open("students.csv", 'r') as text_1:
    lst = [item for item in csv.reader(text_1, delimiter=';')]

print(lst, end='')