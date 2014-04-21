import os
import time
import shutil 



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

