path = "N:\Git\codewars\google_stock_data.csv"
lines = [line for line in open(path)]

print(lines[0])
# strip - remove trailing or leading whitespace
lines[0].strip()

import csv
import datetime
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # the first line in the header
#data = [row for row in reader] ---    read the remaining data

data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[3])
    volume = int(row[2])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

