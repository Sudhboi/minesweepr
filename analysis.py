import main
import time
import csv

data = open("record.csv", 'a+')
writer = csv.writer(data)
runs = 1

while runs < 20:
    ctime = time.time()
    try:
        status = main.solve()
    except:
        status = False
    writer.writerow([time.time() - ctime, status])
    data.flush()
    runs += 1

data.close()
