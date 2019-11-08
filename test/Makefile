#
# This Makefile automates running tests for the project.
#
PYTHON=python

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
