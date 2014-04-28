.PHONY: sever test clean

server:
	python concept_official_copy/server.py

test:
	python -m unittest discover -s test -p '*_test.py'

clean:
	find . -name "*.pyc" | xargs rm || true
