#Import Module
import os, csv
from pathlib import Path 

#Use Pathlib To Name File Location
csv_file_path = Path("./Resources/election_data.csv")

#List Variables 
total_votes = 0 
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

#Open csv
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    #Put Election_data.csv in csvreader
    csvreader = csv.reader(elections,delimiter=",") 

    #Bypass Header (don't want this included in data)
    header = next(csvreader)     

    #Specify Rows
    for row in csvreader: 

        #The total_votes Variable Holds The Count of Unique IDs
        total_votes +=1

        #4 Candidates (Count # of Times Name Appears/Store In List)
        if row[2] == "Charles Casper Stockham": 
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony_Doane_votes +=1

 #Make A Dictionary From Our 2 Lists (To Find Winner)
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes, Raymon_Anthony_Doane_votes]

# Zip Together: candidate(key) & the total votes(value)
# Max Function (of Dictionary) Will Reveal Winner
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Print Analyses Summary
Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_votes) *100
Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) *100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_votes) *100

#Print Summary Table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Output The File
output_file = Path("./Resources/Election_Results_Summary.txt")

with open(output_file,"w") as file:

#What To Print In Elections_Results_Summary:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
