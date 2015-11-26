ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV = venv/bin
ACTIVATE = . venv/bin/activate;

run:
	$(ROOT_DIR)/$(VENV)/python vacation/vacation.py

test:
	$(ROOT_DIR)/$(VENV)/nosetests vacation --verbose --detailed-errors --with-coverage --cover-tests
