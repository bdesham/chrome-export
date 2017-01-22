#!/usr/bin/python

# py-chrome-bookmarks
# 
# A script to convert Google Chrome's bookmarks file to the standard HTML-ish
# format.
#
# Copyright (c) 2011, 2017 Benjamin D. Esham. This program is released under the
# ISC license, which you can find in the file LICENSE.md.

from __future__ import print_function
from json import loads
from os.path import expanduser
from re import match
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

def html_for_node(node):
	if 'url' in node:
		return html_for_url_node(node)
	elif 'children' in node:
		return html_for_parent_node(node)
	else:
		return ''

def html_for_url_node(node):
	if not match("javascript:", node['url']):
		return '<dt><a href="%s">%s</a>\n' % (sanitize(node['url']), sanitize(node['name']))
	else:
		return ''

def html_for_parent_node(node):
	return '<dt><h3>%s</h3>\n<dl><p>%s</dl><p>\n' % (sanitize(node['name']),
			''.join([html_for_node(n) for n in node['children']]))

def version_text():
	print("py-chrome-bookmarks {}".format(script_version), file=stderr)
	print("(c) 2011, 2017 Benjamin D. Esham", file=stderr)
	print("https://github.com/bdesham/py-chrome-bookmarks", file=stderr)

def help_text():
	version_text()

	print("")
	print("usage: python py-chrome-bookmarks input-file output-file", file=stderr)
	print("  input-file is the Chrome bookmarks file", file=stderr)
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

try:
	f = open(in_file, 'r')
except IOError as e:
	print("py-chrome-bookmarks: error opening the input file.", file=stderr)
	print(e, file=stderr)
	exit()

j = loads(f.read())
f.close()

try:
	out = open(out_file, 'w')
except IOError as e:
	print("py-chrome-bookmarks: error opening the output file.", file=stderr)
	print(e, file=stderr)
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
