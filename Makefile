test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd foreignform/staticapp/

database:
	dropdb foreignform --if-exists
	createdb foreignform
