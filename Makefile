install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black \Codes/*.py 

test:
	python -m pytest \Codes/Test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=\Codes/Check_.*?py \Codes/*.py

all: install format lint test
