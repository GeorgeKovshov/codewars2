path = "N:\Git\codewars\google_stock_data.csv"
lines = [line for line in open(path)]

print(lines[0])
# strip - remove trailing or leading whitespace
lines[0].strip()

import csv
from datetime import datetime
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
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

# Compute and store daily stock returns
returns_path = "N:\Git\codewars\google_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    #writer.writerow([todays_date,daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])