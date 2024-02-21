
export PROJECT_BASE=$(CURDIR)


include defines.mk


all: deps

build:
	$(PYTHON) -m build

$(PROJECT_BASE)/dist/$(MODULE)-*.whl: build

install: $(PROJECT_BASE)/dist/$(MODULE)-*.whl
	$(PIP) install --upgrade --force-reinstall $(PROJECT_BASE)/dist/$(MODULE)-*.whl 

install_pip:
	$(PIP) install --upgrade --force-reinstall fitfile 

uninstall:
	$(PIP) uninstall -y fitfile

reinstall: clean uninstall install

dist: install

publish_check: dist
	$(PYTHON) -m twine check dist/*

publish: clean publish_check
	$(PYTHON) -m twine upload dist/* --verbose

deps:
	$(PIP) install --upgrade --requirement requirements.txt

devdeps:
	$(PIP) install --upgrade --requirement dev-requirements.txt

remove_deps:
	# $(PIP) uninstall -y --requirement requirements.txt
	$(PIP) uninstall -y --requirement dev-requirements.txt

test:
	$(MAKE) -C test

verify_commit: test

flake8:
	$(PYTHON) -m flake8 fitfile/*.py fitfile/conversions/*.py fitfile/exceptions/*.py fitfile/field_enums/*.py --max-line-length=180 --ignore=E203,E221,E241,W503

test_clean:
	$(MAKE) -C test clean

clean: test_clean
	$(MAKE) -C test clean
	rm -f *.pyc
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

merge_develop:
	git fetch --all && git merge remotes/origin/develop

.PHONY: deps remove_deps test verify_commit clean install uninstall dist build publish_check publish merge_develop
