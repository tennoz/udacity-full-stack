import urllib

def read_text():
	quotes = open("/media/ahmad/C2169F8B169F7EDB/Dev/udacity/fullstack-web-development/text")
	contents = quotes.read()
	print(contents)
	quotes.close()
	check(contents)

def check(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
	output = connection.read()
	if "true" in output:
		print("Profanity Alert!")
	elif "false" in output:
		print("This text has no curse words.")
	else:
		print("Couldn't scan the doc.")

read_text()