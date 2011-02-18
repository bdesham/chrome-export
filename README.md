# py-chrome-bookmarks

A simple Python script to convert [Google Chrome](http://www.google.com/chrome)’s bookmarks to the [standard HTML-ish bookmarks file format](http://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx).  Script written by Benjamin Esham <bdesham@gmail.com>.

The functionality to do this is already built into Chrome (select Bookmarks → Bookmarks Manager, then click “Organize” and select “Export Bookmarks…”).  I wrote this script to be able to perform this conversion in a cron script.

## Usage

From the command line, do

    python py-chrome-bookmarks.py .../path/to/Chrome/Bookmarks output.html

## Feature wishlist

I’ll implement these when I get around to them…

* Identify the earliest version of Python that will run this script and add that to the README
* Make a educated guess for the input filename based on the OS
* Print to stdout if no output filename is given

## Links

This script is [hosted on GitHub](https://github.com/bdesham/py-chrome-bookmarks).

## License

Copyright © 2011, Benjamin Esham.  This software is released under the following version of the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following condition: the above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.**
