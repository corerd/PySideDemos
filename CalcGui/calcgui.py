#!/usr/bin/env python

'''
ULTRA QUICK GUIS WITH QTDESIGNER/PYTHON
Derived from:
https://vcansimplify.wordpress.com/2013/04/08/ultra-quick-guis-with-wxformbuilderpython/

Usage
Insert any valid mathematical expression in the Text Box and get the result.

This script depends on Qt Designer ui files.
The depending rules are declared in a Makefile.
Run using:
    make run

References:
http://it.toolbox.com/blogs/enlightenment/pyside-tutorial-using-qt-designer-with-pyside-66012
'''

from sys import argv, exit
from mainctrl import GuiApplication


if __name__ == "__main__":
    # Create and show a Gui application
    app = GuiApplication(argv)
    app.window.show()
    # Enter Gui application main loop
    exit(app.exec_())
