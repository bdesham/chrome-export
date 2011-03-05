#!/usr/bin/python

# py-chrome-history
# 
# A script to convert Google Chrome's history file to the standard HTML-ish
# bookmarks file format.
#
# (c) Benjamin Esham, 2011.  See the accompanying README for this file's
# license and other information.

import sys, os, sqlite3

# html escaping code from http://wiki.python.org/moin/EscapingHtml

html_escape_table = {
	"&": "&amp;",
	'"': "&quot;",
	"'": "&#39;",
	">": "&gt;",
	"<": "&lt;",
	}

def html_escape(text):
	return ''.join(html_escape_table.get(c,c) for c in text)

def sanitize(string):
	res = ''
	string = html_escape(string)

	for i in range(len(string)):
		if ord(string[i]) > 127:
			res += '&#x%x;' % ord(string[i])
		else:
			res += string[i]

	return res

in_file = os.path.expanduser(sys.argv[1])
out_file = os.path.expanduser(sys.argv[2])

connection = sqlite3.connect(in_file)
curs = connection.cursor()

out = open(out_file, 'w')

out.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>

<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
<title>Bookmarks</title>
<h1>Bookmarks</h1>

<dl><p>

<dl><dt><h3>History</h3>

<dl><p>""")

curs.execute("SELECT url, title FROM urls")

for row in curs:
	if len(row[1]) > 0:
		out.write('<dt><a href="%s">%s</a>\n' % (sanitize(row[0]), sanitize(row[1])))

connection.close()

out.write("</dl></p>\n</dl>")

out.close()
