python_command = python3
pip_command = pip3

ifeq ($(OS), Windows_NT)
	python_command = python
	pip_command = pip
endif

run:
	clear
	$(python_command) src/main.py

init:
	$(pip_command) install -r requirements.txt

test:
	clear
	pytest tests/*.py