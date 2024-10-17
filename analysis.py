import main
import time
import csv

data = open("record.csv", 'a+', newline="\n")
writer = csv.writer(data)
runs = 0

while runs < 500:
    ctime = time.time()
    status = main.solve()
    print(status)
    writer.writerow([time.time() - ctime, status])
    data.flush()
    runs += 1

data.close()
