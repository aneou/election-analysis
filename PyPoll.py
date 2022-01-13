import csv, os


#variable for load file path
file_to_load = os.path.join("resources","election_results.csv")

#Variable for save file path
file_to_save = os.path.join("analysis","election_analysis.txt")

#track election info
total_votes = 0
candidate_options = []
candidate_votes = {}

#track winning candidate info
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #remove headers from file reader
    headers = next(file_reader)

    for row in file_reader:
        #count total votes
        total_votes += 1
        #get candidate name from vote
        name = row[2]

        #add candidate to list if not in it
        if name not in candidate_options:
            candidate_options.append(name)
            #create candidate's vote count
            candidate_votes[name] = 0

        #count candidate's vote
        candidate_votes[name] +=1
#save results to file
with open(file_to_save, "w") as txt_file:
    election_results = (
                f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)
    # find candidates voting percentage
    for candidate_name in  candidate_options:
        #get candidates votes
        votes = candidate_votes[candidate_name]
        #calculate percentage of vote from total votes
        vote_percentage = float(votes/total_votes)*100
        candidate_result =(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
        print(candidate_result, end="")
        txt_file.write(candidate_result)
        #find winning candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)