# Check template
def which_template(template,css,js,path):
	if template == "HTML":
		html_template(css,js,path)


# HTML document
def html_template(css, js, path):
	h = open("index.html", "w")
	h.write("<!DOCTYPE html>\n<html>\n<head>\n\n  <title>" + path[3:].title() + "</title>\n")
	if css == "y":
		h.write("\n  <link rel='stylesheet' href='css/style.css'>\n\n")
	h.write("</head>\n")
	h.write("<body>\n\n\n\n")	
	if js == "y":
		h.write("  <!-- Scripts -->\n\n  <script src='js/script.js'></script>\n\n")
	h.write("</body>\n</html>")	
	