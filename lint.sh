echo "--------------------------mypy"
poetry run mypy snapshotweb/tests/test1.py
echo "--------------------------flake8"
poetry run flake8 snapshotweb/tests/test1.py
echo "--------------------------black"
poetry run black snapshotweb/tests/test1.py
echo "--------------------------isort"
poetry run isort snapshotweb/tests/test1.py