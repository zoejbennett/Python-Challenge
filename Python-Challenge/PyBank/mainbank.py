#import os and csv to read in csv
import os
import csv

#create path
CSV_PATH = os.path.join('Resources', 'budget_data.csv')
ANALYSIS_PATH =  os.path.join('analysis', 'final_bank.txt')


#create empty variabels before initiating loops
months_count = 0
total_profit = 0
total_change = 0
max_profit_val = ["",-1000000000]
max_loss_val = ["", 1000000000]
max_profit_month = None
max_loss_month = None
previous_profit = None

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH, 'r') as csvfile:
    #show delimiter for csv file
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    #skip the header
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        #calculations: 
        #print total number of months included in the dataset
        
        months_count += 1
        current_month = row[0]
        current_profit = int(row[1])
        
        #print(current_profit)
        total_profit += current_profit
        # calculate total profit change
        if previous_profit is not None:
                current_change = current_profit - previous_profit
                total_change += current_change
        
      

        #calculate max value
        if previous_profit is not None:
                current_change = current_profit - previous_profit
                total_change += current_change
                if current_change > max_profit_val[1]:
                        max_profit_val[1] = current_change
                        max_profit_month = current_month

        #calculate min value
        if previous_profit is not None:
               current_change = current_profit - previous_profit
               total_change += current_change
               if current_change < max_loss_val[1]:
                        max_loss_val[1] = current_change
                        max_loss_month = current_month
                        
  #prepare for next row
        previous_profit = current_profit
#calculate average change: total change/(Months -1 )
average_change = round(total_change/(months_count-1), 2)


analysis = (
     "Financial Analysis\n"
     "\n"
     "-----------------"
     "\n"
     f"Total Months: {months_count}\n" 
     f"Total: ${total_profit}\n"
     f"Average Change: {average_change}\n"
     f"Greatest Increase in Profits: {max_profit_month} (${max_profit_val[1]})\n"
     f"Greatest Loss in Profits: {max_loss_month} (${max_loss_val[1]})\n"
)

with open(ANALYSIS_PATH, 'w') as analysis_file:
        analysis_file.write(analysis)
        print(analysis)
