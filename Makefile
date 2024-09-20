PY = ./.venv/bin/python3
MANAGE = src/manage.py


freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

.venv/bin/python3:
	python3 -m venv .venv

.venv/bin/activate: requirements.txt .venv/bin/python3
	${PY} -m pip install -r requirements.txt

run: .venv/bin/activate
	${PY} ${MANAGE} runserver

makemigrations: .venv/bin/activate
	${PY} ${MANAGE} makemigrations

migrate: .venv/bin/activate
	${PY} ${MANAGE} migrate

automigrate: .venv/bin/activate
	${PY} ${MANAGE} makemigrations
	${PY} ${MANAGE} migrate