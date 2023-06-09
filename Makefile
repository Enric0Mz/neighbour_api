PYTHON := python
RUN := poetry run

run:
	@${RUN} uvicorn api.main:app --reload  --port 9000

format:
	@echo "Running black"
	@${RUN} black api tests

	@echo "Running isort"
	@${RUN} isort api tests --profile=black --line-length=79

	@echo "Running autoflake"
	@${RUN} autoflake --remove-all-unused-imports --remove-unused-variables --remove-duplicate-keys --expand-star-imports -ir api tests

token:
	@$(PYTHON) -c "import requests; r = requests.post('http://localhost:9000/api/auth/token', data={'username': 'enricovmarquezz@gmail.com', 'password': 'Teste@123'}); print(r.json().get('access_token'))"
