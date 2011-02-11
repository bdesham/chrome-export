#!/usr/bin/python

import json, sys, xml.sax.saxutils, os

def escape_text(string):
	return xml.sax.saxutils.escape(string.encode('utf-8'))

def get_child_urls(node):
	for c in node['children']:
		if 'url' in c and not c['url'].startswith('javascript:'):
			out.write('<dd><a href="%s">%s</a></dd>' % (escape_text(c['url']), escape_text(c['name'])))
		if 'children' in c:
			out.write("<dt>%s</dt><dd><dl>" % escape_text(c['name']))
			get_child_urls(c)
			out.write("</dl></dd>")

in_file = os.path.expanduser(sys.argv[1])
out_file = os.path.expanduser(sys.argv[2])

f = open(in_file, 'r')
file_contents = f.read()
f.close()

j = json.loads(file_contents)

out = open(out_file, 'w')

out.write("""<html>

<head>
<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
<title>Chrome Bookmarks</title>
</head>

<body>

<dl>

<dt>Bookmark Bar</dt><dd><dl>
%(bookmark_bar)s
</dl></dd>

<dt>Other</dt><dd><dl>
%(other)s
</dl></dd>

</dl></body></html>"""
	% {'bookmark_bar': get_child_urls(j['roots']['bookmark_bar']),
		'other': get_child_urls(j['roots']['other'])})

out.close()
