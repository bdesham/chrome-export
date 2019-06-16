man:
	pandoc --standalone --to man \
		man_pages/export-chrome-bookmarks.md --output man_pages/export-chrome-bookmarks.1
	pandoc --standalone --to man \
		man_pages/export-chrome-history.md --output man_pages/export-chrome-history.1
