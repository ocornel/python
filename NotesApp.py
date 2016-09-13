def NewFile():
	''' creates a file for the notes'''
	filename = input("Give a file name: ")
	filename += ".txt"
	newfile = open(filename, 'w')
	newfile.close()
def MakeNote():
	'''User choose file to add notes into then adds note'''
	notefile = input("Which file? ")
	notefile += ".txt"
	notesfile = open(notefile, "a")
	newNoteText = input("Write Note: ")
	newNoteText += "\n"
	notesfile.write(newNoteText)
	notesfile.close()
def ReadNotes():
	'''User chooses the file to read from'''
	notefile = input("Which file to read? ")
	notefile += ".txt"
	try:
		notesfile = open(notefile, "r")
		notelines = notesfile.readlines()
		print()
		for line in notelines:
			print(line, end='')
		notesfile.close()
		print()
	except(FileNotFoundError):
		print("\nTHAT FILE DOES'T EXIST YET\n\tplease use\n\tNewFile()\tto create a new file \n\tMakeNote()\tto make a note\nThen you can read from existing files.\n")

def BulkCreate():
	'''Allows user create a bulk of files'''
	files = input("Enter names of files you want to create comma separated:\n")
	files = files.split(",")
	for fname in files:
		fname += ".txt"
		newfile = open(fname, 'w')
		newfile.close()
