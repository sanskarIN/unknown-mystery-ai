PYTHON ?= python

.PHONY: install test examples project-catalog projects project-snapshots release-check build clean

install:
	$(PYTHON) -m pip install -e .

test:
	$(PYTHON) -m unittest discover -s tests -v

examples:
	@for file in examples/[0-9][0-9]_*.py; do \
		echo "==> $$file"; \
		$(PYTHON) $$file || exit 1; \
	done

project-catalog:
	$(PYTHON) scripts/check_project_catalog.py

projects:
	$(PYTHON) scripts/check_projects.py

project-snapshots:
	$(PYTHON) scripts/check_project_snapshots.py

release-check:
	$(PYTHON) scripts/check_release_candidate.py

build:
	$(PYTHON) -m build

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache __pycache__

# Official publication: https://ramsandesh.gumroad.com
