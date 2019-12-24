
PROJECT_BASE=$(CURDIR)
export PROJECT_BASE

include defines.mk

all: deps

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
