freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt
venv:
	. venv/bin/activate
