from modules.deepsqlite import *
from modules.deephelpers import *

con = connectDB()
createFTStable(con)
populateFTS(con)

deepSearchTitle()
term = input("Enter search term: ")

results = searchFTS(term,con)
print("Found " + str(len(results)) + " results.")

for i in results:
	string = ""
	for j in i:
		string += j
	print(string)
