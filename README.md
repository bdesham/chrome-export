# py-chrome-bookmarks [![Build Status](https://travis-ci.org/bdesham/py-chrome-bookmarks.svg?branch=master)](https://travis-ci.org/bdesham/py-chrome-bookmarks)

Scripts to convert [Google Chrome]’s bookmarks and history to the [standard HTML-ish bookmarks file format][format].

[Google Chrome]: http://www.google.com/chrome/
[format]: https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx

The functionality to do this for bookmarks is already built into Chrome (select Bookmarks&nbsp;→ Bookmarks Manager, then click “Organize” and select “Export Bookmarks…”). I wrote this script to be able to perform this conversion in a cron script.

## Usage

These scripts require Python, either version 2.7.x or else version 3.2 or later. They should work on Linux, macOS, and Windows.

### Bookmarks script

From the command line, do

    python py-chrome-bookmarks.py .../path/to/Chrome/Bookmarks output.html

The script will ignore URLs that start with “javascript:”.

### History script

From the command line, do

    python py-chrome-history.py .../path/to/Chrome/History output.html

**Note:** it’s probably necessary to quit Chrome before running this so that the history database isn’t locked. Alternately, make a copy of Chrome’s History file and run the script on that.

The script will ignore history entries with empty titles.

## Feature wishlist

I’ll implement these when I get around to them…

* Make a educated guess for the input filename based on the OS
* Print to stdout if no output filename is given

## Notes for developers

To test changes to the scripts, run the shell script `test/run_tests`. The script runs the bookmarks and history scripts and verifies that their output is identical to what is expected.

## Version history

* 1.1 (2011-04-06)
    - Added help and version text (and started counting versions).
    - Added some checking for errors while opening the input or output files.
* 1.0
    - Initial release

## Author

This program was created by [Benjamin Esham](https://esham.io).

This project is [hosted on GitHub](https://github.com/bdesham/py-chrome-bookmarks). Please feel free to submit pull requests.

## License

Copyright © 2011, 2017 Benjamin D. Esham. This program is released under the ISC license, which you can find in the file LICENSE.md.
