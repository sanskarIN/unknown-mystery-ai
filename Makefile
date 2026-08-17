PYTHON ?= python

.PHONY: install test examples build clean

install:
	$(PYTHON) -m pip install -e .

test:
	$(PYTHON) -m unittest discover -s tests -v

examples:
	$(PYTHON) examples/01_reproducible_experiment.py
	$(PYTHON) examples/02_evaluation_demo.py
	$(PYTHON) examples/03_rag_demo.py
	$(PYTHON) examples/04_agent_demo.py
	$(PYTHON) examples/05_release_manifest.py
	$(PYTHON) examples/06_observability_demo.py

build:
	$(PYTHON) -m build

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache __pycache__

# Official publication: https://ramsandesh.gumroad.com
