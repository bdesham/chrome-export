#!/usr/bin/env python

# export-chrome-bookmarks
# 
# A script to convert Google Chrome's bookmarks file to the standard HTML-ish
# format.
#
# Copyright (c) 2011, 2017-2018 Benjamin D. Esham. This program is released under the
# ISC license, which you can find in the file LICENSE.md.

from __future__ import print_function
import argparse
import io
from json import loads
from os import environ
from os.path import expanduser
from platform import system
from re import match
from sys import argv, stderr

script_version = "2.0.1"

# html escaping code from http://wiki.python.org/moin/EscapingHtml

html_escape_table = {
	"&": "&amp;",
	'"': "&quot;",
	"'": "&#39;",
	">": "&gt;",
	"<": "&lt;",
	}

output_file_template = """<!DOCTYPE NETSCAPE-Bookmark-file-1>

<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
<title>Bookmarks</title>
<h1>Bookmarks</h1>

<dl><p>

<dl>{bookmark_bar}</dl>

<dl>{other}</dl>
"""

def html_escape(text):
	return ''.join(html_escape_table.get(c,c) for c in text)

def sanitize(string):
	res = ''
	string = html_escape(string)

	for i in range(len(string)):
		if ord(string[i]) > 127:
			res += '&#x{:x};'.format(ord(string[i]))
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
		return '<dt><a href="{}">{}</a>\n'.format(sanitize(node['url']), sanitize(node['name']))
	else:
		return ''

def html_for_parent_node(node):
	return '<dt><h3>{}</h3>\n<dl><p>{}</dl><p>\n'.format(sanitize(node['name']),
			''.join([html_for_node(n) for n in node['children']]))


# Parse the command-line arguments

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
		description="Convert Google Chrome's bookmarks file to the standard HTML-based format.",
		epilog="(c) 2011, 2017-2018 Benjamin D. Esham\nhttps://github.com/bdesham/chrome-export")
parser.add_argument("input_file", type=argparse.FileType('r'), nargs="?",
		help="The location of the Chrome bookmarks file to read. If this is omitted then the script will look for the file in Chrome's default location.")
parser.add_argument("output_file", type=argparse.FileType('w'),
		help="The location where the HTML bookmarks file will be written.")
parser.add_argument("-v", "--version", action="version",
		version="export-chrome-bookmarks {}".format(script_version))

args = parser.parse_args()

# Determine where the input file is

if args.input_file:
	input_file = args.input_file
else:
	if system() == "Darwin":
		input_filename = expanduser("~/Library/Application Support/Google/Chrome/Default/Bookmarks")
	elif system() == "Linux":
		input_filename = expanduser("~/.config/google-chrome/Default/Bookmarks")
	elif system() == "Windows":
		input_filename = environ["LOCALAPPDATA"] + r"\Google\Chrome\User Data\Default\Bookmarks"
	else:
		print('Your system ("{}") is not recognized. Please specify the input file manually.'.format(system()))
		exit(1)

	try:
		input_file = io.open(input_filename, 'r', encoding='utf-8')
	except IOError as e:
		if e.errno == 2:
			print("The bookmarks file could not be found in its default location ({}). ".format(e.filename) +
					"Please specify the input file manually.")
			exit(1)

# Read, convert, and write the bookmarks

contents = loads(input_file.read())
input_file.close()

bookmark_bar = html_for_node(contents['roots']['bookmark_bar'])
other = html_for_node(contents['roots']['other'])

args.output_file.write(output_file_template.format(bookmark_bar=bookmark_bar, other=other))
args.output_file.close()
