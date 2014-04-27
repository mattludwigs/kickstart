#!/usr/bin/env python

import os
import time
import shutil 


# Set up the files
# Check to see if directory already exists
def check_dir(path):

	if (os.path.exists(path)):
		print("<< directory already exists exiting >>")
		exit()
	else:
		print("<< directory does not exists, continue with start up >>\n")
		time.sleep(1)

# Make name directory
def new_d(dir_name):
	os.makedirs(dir_name)

def dir_change(newdir):
	os.chdir(newdir)	

def new_file(css,js,path):

	if css == "y" and js == "y":
		new_d("./css")
		new_d("./js")
		c = open("./css/style.css", "a")
		j = open("./js/script.js", "a")
		h = open("./index.html", "a")
		c.close
		j.close
		h.close
	elif css == "n" and js == "n":
		h = open("./index.html", "a")
		h.close
	elif css == "y" and js == "n":
		new_d("./css")
		c = open("./css/style.css", "a")
		h = open("./index.html", "a")
		c.close
		h.close
	elif js == "y" and css =="n":
		new_d("./js")
		j = open("./js/script.js", "a")
		h = open("./index.html", "a")
		j.close
		h.close	
	else:
		dir_change("../")
		shutil.rmtree(path)
		print("relaunch")


# HTML template
def html_template(css, js, path):
	h = open("index.html", "w")
	h.write("<!DOCTYPE html>\n<html>\n<head>\n\n  <title>" + path[2:].title() + "</title>\n")
	if css == "y":
		h.write("\n  <link rel='stylesheet' href='css/style.css'>\n\n")
	h.write("</head>\n")
	h.write("<body>\n\n\n\n")	
	if js == "y":
		h.write("  <!-- Scripts -->\n\n  <script src='js/script.js'></script>\n\n")
	h.write("</body>\n</html>")				


# runs kick start
def main():

	import os
	import time
	import shutil 


	path = raw_input("Enter the directory name: ")

	check_dir(path)

	need_css = raw_input("Do you need css? (y or n)\n> ")
	need_js = raw_input("Do you need JavaScript? (y or n)\n> ")

	new_d(path)
	dir_change(path)

	new_file(need_css,need_js,path)
	html_template(need_css,need_js,path)

if __name__ == "__main__":
    main()

