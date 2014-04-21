#!/usr/bin/env python

from files import *
from templates import *

path = raw_input("Enter the directory name: ")

check_dir(path)

need_css = raw_input("Do you need css? (y or n)\n> ")
need_js = raw_input("Do you need JavaScript? (y or n)\n> ")

new_d(path)
dir_change(path)

new_file(need_css,need_js,path)
html_template(need_css,need_js,path)


