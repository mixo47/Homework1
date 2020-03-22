import os
​
import csv
​
​
election_data = os.path.join("..","Resources","election_data.csv")
​
​
candidates = []
​
num_votes = []
​
​
percent_votes = []
​
​
total_votes = 0
​
​
with open(election_data, newline = "") as csvfile:
​
    csvreader = csv.reader(csvfile, delimiter = ",")
​
    csv_header = next(csvreader)
​
​
​
    for row in csvreader:
​
​
        total_votes += 1 
​
        if row[2] not in candidates:
​
            candidates.append(row[2])
​
            index = candidates.index(row[2])
​
            num_votes.append(1)
​
        else:
​
            index = candidates.index(row[2])
​
            num_votes[index] += 1
​
​
​
    for votes in num_votes:
​
        percentage = (votes/total_votes) * 100
​
        percentage = round(percentage)
​
        percentage = "%.3f%%" % percentage
​
        percent_votes.append(percentage)
​
​
    winner = max(num_votes)
​
    index = num_votes.index(winner)
​
    winning_candidate = candidates[index]
​
​
print("Election Results")
​
print("--------------------------")
​
print(f"Total Votes: {str(total_votes)}")
​
print("--------------------------")
​
for i in range(len(candidates)):
​
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
​
print("--------------------------")
​
print(f"Winner: {winning_candidate}")
​
print("--------------------------")
​
​
​
# Exporting to .txt file
​
output = open("output.txt", "w")
​
line1 = "Election Results"
​
line2 = "--------------------------"
​
line3 = str(f"Total Votes: {str(total_votes)}")
​
line4 = str("--------------------------")
​
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
​
for i in range(len(candidates)):
​
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
​
    output.write('{}\n'.format(line))
​
line5 = "--------------------------"
​
line6 = str(f"Winner: {winning_candidate}")
​
line7 = "--------------------------"
​
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
Collapse




Veysel  9:27 PM
pyBank
main_Pybank.py 
​
import os
​
import csv
​
budget_data = os.path.join("..","Resources", "budget_data.csv")
​
with open(budget_data, newline="") as csvfile:
​
    csvreader = csv.reader(csvfile, delimiter=",")
​
    csv_header = next(csvfile)
​
    print(f"Header: {csv_header}")
​
    P = []
​
    Months = []
​
    # find revenue change
​
    revenue_change = []
​
    for rows in csvreader:
​
        P.append(int(rows[1]))
​
        Months.append(rows[0])
​
​
    for i in range(1, len(P)):
​
        revenue_change.append((int(P[i]) - int(P[i-1])))
​
    revenue_average = sum(revenue_change) / len(revenue_change)
​
    total_months = len(Months)
​
    greatest_increase = max(revenue_change)
​
    greatest_decrease = min(revenue_change)
​
    print("Financial Analysis")
​
​
    print("...................................................................")
​
​
    print("total months: " + str(total_months))
​
​
​
    print("Total: " + "$" + str(sum(P)))
​
​
​
    print("Average change: " + "$" + str(revenue_average))
​
​
​
    print("Greatest Increase in Profits: " + str(Months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
​
​
​
    print("Greatest Decrease in Profits: " + str(Months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))
​
​
    file = open("output.txt","w")
​
​
​
    file.write("Financial Analysis" + "\n")
​
​
​
    file.write("......................................................................" + "\n")
​
​
​
    file.write("total months: " + str(total_months) + "\n")
​
​
​
    file.write("Total: " + "$" + str(sum(P)) + "\n")
​
​
​
    file.write("Average change: " + "$" + str(revenue_average) + "\n")
​
​
​
    file.write("Greatest Increase in Profits: " + str(Months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
​
​
​
    file.write("Greatest Decrease in Profits: " + str(Months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
​
​
​
    file.close()


