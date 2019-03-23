<<<<<<< HEAD
#Modules
import os
import csv



#Set path for file
filename = "budget_data.csv"
csvpath = os.path.join("..","raw_data", filename)


#Read in the CSV file
with open(csvpath, newline="") as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #Create a new list
    budgetdata = list()

    #Loop through the data
    for row in csvreader:
        #Append each row from csvreader
        budgetdata.append(row)
        
#Sum of profit/losses over entire perioed
total_profit_loss = 0
for row in budgetdata:
    total_profit_loss = total_profit_loss + int(row[1])

#Total Months
total_months = len(budgetdata)          

#Variables
total_profit_loss_change = 0
greatest_increase_profit = 0
greatest_decrease_profit = 0

#Calculate profit_loss_change
#Find greatest increase and decrease
for i in range(total_months-1):
    profit_loss_change = int(budgetdata[i+1][1]) - int(budgetdata[i][1])
    
    if profit_loss_change >= greatest_increase_profit:
       greatest_increase_profit = profit_loss_change
       greatest_increase_month = budgetdata[i+1][0]

    if profit_loss_change < greatest_decrease_profit:
       greatest_decrease_profit = profit_loss_change
       greatest_decrease_month = budgetdata[i+1][0]

    total_profit_loss_change = total_profit_loss_change + profit_loss_change

    #Calculate average change 
    average_change = total_profit_loss_change/(total_months-1)           

# Generate Paragraph Analysis Output
output = (
f"Financial Analysis \n"
f"----------------------- \n"
f"Total Months: {total_months} \n"
f"Total: ${total_profit_loss} \n"
f"Average Change: ${average_change:.2f} \n"
f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit}) \n"
f"Greatest Decrease in Profits: {greatest_increase_month} (${greatest_decrease_profit}) \n")

# Print all of the results (to terminal)
print(output)

#Set path for result file
filename = "PyBank.txt"

# Save the results to analysis text file
with open(filename, "w") as txtwrite:
    txtwrite.write(output+"\n")
   

=======
#Modules
import os
import csv



#Set path for file
filename = "budget_data.csv"
csvpath = os.path.join("..","raw_data", filename)


#Read in the CSV file
with open(csvpath, newline="") as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #Create a new list
    budgetdata = list()

    #Loop through the data
    for row in csvreader:
        #Append each row from csvreader
        budgetdata.append(row)
        
#Sum of profit/losses over entire perioed
total_profit_loss = 0
for row in budgetdata:
    total_profit_loss = total_profit_loss + int(row[1])

#Total Months
total_months = len(budgetdata)          

#Variables
total_profit_loss_change = 0
greatest_increase_profit = 0
greatest_decrease_profit = 0

#Calculate profit_loss_change
#Find greatest increase and decrease
for i in range(total_months-1):
    profit_loss_change = int(budgetdata[i+1][1]) - int(budgetdata[i][1])
    
    if profit_loss_change >= greatest_increase_profit:
       greatest_increase_profit = profit_loss_change
       greatest_increase_month = budgetdata[i+1][0]

    if profit_loss_change < greatest_decrease_profit:
       greatest_decrease_profit = profit_loss_change
       greatest_decrease_month = budgetdata[i+1][0]

    total_profit_loss_change = total_profit_loss_change + profit_loss_change

    #Calculate average change 
    average_change = total_profit_loss_change/(total_months-1)           

# Generate Paragraph Analysis Output
output = (
f"Financial Analysis \n"
f"----------------------- \n"
f"Total Months: {total_months} \n"
f"Total: ${total_profit_loss} \n"
f"Average Change: ${average_change:.2f} \n"
f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit}) \n"
f"Greatest Decrease in Profits: {greatest_increase_month} (${greatest_decrease_profit}) \n")

# Print all of the results (to terminal)
print(output)

#Set path for result file
filename = "PyBank.txt"

# Save the results to analysis text file
with open(filename, "w") as txtwrite:
    txtwrite.write(output+"\n")
   

>>>>>>> 2080cea94c08148db1206e66d8afa7daad957653
