.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


clean-pyc:
	echo "Clean pycache"
	find ./rentomatic/ -name '__pycache__' -exec rm -rf {} +
	find ./rentomatic/ -name '*.pyc' -exec rm -f {} +
	find ./rentomatic/ -name '*.pyo' -exec rm -f {} +
	find ./rentomatic/ -name '*~' -exec rm -f {} +
	echo "Clean pytest cache"
	find . -name '.pytest_cache' -exec rm -rf {} +

poetry-requirements: ## export poetry requirements
	poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev
	poetry export -f requirements.txt --output requirements-dev.txt --without-hashes --only dev

local-test: clean-pyc ## run test locally
	pytest .
