ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV = venv/bin
ACTIVATE = . venv/bin/activate;

run:
	# Note you can't pass args (directly) using Make run
	# Use ./run.py
	$(ROOT_DIR)/$(VENV)/python -m vacation.vacation

test:
	$(ROOT_DIR)/$(VENV)/nosetests vacation --verbose --detailed-errors --with-coverage --cover-tests --cover-package=vacation --cover-inclusive

deploy_test:
	# Requires access and a .pypirc file
	$(ROOT_DIR)/$(VENV)/python setup.py sdist upload -r pypitest

deploy:
	# Requires bumping version, pypi access and a .pypirc file
	$(ROOT_DIR)/$(VENV)/python setup.py sdist upload -r pypi
