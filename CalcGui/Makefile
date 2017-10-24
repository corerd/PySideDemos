###
# Qt Designer + PySide = Python GUIs
#
# This Makefile contains the rules to run a TARGET Python script
# that depends on Qt Designer ui files.
##
TARGET = calcgui.py

# View implementation Python scripts
# generated from the corresponding Qt Designer ui files
VIEWS = mainwindow.py


# Rule to generate Python scripts from Qt Designer ui files
%.py: %.ui
	pyside-uic $< -o $@

# The .PHONY rule keeps make from doing something with a file named run
.PHONY: run

# Run the TARGET
run: $(VIEWS)
	python $(TARGET)
