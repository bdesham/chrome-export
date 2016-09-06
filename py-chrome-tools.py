#!/usr/bin/python

# py-chrome-tools
# 
# A toolset to parse/convert Google Chrome's bookmarks and history file formats, allowing:
# - export to standard HTML-ish bookmarks file format
# - TODO:
#
# Copyright (c) 2011 Benjamin D. Esham. This program is released under the ISC
# license, which you can find in the file LICENSE.md.

import json, sys, os, re, sqlite3

script_version = "1.1"

# Obtain script 'logical name' (without path or .py ending):
script_path = sys.argv[0]
script_name = script_path[ script_path.rfind('/')+1: ]
if script_name.rfind('.py') == len(script_name)-3:
    script_name = script_name[ :-3]

def fatal(msg):
    sys.write.stderr("fatal: " + msg)
    sys.exit(1)

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

def html_for_node(node):
	if 'url' in node:
		return html_for_url_node(node)
	elif 'children' in node:
		return html_for_parent_node(node)
	else:
		return ''

def html_for_url_node(node):
	if not re.match("javascript:", node['url']):
		return '<dt><a href="%s">%s</a>\n' % (sanitize(node['url']), sanitize(node['name']))
	else:
		return ''

def html_for_parent_node(node):
	return '<dt><h3>%s</h3>\n<dl><p>%s</dl><p>\n' % (sanitize(node['name']),
			''.join([html_for_node(n) for n in node['children']]))

def version_text():
	old_out = sys.stdout
	sys.stdout = sys.stderr

	print script_name, script_version
	print "(c) 2011, Benjamin Esham"
	print "https://github.com/bdesham/py-chrome-bookmarks"

	sys.stdout = old_out

def help_text():
	version_text()

	old_out = sys.stdout
	sys.stdout = sys.stderr

	print
	print "usage: python " + script_name + " mode input-file output-file"
	print "  mode is one of bookmark or history"
	print "  input-file is the Chrome bookmarks or history file"
	print "  output-file is the destination for the generated HTML bookmarks file"

	sys.stdout = old_out

def outputBookmarks():
	try:
		out = open(out_file, 'w')
	except IOError, e:
		print >> sys.stderr, script_name + ": error opening the output file."
		print >> sys.stderr, e
		exit()
	out.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>

	<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
	<title>Bookmarks</title>
	<h1>Bookmarks</h1>

	<dl><p>

	<dl>%(bookmark_bar)s</dl>

	<dl>%(other)s</dl>
	"""
		% {'bookmark_bar': html_for_node(j['roots']['bookmark_bar']),
			'other': html_for_node(j['roots']['other'])})
        out.close()

def outputHistory():
	try:
		out = open(out_file, 'w')
	except IOError, e:
		print >> sys.stderr, script_name + ": error opening the output file."
		print >> sys.stderr, e
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

# check for help or version requests

if "-v" in sys.argv or "--version" in sys.argv:
	version_text()
	exit()

if len(sys.argv) != 4 or "-h" in sys.argv or "--help" in sys.argv:
	help_text()
	exit()

# the actual code here...

mode_str = os.path.expanduser(sys.argv[1]).lower()
in_file = os.path.expanduser(sys.argv[2])
out_file = os.path.expanduser(sys.argv[3])

MODE_BOOKMARKS=1
MODE_HISTORY=2

if mode_str == "bookmark":
    mode=MODE_BOOKMARKS
elif mode_str == "history":
    mode=MODE_HISTORY
else:
    fatal("mode should be either 'bookmark' or 'history'")


if mode == MODE_BOOKMARKS:
    try:
	f = open(in_file, 'r')
    except IOError, e:
	print >> sys.stderr, script_name + ": error opening the input file."
	print >> sys.stderr, e
	exit()

    j = json.loads(f.read())
    f.close()
    outputBookmarks()
elif mode == MODE_HISTORY:

    connection = sqlite3.connect(in_file)
    curs = connection.cursor()
    outputHistory()
else:
    fatal("Unknown mode <" + str(mode) + ">")


