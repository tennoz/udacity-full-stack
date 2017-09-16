import re
import os
def rename_files():
	file_list = os.listdir(r"/media/ahmad/C2169F8B169F7EDB/Courses/laracast")
	original_path = os.getcwd()
	os.chdir(r"/media/ahmad/C2169F8B169F7EDB/Courses/laracast")

	for file_name in file_list:
		# print("Old name is " + file_name)
		# print("New name is " + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.replace('Laracasts - ', ''))
		
	os.chdir(original_path)

rename_files()