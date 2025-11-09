
export PROJECT_BASE=$(CURDIR)
export VENV=$(PROJECT_BASE)/../.venv


include defines.mk

$(info $$PROJECT_BASE is [${PROJECT_BASE}])
$(info $$VENV is [${VENV}])
$(info $$PLATFORM is [${PLATFORM}])
$(info $$SHELL is [${SHELL}])

export PIP_PATH=$(VENV)/bin/$(PIP)
$(info $$PIP_PATH is [${PIP_PATH}])
export PYTHON_PATH=$(VENV)/bin/$(PYTHON)
$(info $$PYTHON_PATH is [${PYTHON_PATH}])

all: deps

build:
	$(PYTHON_PATH) -m build

$(PROJECT_BASE)/dist/$(MODULE)-*.whl: build

install: $(PROJECT_BASE)/dist/$(MODULE)-*.whl
	$(PIP_PATH) install --upgrade --force-reinstall $(PROJECT_BASE)/dist/$(MODULE)-*.whl 

install_pip:
	$(PIP_PATH) install --upgrade --force-reinstall fitfile 

uninstall:
	$(PIP_PATH) uninstall -y fitfile

reinstall: clean uninstall install

dist: install

publish_check: dist
	$(PYTHON_PATH) -m twine check dist/*

publish: clean publish_check
	$(PYTHON_PATH) -m twine upload dist/* --verbose

deps:
	$(PIP_PATH) install --upgrade --requirement requirements.txt

devdeps:
	$(PIP_PATH) install --upgrade --requirement dev-requirements.txt

remove_deps:
	# $(PIP_PATH) uninstall -y --requirement requirements.txt
	$(PIP_PATH) uninstall -y --requirement dev-requirements.txt

test:
	$(MAKE) -C test

verify_commit: test

flake8:
	$(PYTHON_PATH) -m flake8 fitfile/*.py fitfile/conversions/*.py fitfile/exceptions/*.py fitfile/field_enums/*.py --max-line-length=180 --ignore=E203,E221,E241,W503

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
