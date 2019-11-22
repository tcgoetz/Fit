#
# This Makefile automates running tests for the project.
#
PROJECT_BASE ?= $(CURDIR)/..

PYTHON=python3
PYTHONPATH=${PROJECT_BASE}/..
export PYTHONPATH

TEST_GROUPS=fit_field_enum fit_dependant_field

#
# Over all targets
#
all: $(TEST_GROUPS)

clean:
	rm -f *.pyc
	rm -f *.log
	rm -f *.txt

#
# Targets for testing smaller slices of functionality.
#
$(TEST_GROUPS):
	$(PYTHON) test_$@.py
