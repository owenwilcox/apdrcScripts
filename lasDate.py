import glob
import xml.etree.ElementTree as ET

"""
This file was written by Owen Wilcox on Thursday, April 18, 2019.
It edits existing XML files's time structure without needing to go into each individually,
and should mostly eliminate syntax errors
"""
def main():

	fileList = getFilenames()

	for filename in fileList:
		print "Editing " + filename
		addRootElement(filename)
		editTime(filename)
		removeRootElement(filename)

def addRootElement(filename):
	"""
	The default LAS xml files don't have roots, which is a problem for the library we use to parse the xml.
	For this reason, this method adds a dummy root element to the XML files, which is removed later by the 
	corresponding removeRootElement() method. 
	Parameters: the name of the file to be changed.
	Returns: Nothing
	"""

	#Open the file, read its contents into a variable, then close the file
	f = open(filename, "r")
	allLines = f.readlines()
	f.close()

	#Add <root> at the beginning of the list of lines and </root> at the end
	allLines.insert(0, "<root>\n")
	allLines.append("</root>")
	
	#Re-open the file, and overwrite its contents including the new elements
	f = open(filename, "w")
	f.write("".join(allLines))
	f.close()


def editTime(filename):
	""" 
	editTime() looks through the file for the time tag. Once it finds it, it prompts the user for the new size.
	If the user doesn't provide a value, the existing value is left unchanged. 
	Parameters: the name of the file to be changed
	Returns: Nothing. File is edited in place. 
	"""

	#Open the file for parsing, and find the root element
	et = ET.parse(filename)
	root = et.getroot()
	#Navigate to the axes element
	axes = root.findall('axes/*')

	timenodes = []

	#For each element in axes (since files can have more than one time axis), add it to the list of elements to modify
	for ele in axes:
		if ele.attrib["type"] == "t":
			timenodes.append(ele)

	#Information for the user as to which time entry they're editing
	print "Number of time entries: " + str(len(timenodes))

	#Find the time element, get its size, print that, get the new size, and change if it it's a number + not blank.
	for timenode in timenodes:
		arange = timenode[0]	
		child = timenode.getchildren()
		currentSize =  arange.attrib["size"]
		print "Current size for " + timenode.tag +  " is: " + currentSize
		print "Enter new size: "
		newSize = raw_input()
		if not newSize.isalpha():
			newSize = currentSize
			print "Blank or not number. Size unchanged"
		arange.attrib["size"] = newSize

	#Write back to the file
	et.write(filename)	


def removeRootElement(filename):
	"""
	Removes the root element that was added in addRootElement
	Parameters: the name of the file to be changed
	Returns: Nothing
	"""
	
	f = open(filename, "r")
	allLines = f.readlines()
	f.close()

	allLines.remove("<root>\n")
	allLines.remove("</root>")
	

	f = open(filename, "w")
	f.write("".join(allLines))
	f.close()


def getFilenames():
	"""
	Gets a GDS URL from the user, then looks for all the XML files in the data_xml directory that contain
	that URL. Also creates versions with :80 added and :80 removed, to match any possible cases.
	Parameters: None
	Returns: A list of files containing the user-provided GDS URL
	"""	



	#fileList = glob.glob("/usr/local/tomcat1/content/las86/conf/server/data_xml/*.xml")
	fileList = glob.glob("./*.xml")	
	
	print "Enter GDS URL"
	#might have 80 in the URL, so we check right here
	searchPattern80 = raw_input()

	#remove 80 from where it should always be
	searchPattern = searchPattern80.split('/')
	searchPattern[2] = searchPattern[2][:-3]
	searchPattern = "/".join(searchPattern)
	
	#add 80 in case it's not there
	searchPatternAdd80 = searchPattern80.split('/')
	searchPatternAdd80[2] = searchPatternAdd80[2]+":80"
	searchPatternAdd80 = "/".join(searchPatternAdd80)

	filenames = []

	#Check each condition 
	for fileName in fileList:
		f = open(fileName, "r")
		for line in f:
			if searchPattern in line:
				filenames.append(fileName)
			elif searchPattern80 in line:
				filenames.append(fileName)
			elif searchPatternAdd80 in line:
				filenames.append(fileName)

	filenames = list(set(filenames))

	return filenames

if __name__ == "__main__":
	main()
