.PHONY: sever test clean

server:
	python concept_official_copy/server.py

test:
	py.test -x --tb=short test

clean:
	find . -name "*.pyc" | xargs rm || true
