# steps

- python3 -m venv venv
- source venv/bin/activate
- pip freeze > requirements.txt
- pip install -r requirements.txt

# with nuitka

- on linux, install first: sudo apt install patchelf
- pip install nuitka
- python -m nuitka --standalone app.py
- run with:
  - ./app.dist/app.bin

# with pyinstaller

- on ubuntu first: sudo apt install -y libpython3.11-dev
- replace 3.11-dev with your version
- pip install pyinstaller
- pyinstaller --onefile app.py
- ./dist/app
