VENV=venv/bin/

init:
	python3 -m venv venv
	$(VENV)pip install -U pip
	$(VENV)pip install -Ur requirements_dev.txt

build:
	$(VENV)pip install -U setuptools wheel
	$(VENV)python setup.py sdist bdist_wheel

publish:
	$(VENV)pip install -U twine
	$(VENV)twine upload dist/*

pre-commit:
	$(VENV)pre-commit install

mypy:
	$(VENV)mypy {{cookiecutter.package_slug}}

test:
	$(VENV)pytest --exitfirst tests/
	$(VENV)pytest --cov --cov-fail-under=100

format:
	$(VENV)black {{cookiecutter.package_slug}} setup.py tests
	$(VENV)isort --apply

check-format:
	$(VENV)black --check {{cookiecutter.package_slug}} tests/

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f .coverage
	rm -fr .pytest_cache
	rm -fr .mypy_cache

ci: check-format mypy test