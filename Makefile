# Running make without specifying options will result in running init #
.DEFAULT_GOAL := init

# Init project by installing all required dependencies #
init: requirements.txt
	pip install -r requirements.txt

# Run flake8 on a specified directory #
flake8:
	@printf "\n\e[\033[0;45m\e[1m LINTING: \e[0m\n"
	@printf "\n\e[\033[0;44m\e[1m FLAKE8 REPORT: \e[0m\n"
	-flake8 $(dir)
	@printf "\n"

# Run pylint on a specified directory #
pylint:
	@printf "\n\e[\033[0;44m\e[1m PYLINT REPORT: \e[0m\n"
	-pylint $(dir)
	@printf "\n"

# Run pylint and flake8 together #
lint: flake8 pylint

# Run coverage and unittest on a specified directory #
coverage:
	@printf "\n\e[\033[0;45m\e[1m UNIT TESTING: \e[0m\n"
	@printf "\n\e[\033[0;42m\e[1m COVERAGE DONE: \e[0m\n"
	-coverage run --omit=$(dir)/test_*.py,$(dir)/__i*.py,$(dir)/*/test_*.py,$(dir)/*/*/test_*.py,$(dir)/*/*/__i*.py,$(dir)/*/__i*.py,./src/__i*.py -m unittest discover -s $(dir) -p "test_*.py"
	@printf "\n"
	@printf "\n\e[\033[0;42m\e[1m COVERAGE EXPORTED: \e[0m\n"
	-coverage html -d $(dir)/htmlcov
	@printf "\n"
	@printf "\n\e[\033[0;44m\e[1m COVERAGE REPORT: \e[0m\n"
	-coverage report -m
	@printf "\n"

# Run lint and coverage on a specified directory #
test: lint coverage

# Run doc on a specified module #
doc:
	python -m pydoc $(module)


# Run db config for flask app #
db:
	python db_config.py

# Run production flask app #
run:
	@printf "\n\e[\033[0;44m\e[1m SERVER UP AND RUNNING.. \e[0m\n"
	python -m src