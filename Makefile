run:
	poetry run api.main:app --reload  --port 9000

format:
	poetry run black api