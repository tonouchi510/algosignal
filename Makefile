
install:
	@curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	@source $HOME/.poetry/env
	@poetry install

pandoc:
	pandoc --from markdown --to rst README.md -o README.rst