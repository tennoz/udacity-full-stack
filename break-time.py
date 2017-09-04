import time
import webbrowser

num = 1
print("this prgram started on " + time.ctime())
while(num <= 3):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=UDvobdLt_po")
	num = num + 1
