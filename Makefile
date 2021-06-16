
PROJECT_BASE=$(CURDIR)
export PROJECT_BASE

include defines.mk

all: deps

install:
	python3 setup.py install

uninstall:
	pip3 uninstall -y fit

deps:
	pip3 install --upgrade --requirement requirements.txt

devdeps:
	pip3 install --upgrade --requirement dev-requirements.txt

remove_deps:
	# pip3 uninstall -y --requirement requirements.txt
	pip3 uninstall -y --requirement dev-requirements.txt

test:
	$(MAKE) -C test

verify_commit: test

flake8:
	python3 -m flake8 fit/*.py fit/conversions/*.py fit/exceptions/*.py fit/field_enums/*.py --max-line-length=180 --ignore=E203,E221,E241,W503

clean:
	$(MAKE) -C test clean
	rm -f *.pyc
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf Fit.egg-info

.PHONY: deps remove_deps test verify_commit clean
