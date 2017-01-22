#!/usr/bin/python

# py-chrome-history
# 
# A script to convert Google Chrome's history file to the standard HTML-ish
# bookmarks file format.
#
# Copyright (c) 2011, 2017 Benjamin D. Esham. This program is released under the
# ISC license, which you can find in the file LICENSE.md.

from __future__ import print_function
from os.path import expanduser
import sqlite3
from sys import argv, stderr

script_version = "1.1"

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

def version_text():
	print("py-chrome-history {}".format(script_version), file=stderr)
	print("(c) 2011, 2017 Benjamin D. Esham", file=stderr)
	print("https://github.com/bdesham/py-chrome-bookmarks", file=stderr)

def help_text():
	version_text()

	print("")
	print("usage: python py-chrome-history input-file output-file", file=stderr)
	print("  input-file is the Chrome history file", file=stderr)
	print("  output-file is the destination for the generated HTML bookmarks file", file=stderr)

# check for help or version requests

if "-v" in argv or "--version" in argv:
	version_text()
	exit()

if len(argv) != 3 or "-h" in argv or "--help" in argv:
	help_text()
	exit()

# the actual code here...

in_file = expanduser(argv[1])
out_file = expanduser(argv[2])

connection = sqlite3.connect(in_file)
curs = connection.cursor()

try:
	out = open(out_file, 'w')
except IOError as e:
	print("py-chrome-history: error opening the output file.", file=stderr)
	print(e, file=stderr)
	exit()

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
