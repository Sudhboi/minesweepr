import csv

data = open('record.csv', 'r')
list = csv.reader(data)

won = 0
lost = 0
unlucky = 0

for record in list:
    if record[1] == "Won":
        won += 1
    elif record[1] == "Triggered Mine":
        lost += 1
    elif record[1] == "Unlucky Start":
        unlucky += 1
    
total = won + lost + unlucky

print("Total Games - {}".format(total))
print("Won - {}, Lost - {}, Unlucky - {}".format(won, lost, unlucky))

print("Percent of Unlucky Games - {:.2%}".format((unlucky/total)))
print("Percent of Won Games - {:.2%}".format((won/total)))
print("Percent of Lost Games - {:.2%}".format((lost/total)))

print("Percent of Winnable Games Won - {:.2%}".format((lost/(won + lost))))