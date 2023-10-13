from modules.deephelpers import *
from modules.deepsqlite import *
import os
import random

inputList = inputList()
titlePrinter()
check = rootcheck()
masterList = []
while len(inputList) > 0:
	if not os.path.exists("../output/deepminer.db"):
		deepminerDB = createDB()
	deepminerCon = connectDB()
	tables = createTables(deepminerCon)
	connectedOnions = []
	url = random.choice(inputList)
	torstatus()
	extensions = ('.jpg', 'jpeg', '.mp4', '.png', '.gif')
	blacklist = ('http://76qugh5bey5gum7l.onion') #This is for any site that makes the program hang excessively long
	if url not in masterList and not url.endswith(extensions) and not url.startswith(blacklist):
		print("New iteration:")
		print("Currently scanning " + url)
		status = onionStatus(url)
		print(status)
		if status != 404:
			html = onionHTML(url)
			if html == "None":
				inputList.remove(url)
				print("Returned TraceError. Moving to next URL")
			else:
				res = []
				onions = onionExtractor(html,url)
				atag = aTag(url,html)
				allonions = onions + atag
				onionResults = list(set(allonions))
				for site in onionResults:
					if site not in res:
						res.append(site)
				newList = inputAdder(onions,inputList)
				masterList.append(url)
				if url in newList:
					newList.remove(url)
				inputList = newList
				print("Found this many sites " + str(len(res)))
				print(res)
				url,urlDir = urlSplitter(url)
				if urlDir == "":
					urlDir = "/"
				data = addDeepData(url,urlDir,html,deepminerCon)
				for connection in res:
					site,siteDir = urlSplitter(connection)
					if siteDir == "":
						siteDir = "/"
					connections = addDeepConnections(url,urlDir,site,siteDir,deepminerCon)
		else:
			inputList.remove(url)
			print("URL gave bad response...not scanning")
	elif url in masterList:
		inputList.remove(url)
		print(url)
		print("URL already scanned")
	elif url.startswith(blacklist):
		inputList.remove(url)
		print(url)
		print("URL in blacklist")
	elif url.endswith(extensions):
		inputList.remove(url)
		print(url)
		print("URL ends with extension not compatible")
'''
#Keeps the program running indefinitely
	while True:
       	python = sys.executable
        os.execl(python, python, *sys.argv)
'''
