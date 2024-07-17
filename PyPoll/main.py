# Import modules
import pandas as pd
import csv

# Load dataset from CSV file
ElectionData = pd.read_csv("~/python-challenge/PyPoll/Resources/election_data.csv")



# Define stats

# Pull out third column of data set
votes_by_candidate = ElectionData['Candidate']



# Counting votes 

# Total number
votes = len(votes_by_candidate)

# Create list of candidates without repetition
candidates = []

for i in range(votes):
    if votes_by_candidate[i] not in candidates:
        candidates.append(votes_by_candidate[i])

# Count votes per candidate
vote_counts = [0]*len(candidates)

for i in range(len(candidates)):
    for j in votes_by_candidate:
        if j == candidates[i]:
            vote_counts[i] = vote_counts[i]+1





# Print analysis in terminal
print("\nElection Results\n")
print("-------------------------\n")
print(f"Total Votes: {votes}\n")
print("-------------------------\n")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {vote_counts[i]/votes*100:.3f}% ({vote_counts[i]})\n")
print("-------------------------\n")