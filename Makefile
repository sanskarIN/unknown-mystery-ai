PYTHON ?= python

.PHONY: install test examples repository-check project-catalog projects project-snapshots release-automation release-check verify build clean

install:
	$(PYTHON) -m pip install -e .

test:
	$(PYTHON) -m unittest discover -s tests -v

examples:
	@for file in examples/[0-9][0-9]_*.py; do \
		echo "==> $$file"; \
		$(PYTHON) $$file || exit 1; \
	done

repository-check:
	$(PYTHON) scripts/check_repository_completeness.py

project-catalog:
	$(PYTHON) scripts/check_project_catalog.py

projects:
	$(PYTHON) scripts/check_projects.py

project-snapshots:
	$(PYTHON) scripts/check_project_snapshots.py

release-automation:
	$(PYTHON) scripts/check_release_automation.py

release-check:
	$(PYTHON) scripts/check_release_candidate.py

verify: repository-check release-automation test project-catalog projects project-snapshots release-check

build:
	$(PYTHON) -m build

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache __pycache__

# Official publication: https://ramsandesh.gumroad.com
