
PROJECT_BASE=$(CURDIR)
export PROJECT_BASE

include defines.mk

all: deps

deps:
	$(PIP) install --user --upgrade --requirement requirements.txt
	$(PIP) install --user --upgrade --requirement dev-requirements.txt

remove_deps:
	# $(PIP) uninstall -y --requirement requirements.txt
	$(PIP) uninstall -y --requirement dev-requirements.txt

test:
	$(MAKE) -C test

flake8:
	flake8 *.py --max-line-length=180 --ignore=E203,E221,E241,W503

clean:
	$(MAKE) -C test clean
	rm -f *.pyc

.PHONY: deps remove_deps test clean
