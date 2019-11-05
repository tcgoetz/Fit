
deps:
	pip install --upgrade --requirement requirements.txt

remove_deps:
	pip uninstall --requirement requirements.txt
	
clean:
	rm -f *.pyc
