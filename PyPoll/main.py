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

# Find winner
winning_total = max(vote_counts)
for i in range(len(candidates)):
    if vote_counts[i] == winning_total:
        winner = candidates[i]


# Print results in terminal
print("\nElection Results\n")
print("-------------------------\n")
# Print total number of votes
print(f"Total Votes: {votes}\n")
print("-------------------------\n")
# Print each candidate's vote percentage and vote total
for i in range(len(candidates)):
    print(f"{candidates[i]}: {vote_counts[i]/votes*100:.3f}% ({vote_counts[i]})\n")
print("-------------------------\n")
# Print winner
print(f"Winner: {winner}\n")
print("-------------------------\n")

# Print results in file
with open("python-challenge/PyPoll/Analysis/PyPoll.txt", "w") as f:
    print("Election Results\n", file=f)
    print("-------------------------\n", file=f)
    # Print total number of votes
    print(f"Total Votes: {votes}\n", file=f)
    print("-------------------------\n", file=f)
    # Print each candidate's vote percentage and vote total
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {vote_counts[i]/votes*100:.3f}% ({vote_counts[i]})\n", file=f)
    print("-------------------------\n", file=f)
    # Print winner
    print(f"Winner: {winner}\n", file=f)
    print("-------------------------\n", file=f)