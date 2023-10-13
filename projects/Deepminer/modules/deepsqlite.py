import os
import sqlite3

def createDB():
	con = sqlite3.connect('output/deepminer.db')
	return con

def connectDB():
	con = sqlite3.connect('output/deepminer.db', timeout=30)
	return con

def createTables(con):
	cur = con.cursor()
	deepdata = """
	CREATE TABLE IF NOT EXISTS "Deepdata" (
	"URL"   TEXT,
	"Directory"     TEXT,
	"HTML"  TEXT,
	PRIMARY KEY('URL', 'Directory')
	);"""
	cur.execute(deepdata)

	deepconnections = """
	CREATE TABLE IF NOT EXISTS "Deepconnections" (
	"URL"	TEXT,
	"URLDIR"	TEXT,
	"SITE"	TEXT,
	"SITEDIR"	TEXT,
	PRIMARY KEY("URL","SITE","URLDIR","SITEDIR")
	);
	"""
	cur.execute(deepconnections)

def addDeepData(url,directory,html,con):
	cur = con.cursor()
	addData = "INSERT OR REPLACE INTO Deepdata (URL, Directory, HTML) VALUES (?, ?, ?)"
	cur.execute(addData,(url, directory, html))
	con.commit()

def addDeepConnections(url, urlDir, site, siteDir,con):
	cur = con.cursor()
	addConnections = "INSERT OR REPLACE INTO Deepconnections (URL, URLDIR, SITE,SITEDIR) VALUES (?, ?, ?, ?)"
	cur.execute(addConnections,(url,urlDir,site,siteDir))
	con.commit()

def queryTables(con):
	cur = con.cursor()
	cur.execute("SELECT URL, Directory, HTML FROM Deepdata")
	results = cur.fetchall()
	for row in results:
		print(row)

	cur.execute("SELECT URL,URLDIR,SITE,SITEDIR FROM Deepconnections")
	results = cur.fetchall()
	for row in results:
		print(row)

def commitDB(con):
	try:
		con.commit()
	except:
		con.rollback()
		raise RuntimeError("Error occurred. Rolling back database.")

def searchDB(term,con):
	cur = con.cursor()
	query = "SELECT URL,Directory FROM Deepdata WHERE HTML LIKE \'%" + term + "%\' ORDER BY URL;"
	cur.execute(query)
	results = cur.fetchall()
	return results

def createFTStable(con):
	cur = con.cursor()
	query = "CREATE VIRTUAL TABLE IF NOT EXISTS Deepsearch USING fts5(URL, Directory, HTML);"
	cur.execute(query)

def populateFTS(con):
	cur = con.cursor()
	query = "INSERT INTO Deepsearch SELECT URL, Directory, HTML FROM Deepdata;"
	cur.execute(query)

def searchFTS(term,con):
	cur = con.cursor()
	query = "SELECT URL,Directory FROM Deepsearch WHERE HTML MATCH \'" + term  + "\' ORDER BY rank;"
	cur.execute(query)
	results = cur.fetchall()
	return results
