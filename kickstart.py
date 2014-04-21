#!/usr/bin/env python
# runs kick start
from files import *
from templates import *

path = raw_input("Enter the directory name: ")

check_dir(path)

template = raw_input("What type of project? (HTML, PHP, ect.)\n> ")
need_css = raw_input("Do you need css? (y or n)\n> ")
need_js = raw_input("Do you need JavaScript? (y or n)\n> ")


new_d(path)
dir_change(path)

new_file(need_css,need_js,path)

which_template(template,need_css,need_js,path)

