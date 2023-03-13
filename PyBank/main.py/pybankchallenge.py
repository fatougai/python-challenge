import os
import csv
from statistics import mean

#budget_data_csv = '../Resources/budget_data.csv'
#budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')


totalvolume = 0
monthCount = 0
greatestincrease = 0
greatestdecrease = 0
bestmonth = ''
worstmonth = ''
line = "--------------------------"

EachMonthChange = []
change = []

with open(budget_data_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        monthCount += 1
        totalvolume += int(row[1])
        if int(row[1]) > greatestincrease:
            bestmonth = (row[0])
            greatestincrease = int(row[1])
        elif int(row[1]) < greatestdecrease:
            worstmonth = (row[0])
            greatestdecrease = int(row[1])
        change.append(int(row[1]))

  
# for monthly changes
for i in range(len(change)-1):
    monthlychange = (change[i+1] - change[i])
    EachMonthChange.append(monthlychange)   

average_change = mean(EachMonthChange)

print("Financial Analysis")
print(line) 

print("Total Months: " + str(monthCount))
print("Average Change is: $" + str(round(average_change, 2)))
print("Total: $" + str(totalvolume))
print("Greatest Increase in Profits: " + str(bestmonth) + "  ($" + str(greatestincrease) + ")")
print("Greatest Decrease in Profits: " + str(worstmonth) + "  ($" + str(greatestdecrease) + ")")


""" f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(monthCount))
f.write("Average Change is: $" + str(round(averageChange, 2)))
f.write("Total: $" + str(totalVolume))
f.write("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
f.write("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")
 """