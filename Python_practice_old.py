print('hello world')

counties = ['Arapahoe', 'Denver', 'Jefferson']
counties.append("El Paso")
counties.insert(2, "El Paso")
counties.remove("El Paso")

counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438


voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.insert(1,{"county":"El Paso", "registered_voters": 46119})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Denver", "registered_voters": 463353})

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")




print(voting_data)
