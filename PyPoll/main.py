#import os and csv files
import os
import csv

#initialize variables
candidates = []
num_votes = 0
vote_counts = []

#set path
#file_name = 'election_data_2.csv'
#filepath = os.path.join('raw_data',file_name)
election_data_csv_path = os.path.join("Resources", "election_data.csv") 
election_data_txt_path = os.path.join("Analysis" , "pypoll_results_summary.txt")


#open the file
with open(election_data_csv_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    line = next(csvreader,None)

    #go line by line and process each vote
    for line in csvreader:

        #add to total number of votes
        num_votes = num_votes + 1

        #candidate voted for
        candidate = line[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()