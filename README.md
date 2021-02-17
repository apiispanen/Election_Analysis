# Election Analysis

## Project Overview
- A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election:
1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate on.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.
- The counties represented here were Jefferson, Denver & Arapahoe.

### Candidate Results
The candidate results were:
- Charles Casper Stockham got 23.0% of the vote, with 85,213 votes. 
- Diana DeGette got 73.8% of the vote with 272,892 votes. 
- Finally, Raymon Anthony Doane got 3.1% of the vote with 11,606 votes.
<br><br>
<strong>Winner of the Election</strong><br>
The winner of the election was Diana DeGette, with 73.8% of the total vote.
 
### County Results
The county results were:
- Jefferson: 10.5% of the votes, with 38,855 votes cast from there.
- Denver: 82.8% of the votes, with 306,055 votes.
- Arapahoe: 6.7% of the votes, with 24,801 votes.
<br><br>
<strong>Highest County</strong><br>
Denver had the highest county turnout, with a 82.8% of the total vote.

## Setbacks & Challenges
Based on our results, there may have been some setbacks. For one, of the counties representated, Denver held 82.8% of the vote. Based on the population of the county, this may be proportional to the overall population of the 3 counties. However, when one county has such a big vote (82.8%), one may be weary that the one county is disporportionally affecting the election turnout. 

<br><br>Another issue we may see with this code is that

## Election Audit Summary
As a proposal to the election commission, 

### Other Uses for the Code
To re-use this code, we could make minor modifications and accomplish the following for other elections:
1.  <strong>Calculate Voter Turnouts</strong>: Since we know that Denver held 82.8% of the votes cast, we may want to see how porportional this is to the entire population of the 3 counties combined. Therefore, adding a voter turnout as a percentage of the county's total population would be beneficial to seeing as to whether or not a county had equitable representation relative to the others. In the code, we would need to research the populations of each county, and then add a dictionary in the following format: <code>county_populations = {'Arapahoe': 656,590, 'Denver': ...etc }</code> Once we establish this, we can divide the total turnouts for each county by their total population (and then multiply by 100), and get the percent of population that voted. If there is an extreme difference in percent of voter turnouts, then the election commission can make future elections better by making sure underrepresented counties are equal with the others, to avoid voting biases based on location.   

2. <strong></strong>: 
