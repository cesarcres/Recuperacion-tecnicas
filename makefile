PYTHON = python
MAIN_FILE = main.py
TEST_FILE = test.py

all: test

main:
	$(PYTHON) $(MAIN_FILE) prefijo

test:
	$(PYTHON) -m unittest $(TEST_FILE)

clean:
	rm -rf __pycache__  # Elimina los archivos de caché de Python
	rm -f *.pyc         # Elimina los archivos compilados de Python