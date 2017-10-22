#!/usr/bin/env python

'''
Verify PySide installation

Defines a simple GUI using Qt Designer which consists of
a centralWidget more two QLabel widgets: one has fixed text,
the text of the other is set runtime with the current PySide version.

This script depends on Qt Designer ui files.
The depending rules are declared in a Makefile.
Run using:
    make run

References:
https://wiki.qt.io/Hello-World-in-PySide
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
