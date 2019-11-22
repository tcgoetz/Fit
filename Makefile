
PROJECT_BASE=$(CURDIR)
export PROJECT_BASE

PIP ?= pip3

deps:
	$(PIP) install --user --upgrade --requirement requirements.txt

remove_deps:
	$(PIP) uninstall --requirement requirements.txt

test:
	$(MAKE) -C test

clean:
	$(MAKE) -C test clean
	rm -f *.pyc

.PHONY: deps remove_deps test clean
