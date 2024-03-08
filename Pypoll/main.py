import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join( "Resources", "election_data.csv")

# Lists  and dictionary to store data

voterid = []
county = []
candidates = []
cand_list = {}

# Open as csvfile:
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Adding headers
    cvs_header= next(csvreader)

#Setting columns
    for row in csvreader:
        # Add voter id
        voterid.append(row[0])

        # Add county
        county.append(row[1])

        #Add candidate
        candidates.append(row[2])


#Total votes

Totalvotes = len(voterid)

#name of the candidates

ccs = "Charles Casper Stockham"
dd = 'Diana DeGette'
rad = 'Raymon Anthony Doane'

#initial variables for vote

v_css=0
v_dd=0
v_rad=0


#Votes for each candidate

for candidate in candidates:
    if candidate == ccs:
        v_css += 1


for candidate in candidates:
    if candidate == dd:
        v_dd += 1


for candidate in candidates:
    if candidate == rad:
        v_rad += 1



# Percentage 
cand_list["Charles Casper Stockham"] = round(v_css/Totalvotes*100,3)
cand_list["Diana DeGette"] = round(v_dd/Totalvotes*100,3)
cand_list["Raymon Anthony Doane"] = round(v_rad/Totalvotes*100,3)


#Setting winner

winner = max(cand_list, key=cand_list.get)

#print the results
print("Election Results")
print("-------------------------")
print("Total Vote: " + str(Totalvotes))
print("-------------------------")
print(ccs + ": "+ str(cand_list["Charles Casper Stockham"]) + "% " + "(" + str(v_css) + ")") 
print(dd + ": " + str(cand_list["Diana DeGette"]) + "% " + "(" + str(v_dd) + ")")
print(rad + ": " + str(cand_list["Raymon Anthony Doane"]) + "% " + "(" + str(v_rad) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")


# Set to a txt file the results
output_result = os.path.join("analysis", "result.txt")

with open(output_result, "w") as txt_file:

    txt_file.write("Election Results" + "\n\n")
    txt_file.write("-------------------------" + "\n\n")
    txt_file.write("Total Vote: " + str(Totalvotes) + "\n\n")
    txt_file.write("-------------------------"+ "\n\n")
    txt_file.write(ccs + ": "+ str(cand_list["Charles Casper Stockham"]) + "% " + "(" + str(v_css) + ")" + "\n\n") 
    txt_file.write(dd + ": " + str(cand_list["Diana DeGette"]) + "% " + "(" + str(v_dd) + ")" + "\n\n")
    txt_file.write(rad + ": " + str(cand_list["Raymon Anthony Doane"]) + "% " + "(" + str(v_rad) + ")" + "\n\n")
    txt_file.write("-------------------------" + "\n\n")
    txt_file.write("Winner: " + str(winner) + "\n\n")
    txt_file.write("-------------------------" + "\n\n")


