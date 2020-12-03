import csv

with open('D:\FINAL PROJECT\CODE\common_crawl.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
