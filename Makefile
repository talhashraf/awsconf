.PHONY: requirements
requirements:
	pip-compile --output-file requirements.txt requirements.in


.PHONY: develop
develop:
	pip install -r requirements-dev.txt
	pip install -e .


.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
