# chrome-export [![Build status](https://github.com/bdesham/chrome-export/actions/workflows/main.yaml/badge.svg)](https://github.com/bdesham/chrome-export/actions/workflows/main.yaml)

*Formerly called py-chrome-bookmarks*

Python scripts to convert [Google Chrome]’s bookmarks and history to the [standard HTML-ish bookmarks file format][format].

[Google Chrome]: http://www.google.com/chrome/
[format]: https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx

The functionality to do this for bookmarks is already built into Chrome (select Bookmarks&nbsp;→ Bookmarks Manager, then click “Organize” and select “Export Bookmarks…”). I wrote this script to be able to perform this conversion in a cron script.

## Installation

### Homebrew

If you have [Homebrew] installed, you can install these scripts with

    brew install chrome-export

[Homebrew]: https://brew.sh

### Nix

If you’re using the [Nix] package manager, run

    nix-env -i -A nixpkgs.chrome-export

If you use NixOS, run

    nix-env -i -A nixos.chrome-export

[Nix]: https://nixos.org/nix/

### Manual installation

Download the .zip or .tar.gz file for the [latest release], extract it, and move the `export-chrome-bookmarks` and/or `export-chrome-history` files to somewhere on your PATH. You may also want to move `export-chrome-bookmarks.1` and `export-chrome-history.1` from the `man_pages` directory to somewhere on your MANPATH (e.g. `/usr/local/share/man/man1`).

[latest release]: https://github.com/bdesham/chrome-export/releases/latest

## Usage

These scripts require Python, either version 2.7.x or else version 3.2 or later. They should work on Linux, macOS, and Windows.

### Bookmarks script

The usage is

    export-chrome-bookmarks [input_file] output_file

If you do not specify an input file, the script will try to open the default Chrome bookmarks file.

The script will ignore URLs that start with “javascript:”.

### History script

The usage is

    export-chrome-history [input_file] output_file

If you do not specify an input file, the script will try to open the default Chrome history file.

The script will ignore history entries with empty titles.

## Notes for developers

To test changes to the scripts, run `bash test/run_tests`. This script runs both programs and verifies that their output is identical to what is expected. If you have already installed the programs somewhere and want to test those copies, run `bash test/run_tests /path/to/bin`, where `/path/to/bin` is the directory where export-chrome-bookmarks and export-chrome-history are located.

The man pages are written in Markdown; run `make man` to use Pandoc to convert them into the man format. The generated versions are checked into Git so that users don’t have to install Pandoc.

## Version history

* 2.0.2 (2019-06-15)
    - Added man pages and made the testing script more flexible. No changes to functionality.
* 2.0.1 (2018-02-09)
    - Fixed an error that occurred when trying to open the default bookmarks file under Python 2.7. (Thanks [Hridoy Sankar Dutta](https://github.com/hridaydutta123)!)
* 2.0 (2018-02-05)
    - Renamed the project from “py-chrome-bookmarks” to “chrome-export”; renamed “py-chrome-bookmarks.py” to “export-chrome-bookmarks”; and renamed “py-chrome-history.py” to “export-chrome-history”. There were no changes in functionality.
* 1.2.1 (2017-06-02)
    - Fixed a Unicode decoding error under Windows 7. (Thanks [Boburmirzo Hamraqulov](https://github.com/bzimor)!)
* 1.2 (2017-01-26)
    - Added support for Python 3, dropped support for Python 2.6 and earlier, and made this all clear in the readme.
    - Giving an input filename is now optional for both scripts. If you omit the input filename then the scripts will try to open Chrome’s bookmarks or history file automatically.
    - The history script now makes a copy of the input file before opening it. Previously, it was necessary either to make a copy yourself or to quit Chrome before running the script. (The history file is a SQLite database and it isn’t possible for two programs to have it open at the same time.)
* 1.1 (2011-04-06)
    - Added help and version text (and started counting versions).
    - Added some checking for errors while opening the input or output files.
* 1.0
    - Initial release

## Author

These programs were created by [Benjamin Esham](https://esham.io).

This project is [hosted on GitHub](https://github.com/bdesham/chrome-export). Please feel free to submit pull requests.

## License

Copyright © 2011, 2017–2018 Benjamin D. Esham. This program is released under the ISC license, which you can find in the file LICENSE.md.
