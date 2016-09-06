# py-chrome-bookmarks

Simple Python script to convert [Google Chrome](http://www.google.com/chrome)’s bookmarks and history to the [standard HTML-ish bookmarks file format](http://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx).

The functionality to do this for bookmarks is already built into Chrome (select Bookmarks → Bookmarks Manager, then click “Organize” and select “Export Bookmarks…”). I wrote this script to be able to perform this conversion in a cron script.

## Usage

### Bookmarks

From the command line, do

    python py-chrome-bookmarks.py bookmark .../path/to/Chrome/Bookmarks output.html

The script will ignore URLs that start with “javascript:”.

### History

From the command line, do

    python py-chrome-history.py history .../path/to/Chrome/History output.html

**Note:** it’s probably necessary to quit Chrome before running this so that the history database isn’t locked. Alternately, make a copy of Chrome’s History file and run the script on that.

The script will ignore history entries with empty titles.

## Version history

* 1.1
    - Added help and version text (and started counting versions). Added some checking for errors while opening the input or output files.
* 1.0
    - Initial release

## Feature wishlist

I’ll implement these when I get around to them…

* Identify the earliest version of Python that will run this script and add that to the README
* Make a educated guess for the input filename based on the OS
* Print to stdout if no output filename is given

## Author

This program was created by [Benjamin Esham](https://esham.io).

This project is [hosted on GitHub](https://github.com/bdesham/py-chrome-bookmarks). Please feel free to submit pull requests.

## License

Copyright © 2011 Benjamin D. Esham. This program is released under the ISC license, which you can find in the file LICENSE.md.
