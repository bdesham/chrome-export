#!/usr/bin/python

import json, sys, os, re

# html escaping code from http://wiki.python.org/moin/EscapingHtml

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    """Produce entities within text."""
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

in_file = os.path.expanduser(sys.argv[1])
out_file = os.path.expanduser(sys.argv[2])

f = open(in_file, 'r')
file_contents = f.read()
f.close()

j = json.loads(file_contents)

out = open(out_file, 'w')

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
