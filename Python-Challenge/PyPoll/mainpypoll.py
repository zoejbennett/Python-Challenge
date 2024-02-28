#import os and csv to read in csv
import os
import csv

counter_dict={}
#sample_list=[]

#create path
CSV_PATH = os.path.join('Resources', 'election_data.csv')
ANALYSIS_PATH =  os.path.join('analysis', 'final_poll.txt')

#create empty variables
total_votes = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH, 'r') as csvfile:
    #show delimiter for csv file
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    #skip the header
    csv_header = next(csv_reader)

    for row in csv_reader:
        #calculate how many votes per candidate
        total_votes += 1
        #calculate votes for each candidate
        candidate = row[2]
        if candidate in counter_dict:
             counter_dict[candidate] = counter_dict[candidate]+1
        else: 
             counter_dict[candidate] = 1


        candidate_analysis = ""
        for candidate, votes in counter_dict.items():
            percentage = (votes / total_votes) * 100
            candidate_calc = f"{candidate}: {percentage:.3f}% ({votes})\n"
            candidate_analysis += candidate_calc
            # print(candidate_analysis)

    #calculate candidate with most votes
    winner = (max(counter_dict, key = counter_dict.get))
    


analysis = (
     "Election Results\n"
     "\n"
     "----------------------\n"
     "\n"
     f"Total Votes: {total_votes} \n"
     "----------------------\n"
     f"{candidate_analysis}"
     "\n"
     "----------------------\n"
     "\n"
     f"Winner: {winner}\n"
     "----------------------\n"
)

with open(ANALYSIS_PATH, 'w') as analysis_file:
        analysis_file.write(analysis)
        print(analysis)