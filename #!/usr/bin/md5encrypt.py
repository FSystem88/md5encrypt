#!/usr/bin/python3
# Author: FSystem88
class md5encrypt:
	def main():
		import requests, random, datetime, sys, time, argparse, hashlib, sqlite3
		from hashlib import md5
		parser = argparse.ArgumentParser(prog='md5encrypt', description="Fucking shit by FSystem88. May be not work!)",epilog='E-mail: FSystem88@bk.ru')
		parser.add_argument('--dict', help='dictionary (unencrypted words)')
		args = parser.parse_args()
		dict = args.dict
		if dict == None:
			print("File none!")
			exit()
		try:
			db = sqlite3.connect("md5encrypt.db")
			dbs = db.cursor()
			dbs.execute("CREATE TABLE dbMD5 (instr text, inmd5 text)")
		except:
			pass
		try:
			with open(dict) as file:
				int = 0
				array = [row.strip() for row in file]
				while array[0+int] != '':
					istr = array[0+int]
					imd5 = hashlib.md5(array[0+int].encode("utf")).hexdigest()
					db = sqlite3.connect("md5encrypt.db")
					dbs = db.cursor()
					dbs.execute("SELECT * FROM dbMD5 WHERE instr='{}'".format(istr))
					data=dbs.fetchall()
					if len(data)==0:
						dbs.execute("INSERT INTO dbMD5 (instr, inmd5) VALUES ('{}', '{}')".format(istr, imd5))
						print('№: '+istr+', md5: '+imd5)
					else:
						pass
					db.commit()
					int += 1
		except:
			pass
md5encrypt.main()
