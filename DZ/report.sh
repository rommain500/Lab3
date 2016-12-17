find . -name '*.py' -type f -exec cat {} + ! -path "*.venv*"
