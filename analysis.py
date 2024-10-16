import main
import time
import csv

data = open("record.csv", 'a+')
writer = csv.writer(data)
runs = 1

while runs < 300:
    ctime = time.time()
    status = main.solve()
    writer.writerow([time.time() - ctime, status])
    data.flush()
    runs += 1

data.close()
