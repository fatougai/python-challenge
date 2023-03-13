import os
import csv
# election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')
# election_data_csv = '../Resources/election_data.csv'
election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'election_data.csv')
# def print_percentages(election_vote):


#     voter_id = int(election_vote[0])
#     candidate = str(election_vote[2])

# len(election_vote)

totalvotes = 0
candidatevotes = {}
winner = ''
line = "-------------------------"





with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csv_reader)

    for row in csv_reader:
        totalvotes += 1
        if row[2] not in candidatevotes:
            candidatevotes[row[2]] = 1
        else:
            candidatevotes[row[2]] += 1   


pollingresult = os.path.join('.', 'Resources', 'pollingresult.txt')

with open(pollingresult, 'w') as txt_file:


    txt_file.write('Election Results')
    txt_file.write(line)
    txt_file.write('Total Votes: ' + str(totalvotes))
    txt_file.write(line)
    for candidate, votes in candidatevotes.items():
        txt_file.write(candidate + ': ' + '{:.2%}'.format(votes/totalvotes) + '   (' +  str(votes) + ')')
        
    txt_file.write(line) 

    winner = max(candidatevotes, key=candidatevotes.get)

    txt_file.write(f'Winner: {winner}')

    txt_file.write(line) 

    txt_file.write('Election Results:')
    txt_file.write(line)
    txt_file.write('Total Votes: ' + str(totalvotes) )
    txt_file.write(line)
    for candidate, votes in candidatevotes.items():
        txt_file.write(candidate + ': ' + '{:.2%}'.format(votes/totalvotes) + '   (' +  str(votes) + ')')
        
    txt_file.write(line) 

    winner = max(candidatevotes, key=candidatevotes.get)

    txt_file.write(f'Winner: {winner}')

    txt_file.write(line) 
   
