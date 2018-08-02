#coding=utf-8
import csv
#读取csv
with open('csvtest.csv', 'r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

#写csv
with open('csvtest.csv', 'a',newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(['name','address','age','state'])
    s1=['3','居住地点','30','2']
    writer.writerow(s1)

# with open('csvtest.csv', 'r') as f:
#     print(f.read())