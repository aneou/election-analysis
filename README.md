# election-analysis
An analysis of some Colorado counties election results

## Overview
Using Python 3.10 the counting of the elction results were automated. The number of votes cast in each county and how much each county contributed to the election. The number of votes cast for each candidate  and how what percentage of the vote they got.
## Results
### Election Results
* Total Votes: 369,711
###
### County Results
* Jefferson:  10.5% (38,855)
* Denver:     82.8% (306,055)
* Arapahoe:   6.7% (24,801)
###
* Largest County Turnout: Denver
###
### Candidate Results
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)
###
* Winner: Diana DeGette: 73.8% (272,892)
## Summary
Using the python code Denver had the greatest turnout and Diana Degette was the winner this election. With a few changes this code can be used for other elections. Although this election was only for one position other elections could have more than one. To do this we can take the header and the ballot id and county to get a list of positions up for election. THen using list of positions up for election as dictionary keys we can create a dictionary with values a list of the variables used in this script i.e. list of candidates, their votes and the winner variables. Then for loops over the dictionary where originally it was just the single position
