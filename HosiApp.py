'''Create patient's files during registration and allow for editing of them'''
from datetime import *
dt = datetime.now()
def InitiateApp():
	inp = input("This will clear every previous record and start you afresh.\nPress Y to innitiate app or any other character to calncel\n: ")
	if inp == 'Y' or inp == 'y':
		open("RegNumbers.txt", "w").write("0")
		print("App Innitiated.\nUse Reg() to Register patients\nUse UpdateRecord() to update a patient's record\nUse ReadRecord() to read patient's record.")
	else:
		print("The App wasn't reinitiated. Previous records are intact")
	
def Reg():
	'''Register patients'''
	try:
		reglistfile = open("RegNumbers.txt", "r")
		reglist = reglistfile.readlines()
		newReg = str(int(reglist[len(reglist)-1]) + 1)
		reglistfile.close()
		editreglist = open("RegNumbers.txt", "a")
		writethis = "\n"+ str(int(reglist[len(reglist)-1]) + 1)
		editreglist.write(writethis)
		editreglist.close()
		filename = newReg + ".html"
		newfile = open(filename, 'w')
		newfile.close()
		newfile = open(filename, 'a')
		pname = input("Name: ")
		yob = input("Year of Birth: ")
		age = dt.year - int(yob)
		title = "<html><head><title>" + newReg + " - " + pname+ "</title></head><h1>PATIENT RECORDS FOR REGISTRATION NUMBER " + newReg+"</h1>"
		newfile.write(title)
		record = "\n<b>NAME: </b>\t\t\t" + pname + "\n<br><b>YEAR OF BIRTH: </b>\t" + yob + "\n<br><b>AGE: </b>\t\t" + str(age) + "\n<br>"
		newfile.write(record)
		newfile.close()
	except(FileNotFoundError):
		print("\nTHE APP HASN'T BEEN INNITIATED YET\nUse InnitiateApp() to innitiate the app.")
def ReadRecord():
	'''Reads record of a patient by patient ID'''
	notefile = input("Patient ID: ") + ".html"
	try:
		notesfile = open(notefile, "r")
		notelines = notesfile.readlines()
		print()
		for line in notelines:
			print(line, end='')
		notesfile.close()
		print()
	except(FileNotFoundError):
		print("\nTHAT FILE DOES'T EXIST YET\n")
def UpdateRecord():
	'''Updates a patient record'''
	notefile = input("Patient ID ") + ".html"
	try:
		notesfile = open(notefile, "r")
		notesfile.close()
		notesfile = open(notefile, "a")
		newNoteText = "<p>\n" + input("Write Note: ") + "</p>\n"
		noteDnT = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) + " At " + str (dt.hour) + ":" +str(dt.minute) 
		notesfile.write("<br><u>Recorded at " + "<b>" + noteDnT + "</b></u>" + newNoteText)
		notesfile.close()
	except(FileNotFoundError):
		print("\nTHAT PATIENT REGISTRATION DOESN'T EXIST YET\n")
