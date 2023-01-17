#!/usr/bin/python3

import sys
import re

class reg:

	def __init__(self, str):
		self.teststr = str

	def htmlsearch(self, inp):
		# HTML Search tag Q1
		self.file = inp
		ls = []
		fh = open(self.file, 'r')
		for i in fh:
			#print(i,end='')
			res = re.findall(r'</.+>',i)
			if res:
				ls.append(res)
			else:
				continue
		print(ls)
		fh.close()

	def semisearch(self, listele):
		#Semicolon search tag Q2
		self.ls = listele
		#print(self.ls)
		for i in self.ls:
			#print(i)
			res = re.search(r';$',i)
			if res:
				print("Match")
			else:
				print("No match")
		# #print(type(self.ls))

	def search8(self, listele):
		#Searching for exact 8 letter words Q3
		self.ls = listele
		print(self.ls)
		for i in self.ls:
			res = re.search(r'........',i)
			if res:
				print("Match")
			else:
				print("No match")

	def searchmob(self, inp):
		#Searching for mobile number Q4
		self.files = inp
		fh = open(self.files, 'r')
		for i in fh:
			#print(i, end='')
			if (re.search(r'[0-9]{10}',i)):
				print(i, end='')
			else:
				continue
		fh.close()

	def searchmac(self, inp):
		#Search MAC addresses Q5
		self.files = inp
		fh = open(self.files, 'r')
		for i in fh:
			#print(i, end='')
			if (re.search(r'[a-fA-F0-9]{2}(:[A-Fa-f0-9]{2}){5}',i)):
				print(i,end=' ')
			else:
				continue
		fh.close()

	def searchip(self, inp):
		#Search IP addresses Q6
		self.files = inp
		fh = open(self.files, 'r')
		for i in fh:
			#print(i, end = '')
			if (re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',i)):
				print(i, end='')
			else:
				continue
		fh.close()

	def searchspc(self, inp):
		#Search special characters Q10
		self.files = inp
		count = 0
		fh = open(self.files, 'r')
		for i in fh:
			#print(i, end='')
			if (re.search(r'[\$\!\@\#\%\^\&\*\(\)\<\>\:\;\{\}\[\]\"\'\\\?\/]',i)):
				count = count + 1
				print(i,end='')
			else:
				continue
		print("The count is :", count)
		fh.close()

	def out(self):
		return "The string passed is : {}".format(self.teststr)

def main():
	string = reg('Diwali Bonus')
	#print(string.out())

	#string.htmlsearch(sys.argv[1])
	#string.searchmob(sys.argv[1])
	#string.searchmac(sys.argv[1])
	#string.searchip(sys.argv[1])
	string.searchspc(sys.argv[1])

	#ls = list(map(str, input("Enter the list to check for semicolon :").split()))
	#string.semisearch(ls)
	#string.search8(ls)


if __name__ == '__main__':
	main()
