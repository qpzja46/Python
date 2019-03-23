# Modules
import csv
import os

# File to load and output
file_to_load = os.path.join("raw_data","election_data.csv")
file_to_output = os.path.join("analysis", "election_result" )

# Set variables
each_vote_count = 0
total_vote_count = 0
highest_vote_count = 0

# Get data file
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)


# 1. Create a dictionary called candidate_information
#   candidate_information = {"key": value}
#   Key (string) is name of candidate
#   value (list) is candidate_vote_detail
#       in the candidate_vote_detail, I would like to store each_vote_count and percentage_vote
#
# It will look like this
# candidate_information = {"name of candidate 1": [each_vote_count, percentage_vote],
#                           ...                                                     }

    candidate_information = {}
    candidate_vote_detail = [0,0]


# Examine each row in the csv file and fill the dictionary with using .items()
# Also keep adding other candidates to examine
    for row in csvreader:
        total_vote_count += 1
        if row[2] in candidate_information.keys():
            candidate_information[row[2]] = candidate_information[row[2]] + 1
        else:
            candidate_information[row[2]] = 1

# Examine the dictionary to calculate percentage_vote and highest_vote_count
percentage_vote = 0
total_vote_count = 0
for v in candidate_information.values():
    total_vote_count = total_vote_count + v
    total_percentage = v / total_vote_count


total_percentage = []
for v in candidate_information.values():
    percentage_vote = str(round(v/total_vote_count,2)*100) + "%"
    total_percentage.append(percentage_vote)


#creates winner_list to put winners (even if there is a tie)
winner_list = 0

for key, value in candidate_information.items():
    if value > winner_list:
        winner_list = value 
        winner = key

# # makes winner_list a str with the first entry
# winner = winner_list[0]
        
# Generate Paragraph Analysis Output
output_1 = (
f"Election Results \n"
f"----------------------- \n"
f"Total Votes: {total_vote_count} \n"
f"----------------------- \n")

# Create candidate specific message with their voting record
# Print all of the results (to terminal)
for key, v in candidate_information.items():
    output_1 = output_1 + f"{key}: {(v/total_vote_count)*100:.2f}% ({v}) \n"

print(output_1)

# Generate winner
output_2 = (
f"----------------------- \n"
f"Winner: {winner} \n"
f"----------------------- \n")

#Print
print(output_2)

#Set path for result file
filename = "PyPoll.txt"

# Save the results to analysis text file
with open(filename, "w") as txtwrite:
    txtwrite.write(output_1+output_2+"\n")