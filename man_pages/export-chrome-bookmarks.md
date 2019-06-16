% EXPORT-CHROME-BOOKMARKS(1) chrome-export

# NAME

**export-chrome-bookmarks** -- convert Google Chrome's bookmarks to the standard bookmarks file format

# SYNOPSIS

**export-chrome-bookmarks** `[input_file] output_file`

# OPTIONS

`input_file`
: The Chrome bookmarks file to read. If you do not specify one, the script will try to locate and use the default Chrome bookmarks file.

`output_file`
: The path where the bookmarks file will be written.

# DESCRIPTION

This script will read the given bookmarks file (attempting to discover it first, if necessary) and then write these bookmarks in the standard HTML-ish format described at <https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx>.

Any bookmarks whose URLs start with "javascript:" will be ignored.

# EXIT STATUS

export-chrome-bookmarks will return zero if it successfully reads and writes the bookmarks files. It will return a nonzero code otherwise.

# AUTHOR

This program was created by Benjamin Esham (https://esham.io).

# PROJECT

This script is part of the chrome-export project, which is hosted at <https://github.com/bdesham/chrome-export>.

# LICENSE

Copyright © 2011, 2017–2018 Benjamin D.\ Esham. This program is released under the ISC license, which you can find at <https://github.com/bdesham/chrome-export/blob/master/LICENSE.md>.
