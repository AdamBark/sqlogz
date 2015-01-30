import sqlite3
import logging

class DBWriter(object):

	def __init__(self, dbPath):
		self._dbPath= dbPath
		self._logCursor = None
		self._conn = None
		self._initDB()

	def _initDB(self):
		self._conn = sqlite3.connect(self._dbPath)
		self._logCursor = self._conn.cursor()
		self._logCursor.execute('DROP TABLE IF EXISTS logTable')
		self._logCursor.execute('''CREATE TABLE logTable (loglevel INT, pathname TEXT, lineno INT, func TEXT, message TEXT)''')

	def _createEntryFromRecord(self, record):
		""" Return dict corresponding to our schema """
		entry = dict(loglevel = record.levelno, pathname = record.filename, lineno = record.lineno, function = record.funcName, message = record.msg)
		return entry

	def _insertEntry(self, entry):
		self._logCursor.execute("INSERT INTO logTable VALUES ('%(loglevel)s', '%(pathname)s', '%(lineno)d', '%(function)s', '%(message)s')" %entry )

	def insertRecord(self, record):
		entry = self._createEntryFromRecord(record)
		self._insertEntry(entry)
	
	def commit(self):
		self._conn.commit()
		
	def close(self):
		self._conn.close() 
	
	def printDB(self):
		print "** DB ENTRIES **"
		self._logCursor.execute("SELECT * FROM logTable")
		print self._logCursor.fetchall()


def test():
	print "starting test..."
	dbw = DBWriter("/tmp/logTable.sqlite")
	r = logging.LogRecord("testName", 2, "/blah.txt", 3, "test message", None, None)
	r2 = logging.LogRecord("testName6", 2, "/blah1.txt", 3, "test message2", None, None)

	dbw.insertRecord(r)
	dbw.insertRecord(r2)
	dbw.commit()
	dbw.printDB()
	dbw.close()
	print "finished test."
	
		
	
	
