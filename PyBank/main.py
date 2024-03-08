import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
date = []
profitlosses = []
change = []

#Setting last profit/loss
l_proffit =0

# Open as csvfile:
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Adding headers
    cvs_header= next(csvreader)

#Setting columns
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add profitlosses
        profitlosses.append(row[1])

        #difference proffit losses
        diff=int(row[1])-int(l_proffit)
        l_proffit= row[1]
        change.append(diff)

#lists together
cleaned_csv = list(zip(date, profitlosses))

#Counting months
month = len(date)

#  Total revenue
total = 0

for pl in profitlosses:
    total = total+int(pl)


# Average between each line in proffit/losses
change_pl = 0

for ch_pl in change:
    change_pl = change_pl+int(ch_pl)

avg_change= round((change_pl-change[0])/(month-1),2)


# Great increase
greatincrease= max(change)
ind_greatincrease = change.index(greatincrease)
month_gi = date [ind_greatincrease]



# Great increase
greatdecrease= min(change)
ind_greatdecrease = change.index(greatdecrease)
month_gd = date [ind_greatdecrease]


#Print the results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month))
print("Total: $" + str(total))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + str(month_gi) + " " + "($" + str(greatincrease) + ")")
print("Greatest Decrease in Profits: " + str(month_gd) + " " + "($" + str(greatdecrease) + ")")


#Create a txt file 
output_result = os.path.join("analysis", "result.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Financial Analysis" + "\n\n") 
    txt_file.write("----------------------------"+"\n\n")
    txt_file.write("Total Months: " + str(month) + "\n\n")
    txt_file.write("Total: $" + str(total) + "\n\n")
    txt_file.write("Average Change: $" + str(avg_change) + "\n\n")
    txt_file.write("Greatest Increase in Profits: " + str(month_gi) + " " + "($" + str(greatincrease) + ")" + "\n\n")
    txt_file.write("Greatest Decrease in Profits: " + str(month_gd) + " " + "($" + str(greatdecrease)+ ")" + "\n\n")