import csv, os

#1. Open the Data File
file_to_load = os.path.join("resources","election_results.csv")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

#2. Write down the names of all the candidates
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n________________________\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")

#3. Add a vote count for each candidate

#4. Get the total votes for each candidate
#5. Get the total votes cast for the election