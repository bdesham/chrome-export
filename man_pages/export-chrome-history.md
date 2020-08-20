% EXPORT-CHROME-HISTORY(1) chrome-export

# NAME

**export-chrome-history** -- convert Google Chrome's history to the standard bookmarks file format

# SYNOPSIS

**export-chrome-history** `[input_file] output_file`

# OPTIONS

`input_file`
: The Chrome history file to read. If you do not specify one, the script will try to locate and use the default Chrome history file.

`output_file`
: The path where the bookmarks file will be written.

# DESCRIPTION

This script will read the given history file (attempting to discover it first, if necessary) and then write all of the entries in the standard HTML-ish bookmarks file format described at <https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx>.

The script will ignore history entries with empty titles.

# EXIT STATUS

export-chrome-history will return zero if it successfully reads the history file and writes the bookmarks file. It will return a nonzero code otherwise.

# AUTHOR

This program was created by Benjamin Esham (https://esham.io).

# PROJECT

This script is part of the chrome-export project, which is hosted at <https://github.com/bdesham/chrome-export>.

# LICENSE

Copyright © 2011, 2017–2018 Benjamin D.\ Esham. This program is released under the ISC license, which you can find at <https://github.com/bdesham/chrome-export/blob/main/LICENSE.md>.
