#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print('saving the clipboard to key ' + sys.argv[2].lower())
    mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if (sys.argv[2].lower() == 'all'):
        answer = input('Are you sure to delete all records? Y or N?')
        if (answer.lower() == 'y' or answer.lower() == 'yes'):
            mcbShelf.clear()
    else:
        print('deleting the clipboard to key ' + sys.argv[2].lower())
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        print('loading all mcb to clipboard ' + str(list(mcbShelf.keys())))
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        print('loading key ' + sys.argv[1] +' to clipboard ' + mcbShelf[sys.argv[1]])
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()