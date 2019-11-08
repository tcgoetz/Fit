
deps:
	pip install --upgrade --requirement requirements.txt

remove_deps:
	pip uninstall --requirement requirements.txt

test:
	$(MAKE) -C test

clean:
	$(MAKE) -C test clean
	rm -f *.pyc

.PHONY: deps remove_deps test clean
